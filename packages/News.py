import newsapi.articles
from util.Voice import Voice

class News:
    articles = newsapi.articles.Articles(API_KEY="397a0021f4924b7a80ba8d4a04d86713")

    @staticmethod
    def topnews():
        Voice.speak('Heres the top news for you')
        news = News.articles.get_by_top('the-times-of-india')
        articles = news.articles

        for art in articles:
            print('-----------------------')	
            print(art['title'])
            print(art['description'])
            print('Read more at -', art['url'])

        return "Heres the top news for you"

    @staticmethod
    def popularnews():
        Voice.speak('Here are some popular news for you')
        news = News.articles.get_by_popular('the-times-of-india')
        articles = news.articles

        for art in articles:
            print('-----------------------')	
            print(art['title'])
            print(art['description'])
            print('Read more at -', art['url'])

        return "Here are some popular news for you"

    @staticmethod
    def latestnews():
        Voice.speak('These are some latest news for you')
        news = News.articles.get_by_latest('the-times-of-india')
        articles = news.articles

        for art in articles:
            print('-----------------------')	
            print(art['title'])
            print(art['description'])
            print('Read more at -', art['url'])

        return "These are some latest news for you"
