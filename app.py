import sqlite3
import arrow
from bottle import route, run, template, debug

class Source:
	def __init__(self, name, url):
		self.name = name
		self.url = url



class Story:
	def __init__(self, id, title, date, category, story, sources):
		self.id = id
		self.title = title
		self.date = date
		self.category = category
		self.story = story
		self.sources = sources

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



class News:
	def __init__(self):
		global stories
		stories = []
		self.load_stories()

	def load_stories(self):
		db = sqlite3.connect('news.db')
		c = db.cursor()
		c.execute("SELECT id,title,date,category,story FROM news")
		news_table = c.fetchall()
		for story in news_table:
			c.execute("SELECT id,source,url FROM sources WHERE id=?", [story[0]])
			story_sources = c.fetchall()
			sources = []
			for source in story_sources:
				sources.append(Source(source[1],source[2]))
			stories.append(Story(story[0],story[1],story[2],story[3],story[4],sources))
		c.close()

	def get_stories(self):
		return stories

	def add_story(self, title, date, category, story, sources):
		db = sqlite3.connect('news.db')
		c = db.cursor()
		c.execute("insert into news (title,date,category,story) values (?,?,?,?)", (title,date,story))
		id = c.lastrowid
		for source in sources:
			c.execute("insert into sources (id,source,url) values (?,?,?)", (id,source.name,source.url))
		db.commit()
		c.close()
		story_instance = Story(id, title, date, category, story, sources)
		stories.append(story_instance)



news_factory = News()

@route('/')
def show_news():
    output = template('header')+template('display_news', news=news_factory.get_stories())
    return output

run(host='0.0.0.0', port=8080, reloader=True, debug=True)