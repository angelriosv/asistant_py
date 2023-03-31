import time
from text_to_speech import VoiceRecognitionModule
from gtts_module import SpeechModule

speech = SpeechModule()
recognition = VoiceRecognitionModule()

while True:
    text = recognition.recognize()

    if text:
        speech.talk(text)
        print(text)

    else:
        speech.talk("No te he entendido")

    time.sleep(1)