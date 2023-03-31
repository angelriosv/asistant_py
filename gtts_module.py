from gtts import gTTS
from playsound import playsound
from time import sleep
import os


class SpeechModule:
    def __init__(self):
        self

    def talk(self, text):
        self.speech = gTTS(text,lang='es-us')

        self.speech.save('./sound.mp3')
        playsound('sound.mp3')
        os.remove('./sound.mp3')
        sleep(1)

