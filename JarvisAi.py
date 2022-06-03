import audioop
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from random import randint
import smtplib
import sys
import requests
from requests import get
import socket


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

emails = {'shubh':'shubhagar133@gmail.com' , 'abhishek' : "onlyabhiii@gmail.com","chicoo":"reachihit@gmail.com"}


x = random.randint(0,9)



def speak(audio):
    engine.say(audio)
    engine. runAndWait()

time = datetime.datetime.now()

def StartUp():
    Start = int(datetime.datetime.now().hour)
    if Start>=0  and Start<12:
        speak(f"Good Morning Sir The time is {time}")
    elif Start>=12 and Start<16:
        speak(f"Good afternoon sir The time is  {time}")
    else:
        speak(f"Good Evening sir The time is  {time}")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listning to you: ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing")
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("please Say that again..")
        speak("sorry i dint understand you")
        return "None"

    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Shubhagar133@gmail.com', 'Shubh@133')
    server.sendmail('Shubhagar133@gmail.com', to, content)
    server.close()

query =  takecommand().lower()

if __name__ =="__main__":
    if 'jarvis start my day' in query :
        StartUp()
    while "jarvis" in query :
        query =  takecommand().lower()
        #to search something
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'search' in query:
            speak("what should i search")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}") 
            speak("opening google")
            # this is the end of searching
           #This is the start of things to open
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        
        elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak("opening google")
        
        elif 'open email' in query:
            webbrowser.open("www.gmail.com")
            speak("opening your gmail")

        elif 'open stack overflow' in query:
            webbrowser.open("www.stackoverflow.com")
            speak("opening coder's best friend")

        elif 'open code' in query:
                code_path="C:\\Users\\shubh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak("opening visual studio code")
                os.startfile(code_path)

        elif 'open notepad' in query:
                note_path="C:\\Windows\\system32\\notepad.exe"
                speak("opening notepad")
                os.startfile(note_path)
                

        elif 'open chrome' in query:
                chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                speak("opening google chrome")
                os.startfile(chrome_path)

        elif 'open cmd' in query:
            speak("opening command prompt")
            os.system("start cmd")
        
        elif ' my ip' in query:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            print(s.getsockname()[0])
            speak("Sir your IP adresse is "+s.getsockname()[0])
       
        #This is the end of things to open

        #This is the start of things to play
        elif 'play clips' in query:
            clip_dir = "C:\\Users\\shubh\\Videos\\Valorant"
            clips = os.listdir(clip_dir)
            os.startfile(os.path.join(clip_dir , clips[x]))
            speak("playing your opee clips")

         #This is the end of things to play

        #This is the start  of conversations
        elif 'how are you' in query:
            speak("I am having a wonderfull day , hope you are having a great day too")

        elif 'the time' in query:
           z = datetime.datetime.now().strftime("%H:%M")
           speak(f"Sir the time is {z}")

        elif 'am bored' in query:
            speak("Sir, if you dont have to study , you can watch some youtube or play a game on pc , whatever you like")

        #this is the start to sending something
        elif 'send an email' in query:
            try:
                speak('whom should i send it to ?')
                if 'shubh' in takecommand():
                    to = emails['shubh']
                    speak("What should I type ?")
                    content = takecommand()
                    speak("sending email")
                    sendEmail( to ,content)
                    speak("email sent successfully")
                    print("Email sent successfully")
                elif 'Abhishek' in takecommand():
                    to = emails['abhishek']
                    speak("What should I type ?")
                    content = takecommand()
                    speak("sending email")
                    sendEmail( to ,content)
                    speak("email sent successfully")
                    print("Email sent successfully")
                
                elif 'Chiku' in takecommand():
                    to = emails['chicoo']
                    speak("What should I type ?")
                    content = takecommand()
                    speak("sending email")
                    sendEmail( to ,content)
                    speak("email sent successfully")
                    print("Email sent successfully")
                
                    

            except Exception as e:
                print(e)
                speak("Sorry sir ,the email could not be delivered due to some issue")

            #this is the end of sending something 
            # this is to stop jarvis
        elif 'jarvis quit' in query:
            speak("Bye Sir, See you soon")
            sys.exit()


