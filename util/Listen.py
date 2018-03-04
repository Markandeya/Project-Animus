import speech_recognition as sr
from .Color import Color
from .Voice import Voice
from .Brain import Brain

#base exception
class Error(Exception):
   """Base class for other exceptions"""
   pass

#custom exception
class DidntUnderstandException(Error):
    pass

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
            if 'hey there' in recog_speech:
                
                Voice.speak("I am listening")
                Listen.color.primary("I'm listening..")
                
                
                with sr.Microphone() as source:
                    audio = Listen.r.listen(source)
                
                try:
                    recog_speech = str(Listen.r.recognize_google(audio))
                    return recog_speech

                except sr.UnknownValueError as e:
                    Voice.speak("Sorry, I did not understand")
                    raise DidntUnderstandException

                #if didnt understand give one more go
                except util.Listen.DidntUnderstandException as e:
                    Voice.speak("Lets try again")
                    Listen.color.primary("lets try again..")
                    
                    
                    with sr.Microphone() as source:
                        audio = Listen.r.listen(source)
                    
                    try:
                        recog_speech = str(Listen.r.recognize_google(audio))
                        return recog_speech

                    except sr.UnknownValueError as e:
                        Voice.speak('Sorry, I did not understand')
                    except sr.RequestError as e:
                        return "There seems to be internet connection problem.."
                
                except sr.RequestError as e:
                    return "There seems to be internet connection problem.."
            elif 'quit' in recog_speech:
                Listen.color.primary("Goodbye")
                quit()
        
        except sr.UnknownValueError:
            #if user is loitering around and/or has not invoked Animus
            #Animus remains idle listening for Hey there Voice activation
            return ""
        except sr.RequestError as e:
            return "There seems to be internet connection problem.."
