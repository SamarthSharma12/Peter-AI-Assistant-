import pyttsx3 
import datetime
import requests
import json
import speech_recognition as sr
engine = pyttsx3.init()

def give_audio(audio):
  engine.say(audio)
  rate = engine.getProperty('rate')
  engine.setProperty('rate', rate+1)
  engine.runAndWait()
def change_voice(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
      engine.setProperty('voice',voices[0].id)
    if voice == 2:
      engine.setProperty('voice',voices[1].id)
    
    
  
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

def wishme(name):
    give_audio("Welcome back {}".format(name))
    give_audio("How may I help you")
    return
    
def take_cmd():
  query = input("How may I help you?")
  return query


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
    
if __name__ == "__main__":
         print("What your name sir")
         name = takeCommandMic()
         wishme(name)
         while True():
            query = takeCommandMic().lower()
            if 'voice' in query:
              print("Choose Voice Number")
              number = takeCommandMic()
              change_voice(number)
            
      
      

#while True:
  #choice = int(input("Enter 1 if you want it in Male voice\nEnter 2 if you want it Female voice\n"))
  #change_voice(choice)
#wishme("Samarth")
#greeting()