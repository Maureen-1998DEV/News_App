import unittest
from app.models import Article

Articles = article.Article


class ArticleTest(unittest.TestCase):
    '''
    Test class to test behaviour of Article class
    '''
    def setUp(self):
        '''
        method that will run before every Test
        '''
        self.new_article = Article('Test author','Test title','Test description','Test url','Test image','Test publishedAt')

    def test_instance(self):
            self.assertTrue(isinstance(self.new_article,Article))