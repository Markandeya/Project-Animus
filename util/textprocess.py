import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from packages.Gmap import Gmap
from packages.News import News
from packages.Mail import Mail
from packages.Calendar import Calendar
from packages.System import System
import speech_recognition as sr
from .Color import Color

color = Color()
'''
Textprocess must return text, if nothing then empty string

'''


def listen():
    r = sr.Recognizer()
    r.energy_threshold = 1000
    
    with sr.Microphone() as source:
        print('active mic')
        sr.SAMPLE_RATE = 48000
        audio = r.listen(source)
        print('listened')
        try:
            recog_speech = str(r.recognize_google(audio))
            return recog_speech

        except sr.UnknownValueError as e:
            color.alert("Sorry, I did not understand")
            return ""
        except sr.RequestError as e:
            color.alert("There seems to be internet connection problem..")
            return ""
        except Exception as e:
            color.alert('Something bad happened')
            return ""


def textprocess(text):
    #print('in textprocess')
    
    text = text.lower()
    
    '''
    #tokenizing and codefying the speech
    ps = PorterStemmer()
    stopwordset = set( stopwords.words('english') )
    morestopwords = ['please', 'Please']

    tokenizedwords = word_tokenize(text)
    
    #remove stopwords
    filteredsentence = [word for word in tokenizedwords if word not in stopwordset]

    stemmedwords = []
    #stemming
    for word in filteredsentence:
        stemmedwords.append(ps.stem(word))
    
    postagged = nltk.pos_tag(tokenizedwords)

    chunkGram = r(triple quotes)NounGroup: {<NN.?>+}(triple quotes)
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(postagged)
    print(chunked)
    '''
    #Map program
    
    if 'map of' in text:
        print('found map of command')
        place = text.split('of')
        place = place[1].lstrip()
        Gmap.open(place)
        return 'Heres the map of '+place
    elif 'map from' in text:
        print('found map from command')
        places = text.split('map from')
        places = places[1].split('to',1)
        print(places)
        Gmap.open(places[0], places[1])
        return 'Heres the route from '+places[0]+' to '+places[1]
    
    elif 'restaurant near me' in text or 'restaurants near me' in text:
        print('found map command')
        place = input('Enter your location')
        Gmap.restaurants(place)
        return "Here are some restaurants near you"

    #news program
        
    if 'top news' == text:
        print('topnews')
        return News.topnews()
    elif 'latest news' == text:
        print('latest news')
        return News.latestnews()
    elif 'trending news' == text:
        print('popular news')
        return News.popularnews()

    #email
    if 'send email' == text:
        print('What is the message?')
        msg = listen()
        color.info('You said :' + msg)
        color.primary('Whom do you want to send? type it out (type c to cancel)-')
        recipient = input()

        if recipient == 'c':
            print('Cancelled operation')
            return ""
        
        color.primary('What is the subject?')
        subject = listen()
        color.info('Subject:'+ subject + '\nMessage:' + msg)
        color.primary('Are you sure you want to send? (say yes)')

        bol = listen()
        if bol == 'yes':
            Mail.send_email(subject, msg)
        else:
            color.alert('Cancelled')
            return "cancel"
        return "Done"

    #Calendar
    if 'create event' == text:
        print('Say the event description?')
        eventdesc = listen()
        color.info('You said :' + eventdesc)
        
        color.primary('What is the title?')
        title = listen()
        color.info('You said :' + title)

        color.primary('Please tell the date and time (like eg: April 27 1997)?')
        timedate = listen()
        color.info('You said :' + timedate)

        color.info('Title:'+ title + '\nDescription:' + eventdesc + '\nDate:' + timedate)
        color.primary('Are you sure you want to send? (say yes)')

        bol = listen()
        if bol == 'yes':
            Calendar.create_event(title, eventdesc, timedate)
        else:
            color.alert('Cancelled')
            return "cancel"
        return "Done"
    elif 'get event' == text or 'get events' == text :
        Calendar.get_events()
        return "Done"

    #Launch application
    if 'launch' == text:
        print('Say the appname')
        appname = listen().lower()
        System.launchapp(appname)
        return "Done"

    #Set brightness
    if 'set brightness as' in text:
        string = text.split('as')
        try:
            string = string[1].lstrip()
        except Exception as e:
            return "cancel"
        if string != "":
            value = int(string)
            System.change_brightness(value)
        else:
            print("Please say a value")
        return "Done"

    #Set volume
    if 'set volume as' in text:
        string = text.split('as')
        try:
            string = string[1].lstrip()
        except Exception as e:
            return "cancel"
        value = int(string)
        System.set_sound(value)
        return "Done"
    
    #Shutdown
    if 'shutdown' == text:
        System.shutdown()
    
    if 'restart' == text:
        System.restart() 
        