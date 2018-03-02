from util.Voice import Voice
from util.Listen import Listen
from util.Notify import Notify
from util.Color import Color

'''
    This is the main Animus class, Animus itself is considered to have
    human like features to carry out operations
'''

class Animus(object):
    mouth = None
    notifier = None
    color = None
    ear = None

    def __init__(self):
        
        #Create mouth and Greet user
        Animus.mouth = Voice()
        Animus.mouth.speak('Hello sir, what can I do?')

        #Create notifier and Show initialised notification
        Animus.notifier = Notify()
        Animus.notifier.notify('Good day sir!')

        #Greet in terminal
        Animus.color = Color()
        Animus.color.primary('Animus initialized..')
        
        #Create ear and listen to user
        Animus.ear = Listen()

        #listen and interpret once
        Listen.color.primary("Say something..")

        speech = Animus.ear.spokenwords()
        
        if 'quit' == speech:
            Animus.mouth.speak('Goodbye')
            Animus.color.primary('Goodbye')
            quit()
        
        Animus.color.primary(speech)
        Animus.mouth.speak(speech)

        #start infinite listening loop
        self.start()
    
    @staticmethod
    def start():
        while(True):
            speech = Animus.ear.spokenwords()

            if 'Animus quit' == speech:
                Animus.mouth.speak('Goodbye')
                Animus.color.primary('Goodbye')
                quit()
            
            Animus.color.primary(speech)
            Animus.mouth.speak(speech)

