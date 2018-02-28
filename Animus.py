from util.Voice import Voice
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
        mouth.speak('Namaskar वसुदेव, mein apke liye kya karsakti hoon?')

        #Create notifier and Show initialised notification
        notifier = Notify()
        notifier.notify('Good day sir!')

        #Greet in terminal
        color = Color()
        color.colorize('Say something..', 'blue')