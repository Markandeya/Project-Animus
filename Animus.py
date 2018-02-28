from util.Voice import Voice
from util.Listen import Listen
from util.Notify import Notify
from util.Color import Color

'''
    This is the main Animus class, Animus itself is considered to have
    human like features to carry out operations
'''

class Animus(object):

    def __init__(self):
        
        #Create mouth and Greet user
        mouth = Voice()
        mouth.speak('Hello sir, what can I do?')

        #Create notifier and Show initialised notification
        notifier = Notify()
        notifier.notify('Good day sir!')

        #Greet in terminal
        color = Color()
        color.primary('Animus initialized..')
        
        #Create ear and listen to user
        ear = Listen()
        speech = ear.spokenwords()
        color.primary(speech)
        mouth.speak(speech)