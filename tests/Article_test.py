import unittest 
from app.models import Article  

class Article(unittest.TestCase):
    '''
    Test class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        Set up metod that run before every Test
        '''
        self.new_article = Article('Test author','Test title','Test description','Test url','Test image','Test publishedAt')

    def test_instance(self) :
        self.assertTrue(self.new_article,Article)  