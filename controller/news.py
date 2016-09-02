import sqlite3

import sys
sys.path.insert(0, '/')
from source import Source
from story import Story

class News:
	def __init__(self):
		self.stories = []
		self.load_stories()

	def load_stories(self):
		db = sqlite3.connect('model/news.db')
		c = db.cursor()
		c.execute("SELECT id,title,date,category,story FROM news")
		news_table = c.fetchall()
		for story in news_table:
			c.execute("SELECT id,source,url,headline,story FROM sources WHERE id=?", [story[0]])
			story_sources = c.fetchall()
			sources = []
			for source in story_sources:
				sources.append(Source(source[1],source[2],source[3],source[4]))
			s = Story()
			s.id = story[0]
			s.title = story[1]
			s.date = story[2]
			s.category = "Sport"
			s.story = story[4]
			s.sources = sources
			self.stories.append(s)
		c.close()

	def get_stories(self):
		return self.stories

	def contains_url(self, url):
		for story in self.stories:
			if story.source_exists(url):
				return True

		return False

	def add_story(self, title, date, category, story, sources):
		#db = sqlite3.connect('model/news.db')
		#c = db.cursor()
		#c.execute("insert into news (title,date,category,story) values (?,?,?,?)", (title,date,category,story))
		#id = c.lastrowid
		#for source in sources:
		#	c.execute("insert into sources (id,source,url,headline,story) values (?,?,?,?,?)", (id,source.name,source.url,source.headline,source.story))
		#db.commit()
		#c.close()

		story_instance = Story()
		story_instance.set_id(id)
		story_instance.set_title(title)
		story_instance.set_date(date)
		story_instance.set_story(story)
		for source in sources:
			story_instance.add_source(source)
		self.stories.append(story_instance)
