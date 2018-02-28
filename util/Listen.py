import speech_recognition as sr
from .Color import Color

class Listen:
    r = None
    color = None
    
    def __init__(self):

        self.r = sr.Recognizer()
        print(type(self.r))        
        self.color = Color()

    def spokenwords(self):
        with sr.Microphone() as source:
            self.color.primary("Say something..")
            audio = self.r.listen(source)

        try:
            recog_speech = str(self.r.recognize_google(audio))
            return "You said " + recog_speech
        except sr.UnknownValueError:
            return "Sorry, could you repeat that?"
        except sr.RequestError as e:
            return "There seems to be internet connection problem.."
