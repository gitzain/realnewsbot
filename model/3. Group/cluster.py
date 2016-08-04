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
  #########################################
  # define our feeds
  #########################################
  feeds = [
      'http://feeds.bbci.co.uk/news/rss.xml',
      'http://rss.cnn.com/rss/edition_world.rss',
      'http://news.yahoo.com/rss/',
      'http://feeds.news24.com/articles/News24/World/rss',
      'https://www.rt.com/rss/news/'
  ]

  #########################################
  # parse the feeds into a set of words per document
  #########################################
  def clean_html(self,html):
      """
      Copied from NLTK package.
      Remove HTML markup from the given string.

      :param html: the HTML string to be cleaned
      :type html: str
      :rtype: str
      """

      # First we remove inline JavaScript/CSS:
      cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
      # Then we remove html comments. This has to be done before removing regular
      # tags since comments can contain '>' characters.
      cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
      # Next we can remove the remaining tags:
      cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
      # Finally, we deal with whitespace
      cleaned = re.sub(r"&nbsp;", " ", cleaned)
      cleaned = re.sub(r"  ", " ", cleaned)
      cleaned = re.sub(r"  ", " ", cleaned)
      return cleaned.strip()

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


  def do_it(self):

    for feed in self.feeds:
        d = feedparser.parse(feed)
        for e in d['entries']:
           words = nltk.wordpunct_tokenize(self.clean_html(e['description']))
           words.extend(nltk.wordpunct_tokenize(e['title']))
           lowerwords=[x.lower() for x in words if len(x) > 1]
           self.ct += 1
           print self.ct, "TITLE",e['title']
           self.corpus.append(lowerwords)
           self.titles.append(e['title'])
           self.links.append(e['link'])



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
     
    for key in clusters:
       print "============================================="  
       for id in clusters[key]:
           print id,self.titles[id]




test = NewsProcessor()
test.do_it()