import packages.Wiki as Wiki 

''' 
    This is the Brain of Animus where it processes user speech 
    to recognisable format ,interprets and executes
'''


class Brain:
    wiki = None

    def __init__(self):
        Brain.wiki = Wiki.Wiki()
    
    def interpret(self,text):
        pass