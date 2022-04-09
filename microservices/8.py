# Should remove opinions only keeping facts

from flask import Flask, render_template
import requests 
import json
import tldextract
from ago import human
from datetime import datetime

app = Flask(__name__)

class Source:
	def __init__(self, id, date, headline, story):
		self.id = id
		self.date = date
		self.headline = headline
		self.story = story

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__)

	def get_source_name(self):
		ext = tldextract.extract(self.id)
		return ext.domain

class Story:
    def __init__(self):
		Story.id_counter = 0
		self.id = Story.id_counter
		Story.id_counter = Story.id_counter + 1
		self.date = ""
		self.headline = ""
		self.story = ""
		self.sources = []

    def get_friendly_datetime(self):
        return human(self.date, precision=1)

    def __str__(self):
        return "ID: " + str(self.id) + "Date: " + str(self.date) + "Headline: " + str(self.headline) + "Story: " + str(self.story)

@app.route('/', methods=['GET'])
def template_test():
    response = requests.get('http://127.0.0.1:5007/stories/all') 
    print response.text
    data = json.loads(response.json())
    print data
    stories = []
    for item in data['articles']:
        story = Story()
        story.id = item['id']
        story.date = datetime.strptime(item['date'], '%H:%M:%S %d-%m-%Y')
        story.headline = item['headline']
        story.story = item['story']
        for this_source in item['sources']:
            source = Source(this_source['url'], this_source['publishedDate'],this_source['title'], this_source['description'])
            print source.story
            story.sources.append(source)
        stories.append(story)
        print story
    return render_template('index.html', s=stories)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)
