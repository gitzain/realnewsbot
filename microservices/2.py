# Should group simular articles

from flask import Flask
from flask import request
import feedparser, json
import matplotlib
matplotlib.use('Agg')
import re
import feedparser
import nltk
import math
from operator import itemgetter
import operator
import numpy
from scipy.cluster.hierarchy import dendrogram, linkage
import pylab
import nltk
from flask_restplus import Resource, Api, fields, Namespace

app = Flask(__name__)


app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
api = Api(app, 
          version='1.0',
          title='Ditto API', 
          description='This API compares the texts given to it tells you which ones are similar.',
          default='ditto',
          default_label='Compares texts')


class NewsProcessor:
    def __init__(self):
        self.corpus = []
        self.titles = []        
        self.links = []
        self.ct = -1

        self.key_word_list = set()
        self.nkeywords = 4
        self.feature_vectors = []
        self.n = len(self.corpus)
        self.t = 0.8

    def freq(self, word, document):
        return document.count(word)

    def wordCount(self, document):
        return len(document)

    def numDocsContaining(self, word, documentList):
        count = 0
        for document in documentList:
            if self.freq(word, document) > 0:
                count += 1
        return count

    def tf(self, word, document):
        return self.freq(word, document) \
            / float(self.wordCount(document))

    def idf(self, word, documentList):
        return math.log(len(documentList)
                        / self.numDocsContaining(word, documentList))

    def tfidf(
        self,
        word,
        document,
        documentList,
        ):
        return self.tf(word, document) * self.idf(word, documentList)

    def top_keywords(
        self,
        n,
        doc,
        corpus,
        ):
        d = {}
        for word in set(doc):
            d[word] = self.tfidf(word, doc, corpus)
        sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1))
        sorted_d.reverse()
        return [w[0] for w in sorted_d[:n]]

    def extract_clusters(
        self,
        Z,
        threshold,
        n,
        ):
        clusters = {}
        ct = n
        for row in Z:
            if row[2] < threshold:
                n1 = int(row[0])
                n2 = int(row[1])

                if n1 >= n:
                    l1 = clusters[n1]
                    del clusters[n1]
                else:
                    l1 = [n1]

                if n2 >= n:
                    l2 = clusters[n2]
                    del clusters[n2]
                else:
                    l2 = [n2]
                    l1.extend(l2)
                    clusters[ct] = l1
                    ct += 1
            else:
                return clusters

    def do_it(self, sources):
        matplotlib.use('Agg')

        for source in sources:
            print "****************************************"
            print source.id
            print source.text
            words = nltk.wordpunct_tokenize(source.title)
            words.extend(nltk.wordpunct_tokenize(source.text))
            lowerwords = [x.lower() for x in words if len(x) > 1]
            self.ct += 1

                # print self.ct, "TITLE",source.headline

            self.links.append(source.id)
            self.corpus.append(lowerwords)



        [[self.key_word_list.add(x) for x in
         self.top_keywords(self.nkeywords, doc, self.corpus)]
         for doc in self.corpus]

        self.ct = -1
        for doc in self.corpus:
            self.ct += 1

               # print self.ct,"KEYWORDS"," ".join(self.top_keywords(self.nkeywords,doc,self.corpus))

        for document in self.corpus:
            vec = []
            [vec.append((self.tfidf(word, document,
             self.corpus) if word in document else 0)) for word in
             self.key_word_list]
            self.feature_vectors.append(vec)

        self.n = len(self.corpus)

        mat = numpy.empty((self.n, self.n))
        for i in xrange(0, self.n):
            for j in xrange(0, self.n):
                mat[i][j] = \
                    nltk.cluster.util.cosine_distance(self.feature_vectors[i],
                        self.feature_vectors[j])

        Z = linkage(mat, 'single')

        dendrogram(Z, color_threshold=self.t)

        clusters = self.extract_clusters(Z, self.t, self.n)

        results = []
        for key in clusters:
            group = []
            for id in clusters[key]:
                group.append(self.links[id])
            results.append(group)
        return results



class Source:
    def __init__(self, id, title, text):
        self.id = id
        self.title = title
        self.text = text

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__)

def toJson(inputy):
    output = "{ \"similar_texts\": ["
    for item in inputy:
        print str(item)
        output += "{ \"similar\":" + json.dumps(item) + "},"
    if inputy:
        output = output[:-1]
    output += "]}"
    print output
    return output

def json_to_sources(sources_json):
    

    sources = []

    for item in sources_json['texts']:
        source = Source(item['id'],item['title'],item['text'])
        sources.append(source)

    return sources




###########################################################

text = api.model('Text', {
    'id': fields.String,
    'title': fields.String,
    'text': fields.String

})

texts = api.model('Texts', {
    'texts': fields.List(fields.Nested(text))
})

similar = api.model('SimilarTexts', {
    'similar': fields.List(fields.Nested(text))
})

similar_text = api.model('Result', {
    'similar_texts': fields.List(fields.Nested(similar))
})



@api.route('/compare')
class CompareAPI(Resource):
    @api.expect(texts)
    #@api.marshal_with(similar_text, code=201)
    def post(self):
        sources = json_to_sources(request.json)
        results = NewsProcessor().do_it(sources)
        print toJson(results)
        return toJson(results)

###########################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
