import tldextract

class Source:
	def __init__(self, name, url, headline, story):
		self.name = tldextract.extract(url).domain
		self.url = url
		self.headline = headline
		self.story = story
		self.summary = story[:150]

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_story(self):
		return self.story

	def check_source(self, url):
		if url == self.url:
			return True
		else:
			return False