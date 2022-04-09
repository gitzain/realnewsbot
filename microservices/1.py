# Collects and returns news articles

import feedparser
import json
import re
from flask import Flask
from flask_restplus import Resource, Api, fields
import newspaper
from newspaper import Article

app = Flask(__name__)
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
api = Api(app, 
          version='1.0',
          title='Reporter API', 
          description='This API returns articles from news outlets.',
          default='reporter',
          default_label='Access to news stories')

FEEDS = ['http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk',
         'http://www.france24.com/en/top-stories/rss',
         'https://www.aljazeera.com/xml/rss/all.xml']

# Main class that gets stories given a list of rss feeds.
class Reporter:

    # Nested class that represents a source
    class Article:
	    def __init__(self, url, publishedDate, title, description):
	    	self.url = url
	    	self.publishedDate = publishedDate
	    	self.title = title
	    	self.description = description

	    def toJSON(self):
	    	return json.dumps(self, default=lambda o: o.__dict__)

    # Collects and returns news articles
    def get_articles(self, rss_feeds):

        articles = []

        for feed in rss_feeds:
            items = feedparser.parse(feed)
            for item in items['entries']:
                #article = Article(url)
                #article.download()
                #article.parse()
                #article.text
                article = self.Article(item['link'], "",item['title'],self.remove_html_tags(item['description']))
                articles.append(article)
   
        return articles

    def articles_to_json(self, articles):
        output = "{ \"status\": \"ok\", \"articles\": ["
        for article in articles:
            output += article.toJSON() + ","
        output = output[:-1]
        output += "]}"
        return output

    def get_stories(self):
        json_output = self.articles_to_json(self.get_articles(FEEDS))
        return json_output

    def remove_html_tags(self, text):
        tag_re = re.compile(r'<[^>]+>')
        return tag_re.sub('', text)

###########################################################

article = api.model('Article', {
    'url': fields.String(description='URL to the story'),
    'publishedDate': fields.String(description='Date the story was published'),
    'title': fields.String(description='Title/headline to the story'),
    'description': fields.String(description='The story text'),

})

articles = api.model('Articles', {
    'status': fields.String,
    'articles': fields.List(fields.Nested(article))
})

@api.route('/sources')
class ReporterAPI(Resource):
    @api.response(200, 'Success', articles)
    def get(self):
        return Reporter().get_stories()

###########################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
