import wikipedia
from util.Color import Color
from util.Voice import Voice
import re

'''
Note to self: wiki returns string to print and speaks
for itself
'''

class Wiki:
    color = None 

    def __init__(self):
        Wiki.color = Color()

    def query(self, text=''):
        #print('trying wiki')
        #print(text)
        try:
            answer = wikipedia.summary(text, sentences=2)
            self.color.info('Didnt find what you wanted? Try google : http://google.com/search?q='+re.sub(r' ', '+', text))
            Voice.speak('Heres a summary')
            return answer

        except wikipedia.exceptions.DisambiguationError as de:
            Voice.speak('I am confused')
            Wiki.color.info('Did you mean -')
            Wiki.color.info(de)
            self.color.info('Google instead? :- http://.google.com/search?q='+re.sub(r' ', '+', text))

            return ""

        except wikipedia.exceptions.PageError as pe:
            Voice.speak('Sorry could not find any results')
            Wiki.color.alert('Sorry could not find any results')
            return ""

        except ValueError as e:
            Voice.speak('Something went wrong')
            Wiki.color.alert('Encountered ValueEror')
            return ""