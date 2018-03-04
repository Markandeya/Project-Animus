import packages.Wiki as Wiki
import packages.Wolfram as Wolfram

''' 
    This is the Brain of Animus where it processes user speech 
    to recognisable format ,interprets and executes
'''


class Brain:
    wiki = None
    wolfram = None

    def __init__(self):
        Brain.wiki = Wiki.Wiki()
        Brain.wolfram = Wolfram.Wolfram()

    #Main thinking function

    def interpret(self,text):
        print('Interpreting speech')
        try:
            return Brain.wolfram.query(text)

        except Exception as e:
            print(e)
            return Brain.wiki.query(text)