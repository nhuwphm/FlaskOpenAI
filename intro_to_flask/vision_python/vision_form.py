import sys 
sys.dont_write_bytecode = True
#Need to do the following installs:
# pip install flask-wtf
# pip install email_validator
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, validators, ValidationError

class VisionmeForm(Form):
    prompt = TextAreaField("Put your image here or Give me a link to an image and I will tell you whats in it.",  [validators.InputRequired("Please enter a prompt.")])
    submit = SubmitField("Send") 