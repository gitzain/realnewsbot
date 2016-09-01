from bottle import route, run, template, debug

import sys
sys.path.insert(0, 'controller/')
from summarize import SummaryTool
from source import Source
from story import Story
from reporter import Reporter
from news import News


news = News()

reporter = Reporter()
stories = reporter.get_stories(news)

for story in stories:
	news.add_story(story.get_title(),story.get_date(),story.get_category(),story.get_story(),story.get_sources())

@route('/')
def show_news():
    output = template('header')+template('display_news', news=news.get_stories())
    return output

#reloader=True, 
run(host='0.0.0.0', port=8080, debug=True)