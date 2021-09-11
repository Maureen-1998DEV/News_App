class Article:
    '''
    Articles class to define Articles Objects
    '''

    def __init__(self,author,title,description,url,image,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.publishedAt = publishedAt