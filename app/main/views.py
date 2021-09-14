from flask import render_template
from . import main

from ..request import get_newsource, get_articles

# views


@main.route('/')
def index():
    '''
    view page function that returns the index page and its data
    '''
    # Getting news sources
    general_newsource = get_newsource('general')
    business_newsource = get_newsource('business')
    technology_newsource = get_newsource('technology')
    science_newsource = get_newsource('science')
    entertainment_newsource = get_newsource('entertainment')
    health_newsource = get_newsource('health')
    sports_newsource = get_newsource('sports')
    print(general_newsource)

    title = ' Home | Welcome to the World of news'
    # search_article = request.args.get('article_query')
    # if search_article:
    #     return redirect(url_for('main.search',article_name = search_article))
    # else:
    return render_template('index.html', title=title,
                           general=general_newsource,
                           business=business_newsource,
                           technology=technology_newsource,
                           science=science_newsource,
                           entertainment=entertainment_newsource,
                           health=health_newsource,
                           sports=sports_newsource
                           )


@main.route('/source/articles/<source_id>')
def article(source_id):
    '''
    View article page function that returns the article details page and its data
    '''
    articles = get_articles(source_id)
    print(articles)

    return render_template('article.html', articles=articles)
