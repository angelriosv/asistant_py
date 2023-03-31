import pyttsx3

engine = pyttsx3.init()

# engine.setProperty('lang','es')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

engine.say("Hello World")
engine.runAndWait()
