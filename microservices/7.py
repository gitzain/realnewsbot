# Manages stories

from flask import Flask
import requests 

import json, datetime
import jsonpickle
from flask_restplus import Resource, Api, fields, Namespace



app = Flask(__name__)

app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
api = Api(app, 
          version='1.0',
          title='News Manager API', 
          description='This API manages processing and access to news.',
          default='newsroom',
          default_label='Manages stories')



class Source:
	def __init__(self, url, publishedDate, title, description):
		self.url = url
		self.publishedDate = publishedDate
		self.title = title
		self.description = description

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__)

class Story:
    def __init__(self):
		Story.id_counter = 0
		self.id = Story.id_counter
		Story.id_counter = Story.id_counter + 1
		self.date = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
		self.headline = ""
		self.story = ""
		self.sources = []

    def update_story(self):
        string_to_summarise = ""
        for source in self.sources:
            string_to_summarise = string_to_summarise + " " + source.description
            print "**************** going to add this this the string to sent to summy"
            print source.description
        string_to_summarise = "{ \"text\":" + json.dumps(string_to_summarise) + "}"
        response = requests.post("http://0.0.0.0:5004/summarise", data=string_to_summarise, headers = {'Content-type': 'application/json'})
        response_json = json.loads(response.json())
        print  "*************************data from summary api"
        print response_json
        self.story = response_json['text']
        print  "*******************story summarised"
        print self.story
        

    def update_headline(self):
		string_to_summarise = ""
		for source in self.sources:
			string_to_summarise = string_to_summarise + " " + source.headline
		string_to_summarise = "{ \"text\":" + json.dumps(string_to_summarise) + "}"
		response = requests.post("http://0.0.0.0:5004/title", data=string_to_summarise, headers = {'Content-type': 'application/json'})
		response_json = json.loads(response.text)
		self.headline = response_json['summary']
		print  "*****"
		print self.headline

    def add_source(self, source):
        self.sources.append(source)
        self.update_story()
        self.headline = source.title

    def __str__(self):
        return "ID: " + str(self.id) + "Date: " + str(self.date) + "Headline: " + self.headline + "Story: " + self.story

    def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__)




class Newsroom:

    def index(self):
        # get sources
        response = requests.get('http://127.0.0.1:5001/sources')
        json_data_sources = json.loads(response.json())
        sources = {}
        for item in json_data_sources['articles']:
            source = Source(item['url'], item['publishedDate'],item['title'],item['description'])
            sources[item['url']] = source


        # group similar
        texts = {}
        text = []
        texts["texts"] = text
        for key, value in sources.iteritems():
            texty = {}
            texty["id"] = value.url
            texty['title'] = value.title
            texty["text"] = value.description
            text.append(texty)
        reqy = json.dumps(texts)
        print "data going to compare ********************"
        print reqy
        response = requests.post("http://0.0.0.0:5002/compare", data=reqy, headers = {'Content-type': 'application/json'})
        json_data_similar = json.loads(response.json())
        print "**************** response from ditto"
        print type(json_data_similar)



        # create story ojbects
        stories = []
        #print json_data_similar['similar_texts'][0]["similar"][1]
        for item in json_data_similar['similar_texts']:
            story = Story()
            for identification in item['similar']: 
                story.add_source(sources[identification])
            stories.append(story)
        # check stories works
        print "*************"

        output = "{ \"status\": \"ok\", \"articles\": ["
        for stry in stories:
            output += jsonpickle.encode(stry, unpicklable=False) + ","
        if stories:
            output = output[:-1]
        output += "]}"
        print output
        return output

    def remove_dot_key(obj):
        for key in obj.keys():
            new_key = key.replace("articles","texts")
            if new_key != key:
                obj[new_key] = obj[key]
                del obj[key]
        return obj

    def toJson(inputy):
        output = "{ \"status\": \"ok\", \"sources\": ["
        for item in inputy:
            output += item.toJSON() + ","
        if inputy:
            output = output[:-1]
        output += "]}"
        print output
        return output

###########################################################

@api.route('/stories/all')
class NewsroomAPI(Resource):
    source = api.model('Source', {
        'url': fields.String(description='URL to the story'),
        'publishedDate': fields.String(description='Date the story was published'),
        'title': fields.String(description='Title/headline to the story'),
        'description': fields.String(description='The story text'),

    })

    story = api.model('Story', {
        'id': fields.String,
        'date': fields.String,
        'headline': fields.String,
        'story': fields.String,
        'story': fields.List(fields.Nested(source)),

    })

    newspaper = api.model('Newspaper', {
        'status': fields.String,
        'stories': fields.List(fields.Nested(story)),

    })

    @api.response(200, 'Success', newspaper)
    def get(self):
        return Newsroom().index()

###########################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)
