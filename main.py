from idlelib import query

import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import datetime


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')  # Recognize speech via Google API
            print(f"You said: {query}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Please repeat.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            return None
        return query


if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jarvis AI")


    while True:
        query = takeCommand()
        sites = [["youtube" , "https://www.youtube.com"] , ["wikipedia" , "https://www.wikipedia.com"] , ["spotify" , "https://open.spotify.com"] , ["google" , "https://www.google.co.in/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} ma'am...")
                webbrowser.open(site[1])


        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:&M:%S")
            say(f"Ma'am the time is {strfTime}")

        