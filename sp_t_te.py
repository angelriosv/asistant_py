from gtts import gTTS
from playsound import playsound

s = gTTS("Hola mundo", lang='es-us')

s.save('sound.mp3')

playsound('sound.mp3')