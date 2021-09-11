from flask import render_template,request,redirect,url_for
from app import app
from ..request import get_newsource,get_articles,search_article

#views
@app.route('/')
def index():
    '''
    view page function that returns the index page and its data
    '''
    #Getting news sources
    general_newsource = get_newsource('general')
    business_newsource = get_newsource('business')
    technology_newsource = get_newsource('technology')
    science_newsource = get_newsource('science')
    entertainment_newsource = get_newsource('entertainment')
    health_sources = get_newsource('health')
    sports_newsource = get_newsource('sports')
    
    

    title = ' Home | Welcome to the World of news'
    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('main.search',article_name = search_article))
    else:    
      return render_template('index.html', title=title, general = general_newsource, technology = technology_newsource, entertainment = entertainment_newsource, sports = sports_newsource, business= business_newsource, science = science_newsource, health = health_sources)

@app.route('/article/<source>')
def article(source):

    '''
    View article page function that returns the article details page and its data
    '''
    articles = get_articles(source)
    return render_template('article.html',articles =articles) 


@app.route('/search/<article_name>')
def search (article_name):
    '''
    View function to display search 
    '''
    article_name_list = article_name.split("") 
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'Search results for{article_name}'
    return render_template('search.html',article = searched_articles) 
