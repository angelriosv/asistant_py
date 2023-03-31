import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source :
    print("Por favor habla")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="es")
        print(text)
    except:
        print("No te puedo entender")