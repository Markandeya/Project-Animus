import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from packages.Gmap import Gmap
from packages.News import News

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
        
    if 'top news' in text:
        print('topnews')
        return News.topnews()
    elif 'latest news' in text:
        print('latest news')
        return News.latestnews()
    elif 'trending news' in text:
        print('popular news')
        return News.popularnews()