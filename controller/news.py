import sqlite3
from datetime import datetime
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
			s = Story()
			s.set_unique_id(story[0])
			s.set_title(story[1])
			s.set_date(story[2])
			s.set_category(story[3])
			s.set_story(story[4])

			c.execute("SELECT id,source,url,headline,story FROM sources WHERE id=?", [story[0]])
			story_sources = c.fetchall()
			for source in story_sources:
				s.add_source(Source(source[1],source[2],source[3],source[4]))

			self.stories.insert(1, s)

		c.close()

	def get_stories(self):
		return self.stories

	def get_today_stories(self):
		filtered_sorted_stories = []

		for story in self.stories:
			print story.get_date()
			print datetime.today().date()
			
			if datetime.strptime(story.get_date(), "%d/%m/%y %H:%M:%S").date() == datetime.today().date():
				filtered_sorted_stories.insert(1, story)

		return filtered_sorted_stories

	def contains_url(self, url):
		for story in self.stories:
			if story.source_exists(url):
				return True

		return False

	def add_story(self, title, date, category, story, sources):
		db = sqlite3.connect('model/news.db')
		c = db.cursor()
		c.execute("insert into news (title,date,category,story) values (?,?,?,?)", (title,date,category,story))
		id = c.lastrowid
		for source in sources:
			c.execute("insert into sources (id,source,url,headline,story) values (?,?,?,?,?)", (id,source.name,source.url,source.headline,source.story))
		db.commit()
		c.close()

		story_instance = Story()
		story_instance.set_title(title)
		story_instance.set_date(date)
		story_instance.set_story(story)
		for source in sources:
			story_instance.add_source(source)
		self.stories.insert(1, story_instance)
