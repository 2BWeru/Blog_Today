from flask import render_template
from flask_mail import Message
from . import mail
subject_pref = 'Pitch_view'
sender_email = 'jaelweru5@gmail.com'


def mail_message(subject,template,to,**kwargs):
    email = Message(subject_pref+subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)