import os
import secrets
from flask import current_app
from PIL import Image
from flask import url_for
from flask_mail import Message
from scratchmap import mail

#Function to save the picture into static folder
def save_picture(form_picture):
    #Random hex of 8 bytes
    random_hex = secrets.token_hex(8)
    #When you don't want to use a variable use an underscore
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename)
    #Make Image smaller
    output_size = (125,125)
    new_image = Image.open(form_picture)
    new_image.thumbnail(output_size)
    new_image.save(picture_path)
    #Return the Filename
    return picture_filename

#Function to send email
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f''' To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request, simply ignore this email and no changes will be made.
'''
    mail.send(msg)
