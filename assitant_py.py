import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

num=0

def speak(num,text):
    tts = gTTS(text=text, lang='es-us')
    filename = 'sound_'+str(num)+'.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Di algo : ')
        audio = r.listen(source)
        said = ''

        try:
            said = r.recognize_google(audio, language='es')
            print(said)
        except Exception as e:
            print('Exception: ' + str(e))

    return said

while True:
    text = get_audio()

    num=num+1

    if text:
        speak(num,text)
    else:
        speak('No te he entendido')


    time.sleep(1)