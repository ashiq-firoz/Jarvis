#front end

import speech_recognition as sr
import pyttsx3 as t_s
import back


def say(string):
    reply= t_s.init()
    reply.say(string)
    reply.runAndWait()


i=0
while i<11:
    r = sr.Recognizer()
    text=" "
    with sr.Microphone() as source:
        audio = r.listen(source)
        say("Say something")
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            say("Cant hear you") 

        if text=="stop":
            break 
    i+=1          

