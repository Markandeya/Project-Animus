import speech_recognition as sr
from .Color import Color
from .Voice import Voice
from .Brain import Brain
'''
returns recognised speech or empty string
'''

class Listen:
    r = None
    color = None
    
    def __init__(self):

        Listen.r = sr.Recognizer()
        #Listen.r.dynamic_energy_threshold = True
        Listen.r.energy_threshold = 4000
        Listen.color = Color()

    def spokenwords(self):
        print('.')
        with sr.Microphone() as source:
            #Listen.r.adjust_for_ambient_noise(source)
            
            sr.SAMPLE_RATE = 48000
            print('active mic')
            audio = Listen.r.listen(source)

        try:
            print('in try')
            recog_speech = str(Listen.r.recognize_google(audio))
            if 'hey there' in recog_speech:
                print('heyy')
                Voice.speak("I am listening")
                Listen.color.primary("I'm listening..")
                
                
                with sr.Microphone() as source:
                    sr.SAMPLE_RATE = 48000
                    audio = Listen.r.listen(source)
                    print('listened')
                try:
                    recog_speech = str(Listen.r.recognize_google(audio))
                    return recog_speech

                except sr.UnknownValueError as e:
                    Voice.speak("Sorry, I did not understand")
                    return ""            
                except sr.RequestError as e:
                    Listen.color.alert("There seems to be internet connection problem..")
                    return ""
                except Exception as e:
                    Listen.color.alert('Something bad happened')
                    return ""
            elif 'quit' in recog_speech:
                Listen.color.primary("Goodbye")
                quit()
        
        except sr.UnknownValueError:
            #if user is loitering around and/or has not invoked Animus
            #Animus remains idle listening for Hey there Voice activation
            print('unknown')
            return ""
        except sr.RequestError as e:
            Listen.color.alert("There seems to be an internet connection problem..")
            return ""
        except Exception as e:
            Listen.color.alert('Something bad happened')
            return ""
