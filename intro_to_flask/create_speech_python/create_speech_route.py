import os
import openai
from openai import OpenAI
import re #regular expressions module
from markupsafe import escape #protects projects against injection attacks
from intro_to_flask import app
import sys 
sys.dont_write_bytecode = True
from flask import render_template, request, Flask, Blueprint
from .create_speech_form import SpeechmeForm

speech_blueprint = Blueprint('create_speech', __name__)

@speech_blueprint.route('/create_speech',methods=['GET', 'POST'])
@app.route('/create_speech',methods=['GET', 'POST'])
def create_speech():
  form = SpeechmeForm(request.form)
  
  if request.method == 'POST':
      if form.validate() == False:
        return render_template('create_speech.html', form=form)
      else:
        # The following response code adapted from example on: 
        # https://platform.openai.com/docs/api-reference/images
        
        client = OpenAI()
      speech_text= form.prompt.data
      speech_file_path = os.path.join ("intro_to_flask/static", "speechoutput.mp3") 
      response = client.audio.speech.create(
      model="tts-1",
      voice="nova",
      input=speech_text,
      )

      
      response.stream_to_file(speech_file_path)
        
      return render_template('create_speech.html', create_speech_prompt=form.prompt.data,create_speech_response=response.content,success=True)
      
  elif request.method == 'GET':
      return render_template('create_speech.html', form=form)