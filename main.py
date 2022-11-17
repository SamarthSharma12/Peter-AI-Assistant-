import pyttsx3 
import datetime
import requests
import json
import speech_recognition as sr
import pyautogui
import webbrowser as wb
import wikipedia
import openai 
from time import sleep
import pywhatkit # for youtube video

import random

engine = pyttsx3.init()

# This function is responsible give audio to the text
def give_audio(audio):
  engine.say(audio)
  rate = engine.getProperty('rate')
  engine.setProperty('rate', rate+1)
  engine.runAndWait()
 
# This is the way to switch either Peter or Peri
def change_voice(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
      engine.setProperty('voice',voices[0].id)
      give_audio("Hello Peter this side")
    if voice == 2:
      engine.setProperty('voice',voices[1].id)
      give_audio("Hello  Peri this side")
    
    
# This function will give you tell you about the time 
def time(Region,City):
      response = requests.get('https://timeapi.io/api/Time/current/zone?timeZone={0}/{1}'.format(Region,City))
      python_data= json.loads(response.text)
      time = python_data.get('time')
      date = python_data.get('dateTime')
      audio = "The date of {0} is{1} and time is {2}".format(City,date,time)
      give_audio(audio)


def greeting():
  hour = datetime.datetime.now().hour
  if hour >= 6 and hour <12:
    give_audio("Good Morning Sir")
  elif hour >=12 and hour < 16:
    give_audio("Good Afternoon Sir")
  elif hour >=16 and hour < 22:
    give_audio("Good Evening Sir")
  else:
    give_audio("Good Night Sir")
    
def greet():
  give_audio("I hope you are having a great time")

def gpt3(s):
  openai.api_key = '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'
  response = openai.Completion.create(
    model="text-curie-001",
    prompt=s,
    temperature=0.2,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=0
  )
  name = response['choices'][0].text
  print(name)
  give_audio(name)
  
def wishme(name):
    give_audio("Welcome back {}".format(name))
    give_audio("How may I help you")
    return
    
"""def take_cmd():
  query = input("How may I help you?")
  return query"""


def takeCommandMic():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening .....")
    audio = r.record(source,duration=3)
  try:
    print("recognizing ...")
    query = r.recognize_google(audio,language="en-IN")
    print(query)
  except Exception as e:
     print(e)
     give_audio("Say  that again Please......")
     return 'None'
  return query
  
def sendwhatappmsg(ph_no,msg):
  Message = msg
  wb.open('https://web.whatsapp.com/send?phone='+ph_no+'&text='+Message)
  sleep(10)
  pyautogui.press('enter')
  
def searchgoogle():
  give_audio("what should I search for?")
  search = takeCommandMic()
  wb.open('https://www.google.com/search?q={}'.format(search ))
  


if __name__ == "__main__":
    change_voice(1)
    """give_audio("What your name Sir")
    name = takeCommandMic()"""
    wishme("Samarth")
    greet()
    while True:
      query = takeCommandMic().lower()
      if 'current' and 'time' in query:
        time('Asia','Calcutta')
      elif 'time' in query :
        give_audio("Say Region")
        region = takeCommandMic()
        give_audio("Say City")
        City = takeCommandMic()
        time(region,City)
      elif 'greet' in query:
        greeting()
        
      elif 'message' in query:
        user_name = {"Samarth":"+91 8979090473","Shobhana":"+91 9368134020","Sanjay":"+91 9412861605",
                      }
        try:
          give_audio("To whom you want to send the Whats app message")
          name = takeCommandMic()
          ph_no = user_name[name]
          give_audio("What is the message?")
          message = takeCommandMic()
          sendwhatappmsg(ph_no,message)
          give_audio("Message has been send")
        except Exception as e:
          print(e)
          give_audio("unable to send the message")
          
      elif 'wikipedia' in query:
        give_audio("searching on wikipeida...")
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences = 2)
        print(result)
        give_audio(result)
      elif 'google' in query:
        searchgoogle()
        
      elif 'youtube' in query:
        give_audio("what should I search for on youtube?")
        topic = takeCommandMic()
        pywhatkit.playonyt(topic)
      elif 'weather' in query:
        city = query.replace("weather","")
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=dc1bd9d9718ec49bb299a339416ac853'.format(city)
        
  
      else:
        gpt3(query)
        break
        
# http://api.openweathermap.org/data/2.5/weather?q=Agra&units=imperial&appid=dc1bd9d9718ec49bb299a339416ac853
      
      

#while True:
  #choice = int(input("Enter 1 if you want it in Male voice\nEnter 2 if you want it Female voice\n"))
  #change_voice(choice)
#wishme("Samarth")
#greeting()
