import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good After Noon')
    else:
        speak('Good Night')

    speak('I am Jarvis Sir, How may I help you?')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..  ')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(f'You said: {query} \n')

    except Exception as e:
        # print(e)

        print('Say it Again ... ')
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ammadhassan803@gmail.com', 'usman.k10')
    server.sendmail('ammadhassan803@gmail.com', to , content)
    server.close()


if __name__ == '__main__':
    wishme()
    if 1:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching in wilipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia ')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'D:\One Plus Data\SnapTube Audio'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[5]))

        elif 'time now' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'The time is {strTime}')

        elif 'open vs code' in query:
            codepath = "C:\\Users\Ammad Hassan\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        elif 'email to bob' in query:
            try:
                speak('What you want to Email?')
                content = takecommand()
                to = 'ammadhassanhi5@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent to Ammad')
            except Exception as e:
                print(e)
                speak('Email is Not sent. Sorry Brother Ammad')
