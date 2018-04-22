from util.Voice import Voice
import util.Listen as Listen
from util.Notify import Notify
from util.Color import Color
from util.Brain import Brain

'''
    This is the main Animus class, Animus itself is considered to have
    human like features to carry out operations
'''

class Animus(object):
    brain = None
    mouth = None
    notifier = None
    color = None
    ear = None

    def __init__(self):
        print('''
      ___   _   _ ________  ____   _ _____ 
     / _ \ | \ | |_   _|  \/  | | | /  ___|
    / /_\ \|  \| | | | | .  . | | | \ `--. 
    |  _  || . ` | | | | |\/| | | | |`--. \\
    | | | || |\  |_| |_| |  | | |_| /\__/ /
    \_| |_/\_| \_/\___/\_|  |_/\___/\____/ 

     ______________________________________                                       
    |                                      |
    | By Vasudev R. Nair                   |
    |______________________________________|                   
    ''')
        #Create Brain
        Animus.Brain = Brain()

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
        Animus.ear = Listen.Listen()

        Animus.ear.color.primary("Say 'Hey there' to start")

        #start infinite listening loop
        self.start()
    
    @staticmethod
    def start():
        while(True):
            speech = Animus.ear.spokenwords()
            
            #if speech is not empty print string
            #run the Brain.py to map the command
            answer = ''
            if speech != "" and speech != None:
                Animus.color.info('You said -')
                Animus.color.primary(speech)
                answer = Animus.Brain.interpret(speech)
                
            if answer != "":
                Animus.color.success(answer)


