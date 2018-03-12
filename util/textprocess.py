import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from packages.Gmap import Gmap
from packages.News import News
from packages.Mail import Mail
import speech_recognition as sr
from .Color import Color

#base exception
class Error(Exception):
   """Base class for other exceptions"""
   pass

#custom exception
class DidntUnderstandException(Error):
    pass

color = Color()

def listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        sr.SAMPLE_RATE = 48000
        audio = r.listen(source)
        print('listened')
        try:
            recog_speech = str(r.recognize_google(audio))
            return recog_speech

        except sr.UnknownValueError as e:
            color.alert("Sorry, I did not understand")
            raise DidntUnderstandException

        #if didnt understand give one more go
        except DidntUnderstandException as e:
            color.alert("Lets try again")
            Color.primary("lets try again..")
            
            
            with sr.Microphone() as source:
                sr.SAMPLE_RATE = 48000
                audio = r.listen(source)
            
            try:
                recog_speech = str(r.recognize_google(audio))
                return recog_speech

            except sr.UnknownValueError as e:
                color.alert('Sorry, I did not understand')
            except sr.RequestError as e:
                color.alert("There seems to be internet connection problem..")
                return ""
            except Exception as e:
                color.alert('Something bad happened')
                return ""

        except sr.RequestError as e:
            color.alert("There seems to be internet connection problem..")
            return ""
        except Exception as e:
            color.alert('Something bad happened')
            return ""


def textprocess(text):
    print('in textprocess')
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
        places = places[1].split('to')

        Gmap.open(places[0], places[1])
        return 'Heres the route from '+places[0]+' to '+places[1]

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
            return ""
        return "Done"