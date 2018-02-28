from colorama import init
from termcolor import colored

'''
{!! Support not included for all the features of termcolor !!}

Text colors: grey,red,green,yellow,blue,magenta,cyan,white

Text highlights: on_grey,on_red,on_green,on_yellow,on_blue,on_magenta,on_cyan,on_white

Attributes: bold,dark,underline,blink,reverse,concealed

'''
class Color:

    def __init__(self):
        init(autoreset=True)
    
    def colorize(self, text, color):
        coloredtext = colored(text, color)
        print(coloredtext)