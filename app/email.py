from flask import current_app, render_template
from flask_mail import Message
from . import mail

def send_email(to, subject, template, **kwargs):
    if not current_app:
        raise Exception #not sure what yet, or if we should???
    msg = Message(subject=current_app.config['RAGTIME_MAIL_SUBJECT_PREFIX'] + subject,
                  recipients=[to],
                  sender=current_app.config['RAGTIME_MAIL_SENDER'])
    msg.body = render_template(template + '.txt', **kwargs)
    #msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)