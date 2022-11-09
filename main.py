import pyttsx3 
import datetime
import requests
import json
import speech_recognition as sr
import pyautogui
import webbrowser as wb
import wikipedia
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

""" def google_search():
  generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
  text =takeCommandMic()
  result = generator(text, max_length=100, do_sample=True, temperature=0.9)
  print(result[0]['generated_text'])
  give_audio(result[0]['generated_text']) """
  
  
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
  
def sendwhatappmsg(ph_no,msg):
  Message = msg
  wb.open('https://web.whatsapp.com/send?phone='+ph_no+'&text='+msg)
  sleep(10)
  pyautogui.press('enter')


if __name__ == "__main__":
         if 'M' in takeCommandMic():
            change_voice(1)
            give_audio("What your name sir")
            name = takeCommandMic()
            wishme(name)
         else:
            change_voice(2)
            give_audio("What your name Ma'am")
            name = takeCommandMic()
            wishme(name)
         while True:
            query = takeCommandMic().lower()
            if 'time' in query :
              give_audio("Say Region")
              region = takeCommandMic()
              give_audio("Say City")
              City = takeCommandMic()
              time(region,City)
            if 'greet' in query:
              greeting()
              
            if 'message' in query:
              user_name = {"Rishabh":"+91 9354471042","Gautam":"+91 9311450881","Samarth":"+91 8979090473","Shobhana":"+91 9368134020","Sanjay":"+91 9412861605",
                           "Seema Mishra":"+91 9452664323","Suket":"+91 8237862436","Vijaya":"+91 9121952003","Shubham":"+91 9582789002",
                           "Aryaman":"+91 9799805800","Satvik":"+91 9110895517"}
              try:
                give_audio("To whom you want to send the Whats app message")
                name = takeCommandMic()
                ph_no = user_name[name]
                give_audio("What is the message?")
                message = takeCommandMic()
                sendwhatappmsg(ph_no,message)
                give_audio('message to send the message')
              except Exception as e:
                print(e)
                give_audio("unable to esnd the message")
                
            if 'wikipedia' in query:
              give_audio("searching on wikipeida...")
              query = query.replace("wikipedia","")
              result = wikipedia.summary(query,sentences = 2)
              print(result)
              give_audio(result)
              
            """ if 'google' in query:
              google_search() """
              
            if 'stop' in query:
              break
            
      
      

#while True:
  #choice = int(input("Enter 1 if you want it in Male voice\nEnter 2 if you want it Female voice\n"))
  #change_voice(choice)
#wishme("Samarth")
#greeting()