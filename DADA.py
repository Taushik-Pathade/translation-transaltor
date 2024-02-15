import googletrans
import gtts
import speech_recognition
import playsound

recognizer =  speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak Now")
    voice =recognizer.listen(source)
text = recognizer.recognize_google(voice, language="en")
print(text)

transaltor = googletrans.Translator()
translation = transaltor.translate(text, dest="hi")
print(translation.text)

convertedaudio = gtts.gTTS(translation.text, lang="hi")
convertedaudio.save("voice.mp3")
playsound.playsound("voice.mp3")
