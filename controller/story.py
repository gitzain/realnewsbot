import sys, arrow, time, dateutil

from uuid import uuid4

sys.path.insert(0, 'controller/')

#Import library essentials
from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer #We're choosing Lexrank, other algorithms are also built in


class Story:
	def __init__(self):
		self.id = uuid4()
		self.title = ""
		self.date = time.strftime("%d/%m/%y %H:%M:%S")
		self.category = ""
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
				added_story += " " + source.get_story()

			return self.get_summary(added_story)
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

	def get_summary(self, text):
		parser = PlaintextParser.from_string(text, Tokenizer("english"))
		summarizer = LexRankSummarizer()
		summary = summarizer(parser.document, 3) #Summarize the document with 5 sentences

		result = ""
		for sentence in summary:
			result += str(sentence)

		return result