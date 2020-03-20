from flask import session, render_template, redirect, url_for, flash, current_app, request, abort
from flask_login import login_required, current_user
from . import main
from .forms import NameForm, EditProfileForm, EditProfileAdminForm, CompositionForm
from .. import db
from ..models import User, Role, Permission, Composition
from ..email import send_email
from ..decorators import admin_required, permission_required

@main.route('/', methods=['GET', 'POST'])
def home():
    """How the page BEHAVES"""
    form = CompositionForm()
    if current_user.can(Permission.PUBLISH) and form.validate_on_submit():
        composition = Composition(release_type=form.release_type.data,
                                  title=form.title.data,
                                  description=form.description.data,
                                  # database needs a real User object
                                  artist=current_user._get_current_object())
        db.session.add(composition)
        db.session.commit()
        # must be generated after first commit
        composition.generate_slug()
        return redirect(url_for('.home'))
    # page number to render, from request's query string 'page',
    # with default of first page (1), and if type can't be int,
    # return default value
    page = request.args.get('page', 1, type=int)
    # Which page of results do you want? We'll display <per_page> results, and won't
    # throw an error if you go outside how many pages we have!
    pagination = Composition.query.order_by(Composition.timestamp.desc()).paginate(
        page, per_page=current_app.config['RAGTIME_COMPS_PER_PAGE'], error_out=False)
    compositions = pagination.items
    # A ?page=2 will display in address when page selected is 2
    return render_template(
        'home.html',
        form=form,
        compositions=compositions,
        pagination=pagination
    )


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    compositions = user.compositions.order_by(Composition.timestamp.desc()).all()
    return render_template('user.html', user=user, compositions=compositions)


@main.route('/composition/<slug>')
def composition(slug):
    composition = Composition.query.filter_by(slug=slug).first_or_404()
    # Use list so we can pass to _compositions template
    return render_template('composition.html', compositions=[composition])


@main.route('/edit/<slug>', methods=["GET", "POST"])
@login_required
def edit_composition(slug):
    composition = Composition.query.filter_by(slug=slug).first_or_404()
    if current_user != composition.artist and \
            not current_user.can(Permission.ADMIN):
        abort(403)
    form = CompositionForm()
    if form.validate_on_submit():
        composition.release_type = form.release_type.data
        composition.title = form.title.data
        composition.description = form.description.data
        # regenerate in case the title changed
        composition.generate_slug()
        db.session.add(composition)
        db.session.commit()
        flash("Your composition was updated!")
        return redirect(url_for('.composition', slug=composition.slug))
    form.release_type.data = composition.release_type
    form.title.data = composition.title
    form.description.data = composition.description
    return render_template('edit_composition.html', form=form)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        # Change all user information and then save to database
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.bio = form.bio.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Looking good! Your profile was updated.')
        return redirect(url_for('.user', username=current_user.username))
    # Show initial values so user can see what they have already
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.bio.data = current_user.bio
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile-admin/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.bio = form.bio.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('The profile was updated.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    # We must ensure role field gets int data
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.bio.data = user.bio
    return render_template('edit_profile.html', form=form, user=user)


@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def moderate():
    return "For review moderators only!"
