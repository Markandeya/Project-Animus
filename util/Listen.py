import speech_recognition as sr
from .Color import Color
from .Voice import Voice

class Listen:
    r = None
    color = None
    
    def __init__(self):

        Listen.r = sr.Recognizer()
        Listen.color = Color()

    def spokenwords(self):
        with sr.Microphone() as source:
            audio = Listen.r.listen(source)

        try:
            recog_speech = str(Listen.r.recognize_google(audio))
            if 'hey Siri' in recog_speech:
                Voice.speak("I am listening")
                Listen.color.primary("I'm listening..")
                audio = Listen.r.listen(source)
            return recog_speech
        except sr.UnknownValueError:
            #if user is loitering around and/or has not invoked Animus
            #Animus remains idle listening for Hey Siri Voice activation
            return ""
        except sr.RequestError as e:
            return "There seems to be internet connection problem.."
