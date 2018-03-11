import wolframalpha
from util.Color import Color
from util.Voice import Voice
import re

app_id = 'L3J57Q-TWXW7R75RT'
'''
Note to self: wolfram returns string to print and speaks
for itself
'''

class Wolfram:
    client = None

    def __init__(self):
        Wolfram.client = wolframalpha.Client(app_id)

    def query(self, text):
        print('Trying wolfram')
        res =   Wolfram.client.query(text)
        answer = next(res.results).text

        #if question is about Animus, override response
        if answer == "My name is Wolfram|Alpha.":
            Voice.speak("My name is Animus, you may call me Ann")
            return "My name is Animus"
        #dont speak additional info within (info) paranthesis
        Voice.speak(re.sub('\(.*?\)', '', answer))

        return answer