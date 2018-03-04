import wolframalpha
from util.Color import Color
from util.Voice import Voice


app_id = 'L3J57Q-TWXW7R75RT'


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
        Voice.speak(answer)

        return answer