import sys, arrow, time, dateutil

from uuid import uuid4

sys.path.insert(0, 'controller/')
from summarize import SummaryTool


class Story:
	def __init__(self):
		self.id = uuid4()
		self.title = ""
		self.date = time.strftime("%d/%m/%y %H:%M:%S")
		self.category = "Sport"
		self.story = ""
		self.sources = []

	def get_id(self):
		return self.id

	def set_id(self, id):
		self.id = id

	def get_title(self):
		try:
			if self.title is "":
				return self.sources[0].headline
			else:
				return self.title
		except:
			return str(len(sources))

	def set_title(self, title):
		self.title = title

	def get_date(self):
		return self.date

	def get_friendly_date(self):
		tz = 'Europe/London'
		arrow_date = arrow.get(self.date, 'DD/MM/YY HH:mm:ss').replace(tzinfo=dateutil.tz.gettz(tz))
		return arrow_date.humanize()

	def set_date(self, date):
		self.date = date

	def get_category(self):
		return self.category.lower()

	def set_category(self, category):
		self.category = category

	def get_story(self):
		if self.story is "":
			added_story = ""

			for source in self.sources:
				added_story += source.get_story()

			print "**********************original story*******************************"
			print added_story

			# Create a SummaryTool object
			st = SummaryTool()
			# Build the sentences dictionary
			sentences_dic = st.get_senteces_ranks(added_story)
			# Build the summary with the sentences dictionary
			summary = st.get_summary("", added_story, sentences_dic)

			print "**********************sumarised story*******************************"
			print summary

			return summary
		else:
			return self.story

	def set_story(self, story):
		self.story = story

	def get_sources(self):
		return self.sources

	def add_source(self, source):
		self.sources.append(source)

	def is_breaking(self):
		return False

	def source_exists(self, url):
		result = False

		for source in self.sources:
			if source.check_source(url):
				return True

		return result
