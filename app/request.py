from app import app
import urllib.request,json
from .models import Source,Article
from datetime import datetime
Source = Source

Article = Article
api_key = '409c0e6afcce4ba0b4749a6ea62c1ce3'
News_Source_url = None
articles_url = None

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the source url
base_url = app.config['NEWS_API_SOURCE']
#Getting the article url
article_url = app.config['NEWS_API_ARTICLE']

def get_newsource(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newsource_url = base_url.format(category,api_key)
    print(get_newsource_url)

    with urllib.request.urlopen(get_newsource_url) as url:
        get_newsource_data = url.read()
        get_newsource_response = json.loads(get_newsource_data)

        newsource_results = None

        if get_newsource_response['results']:
            news_results_list = get_newsource_response['results']
            news_results = process_results(news_results_list)


    return newsource_results

def process_results(newsource_list):
    '''
    Function that processes the source result and transform them to a list of objects
    Args:
    source_list: A list of dictionaries that contain source details
    '''
    newsource_results = []
    for news_item in newsource_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        category = news_item.get('category')
        language = news_item.get('language')

        newsource_object = Source(id,name,description,category,language)
        newsource_results.append(newsource_object)
        return newsource_results
def get_articles(source_id,limit):
    '''
    Function that gets the json response to our url
    '''
    get_articles_url = article_url.format(source_id,limit,api_key)
    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    '''
    Function  that processes the new articles and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain article details
    Returns :
        articles_results: A list of article objects
    '''
    articles_results = []
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        publishedAt = datetime(year=int(publishedAt[0:4]),month=int(publishedAt[5:7]),day=int(publishedAt[8:10]),hour=int(publishedAt[11:13]),minute=int(publishedAt[14:16]))

        if urlToImage:
            articles_object = Article(author, title, description, url, urlToImage, publishedAt)
            articles_results.append(articles_object)

    return articles_results
        
