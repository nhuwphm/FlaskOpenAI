import os
import openai
import re #regular expressions module
from markupsafe import escape #protects projects against injection attacks
from intro_to_flask import app
import sys 
sys.dont_write_bytecode = True
from flask import render_template, request, Flask, Blueprint
from .vision_form import VisionmeForm
from openai import OpenAI

vision_blueprint = Blueprint('visionme', __name__)

@app.route('/visionme',methods=['GET', 'POST'])
def visionme():
  form = VisionmeForm(request.form)
  
  if request.method == 'POST':
      if form.validate() == False:
        return render_template('visionme.html', form=form)
      else:
        # The following response code is an (older) from example on: 
        # https://platform.openai.com/docs/api-reference/audio/createTranscription
    
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",

            messages=[
            {
                "role": "user",
                "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                    "url": form.prompt.data,
                    },
                },
                ],
            }
            ],
        max_tokens=300,
        )
        display_text = response.choices[0].message.content
        return render_template('visionme.html', vision_me_prompt=form.prompt.data,vision_me_response=display_text,success=True)
  elif request.method == 'GET':
      return render_template('visionme.html', form=form)