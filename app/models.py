class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,description,category,language):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.language = language

class Article:
    '''
    Article class to define Articles Objects
    '''

    def __init__(self,author,title,description,url,urlToimage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToimage = urlToimage
        self.publishedAt = publishedAt