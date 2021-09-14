import urllib.request
import json
from .models import Source, Article


# Getting api key
api_key = 'b5a552ecd1014284b4bf5cbc587790c4'
# Getting source url,article url
News_Source_url = None
article_url = None


def configure_request(app):
    global api_key, News_Source_url, article_url
    News_Source_url = app.config['NEWS_API_SOURCE_URL']
    article_url = app.config['NEWS_API_ARTICLE_URL']
    api_key = ['NEWS_API_KEY']


def get_newsource(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newsource_url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey=b5a552ecd1014284b4bf5cbc587790c4'.format(
        category)
    with urllib.request.urlopen(get_newsource_url) as url:
        get_newsource_data = url.read()
        get_newsource_response = json.loads(get_newsource_data)

        newsource_results = None

        if get_newsource_response['articles']:
            newsource_results_list = get_newsource_response['articles']
            newsource_results = process_articles(newsource_results_list)

    return newsource_results


def process_result(newsource_list):
    '''
    Function that processes the source result and transform them to a list of objects
    Args:
    source_list: A list of dictionaries that contain source details
    '''
    newsource_results = []
    for news_item in newsource_list:
        id = news_item.get('id')
        author = news_item.get('author')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')

        language = news_item.get('language')

        newsource_object = Source(
            id, author, description, url, urlToImage, language)
        newsource_results.append(newsource_object)
    return newsource_results


def get_articles(source_id, limit):
    '''
    Function that gets the json response to our url
    '''
    get_article_url = article_url.format(source_id, limit, api_key)
    print(get_article_url)

    with urllib.request.urlopen(get_article_url) as url:
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
        articles_object = Article(author, title, description, url, urlToImage, publishedAt)
        articles_results.append(articles_object)

    return articles_results
        
