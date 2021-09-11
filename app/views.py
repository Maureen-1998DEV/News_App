from flask import render_template
from app import app
#views
@app.route('/')
def index():
    '''
    view page function that returns the index page and its data
    '''
    #Getting source
    source = 'helloworld'
    return render_template('index.html', source = source)

@app.route('/article/<int:article_id>')
def article(article_id):

    '''
    View movie page function that returns the article details page and its data
    '''
    return render_template('article.html',id = article_id)  