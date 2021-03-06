import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey=409c0e6afcce4ba0b4749a6ea62c1ce3'
    NEWS_API_ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sourcesapiKey=409c0e6afcce4ba0b4749a6ea62c1ce3'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
    @staticmethod
    def init_app(app):
      pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
   