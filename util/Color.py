from colorama import init
from termcolor import colored

class Color:

    def __init__(self):
        init(autoreset=True)
    
    def colorize(self, text, color):
        coloredtext = colored(text, color)
        print(coloredtext)
    
    def primary(self, text):
        coloredtext = colored(text, 'magenta')
        print(coloredtext)
    
    def alert(self, text):
        coloredtext = colored(text, 'red')
        print(coloredtext)

    def info(self, text):
        coloredtext = colored(text, 'blue')
        print(coloredtext)
    
    def success(self, text):
        coloredtext = colored(text, 'green')
        print(coloredtext)