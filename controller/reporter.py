import newspaper, logging, tldextract
from newspaper import Article
import feedparser

import sys
sys.path.insert(0, '/')
from source import Source

class Reporter:
	def __init__(self):
		self.feeds = [
			'http://feeds.bbci.co.uk/news/rss.xml',
			'http://rss.cnn.com/rss/edition_world.rss',
			'https://www.rt.com/rss/news/'
			]

	def get_sources(self):
		# This bit of code gets links to the latest stories from the rrs feeds.
		links = []

		for feed in self.feeds:
			d = feedparser.parse(feed)
			for e in d['entries']:
				links.append(e['link'])

		# This bit of code parses the links we just got and creates Source objects.
		sources = []
		
		for url in links:
			article = Article(url)
			article.download()
			article.parse()
			#print "********************"
			#print url
			#print article.text
			domain_name = tldextract.extract(url).domain
			source = Source(domain_name,url,article.title,article.text)
			sources.append(source)

		return sources