from app import app
import urllib.request,json
from .models import Source,Article

Source = Source
Article = Article

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the source url
source_url = ['NEWS_API_SOURCE']
#Getting the article url
article_url = ['NEWS_API_ARTICLE']

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = source_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results