from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    error_msg="That page doesn't exist."
    return render_template('error.html', error_msg=error_msg), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    error_msg="Sorry, we seem to be experiencing some technical difficulties. Please try again later."
    return render_template("error.html", error_msg=error_msg), 500


@main.app_errorhandler(403)
def internal_server_error(e):
    error_msg="This page is forbidden, you're not supposed to be here."
    return render_template("error.html", error_msg=error_msg), 403
