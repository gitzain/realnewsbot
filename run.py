import newspaper, logging, tldextract
from newspaper import Article
import feedparser
logging.basicConfig()
from uuid import uuid4


class Source:
	def __init__(self, name, url, headline, story):
		self.name = name
		self.url = url
		self.headline = headline
		self.story = story
		self.summary = story[:150]

class Story:
	def __init__(self):
		self.id = uuid4()
		self.title = ""
		self.date = "26/08/2016"
		self.story = ""
		self.sources = []

	def get_title(self):
		return self.title

	def get_date(self):
		return self.date

	def get_friendly_date(self):
		arrow_date = arrow.get(self.date, 'DD/MM/YY HH:mm:ss')
		return arrow_date.humanize()

	def get_category(self):
		return self.category.lower()

	def get_story(self):
		return self.story

	def get_sources(self):
		return self.sources

	def add_source(self, source):
		sources.append(source)

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
			domain_name = tldextract.extract(url).domain
			source = Source(domain_name,url,article.title,article.text)
			sources.append(source)
			print source.url

		return sources

	def get_stories(self):
		return



import re
import feedparser
import nltk
import math
from operator import itemgetter
import operator
import numpy
from hcluster import linkage, dendrogram
import pylab

class NewsProcessor:
	def __init__(self):
		self.corpus = []
		self.titles=[]
		self.links=[]
		self.ct = -1

		self.key_word_list=set()
		self.nkeywords=4
		self.feature_vectors=[]
		self.n=len(self.corpus)
		self.t = 0.8

	def freq(self,word, document): return document.count(word)
	def wordCount(self,document): return len(document)
	def numDocsContaining(self,word,documentList):
		count = 0
		for document in documentList:
			if self.freq(word,document) > 0:
				count += 1
		return count

	def tf(self,word, document): return (self.freq(word,document) / float(self.wordCount(document)))
	def idf(self,word, documentList): return math.log(len(documentList) / self.numDocsContaining(word,documentList))
	def tfidf(self,word, document, documentList): return (self.tf(word,document) * self.idf(word,documentList))

	def top_keywords(self,n,doc,corpus):
		d = {}
		for word in set(doc):
			d[word] = self.tfidf(word,doc,corpus)
		sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1))
		sorted_d.reverse()
		return [w[0] for w in sorted_d[:n]]   

	def extract_clusters(self,Z,threshold,n):
		clusters={}
		ct=n
		for row in Z:
			if row[2] < threshold:
				n1=int(row[0])
				n2=int(row[1])

				if n1 >= n:
					l1=clusters[n1] 
					del(clusters[n1]) 
				else:
					l1= [n1]

				if n2 >= n:
					l2=clusters[n2] 
					del(clusters[n2]) 
				else:
					l2= [n2]    
					l1.extend(l2)  
					clusters[ct] = l1
					ct += 1
			else:
				return clusters


	def do_it(self, sources):

		for source in sources:
			words = nltk.wordpunct_tokenize(source.headline)
			words.extend(nltk.wordpunct_tokenize(source.summary))
			lowerwords=[x.lower() for x in words if len(x) > 1]
			self.ct += 1
			print self.ct, "TITLE",source.headline
			self.corpus.append(lowerwords)
			self.titles.append(source.headline)
			self.links.append(source.url)



		[[self.key_word_list.add(x) for x in self.top_keywords(self.nkeywords,doc,self.corpus)] for doc in self.corpus]

		self.ct=-1
		for doc in self.corpus:
		   self.ct+=1
		   print self.ct,"KEYWORDS"," ".join(self.top_keywords(self.nkeywords,doc,self.corpus))



		for document in self.corpus:
			vec=[]
			[vec.append(self.tfidf(word, document, self.corpus) if word in document else 0) for word in self.key_word_list]
			self.feature_vectors.append(vec)



		self.n=len(self.corpus)

		mat = numpy.empty((self.n, self.n))
		for i in xrange(0,self.n):
		  for j in xrange(0,self.n):
			mat[i][j] = nltk.cluster.util.cosine_distance(self.feature_vectors[i],self.feature_vectors[j])


		Z = linkage(mat, 'single')

		dendrogram(Z, color_threshold=self.t)





		clusters = self.extract_clusters(Z,self.t,self.n)
		
		stories = []

		for key in clusters:
			print "============================================="
			story = Story()  
			for id in clusters[key]:
				story.add_source(sources[id])
				print id,self.titles[id],sources[id].url
			stories.append(story)


		return stories



reporter = Reporter()
sources = reporter.get_sources()

np = NewsProcessor()
stories = np.do_it(sources)

for story in stories:
	print "we got a story"
	print story
	print "*********=====================**********"

#for source in sources:
#	print source.story
#	print "**************"



#test = NewsProcessor()
#test.do_it()