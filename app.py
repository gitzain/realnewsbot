from bottle import route, run, template, debug,time

import sys
sys.path.insert(0, 'controller/')
from source import Source
from story import Story
from reporter import Reporter
from news import News


import threading



news = News()
reporter = Reporter()



def keep_checking_new_stories():
	t = threading.Timer(60.0, keep_checking_new_stories)
	t.start()
	get_latest_news()

t = threading.Timer(60.0, keep_checking_new_stories)
t.start() 

def get_latest_news():
	stories = reporter.get_stories(news)

	for story in stories:
		print story.get_title()
		news.add_story(story.get_title(),story.get_date(),story.get_category(),story.get_story(),story.get_sources())

get_latest_news()


@route('/')
def show_news():
    output = template('header')+template('display_news', news=news.get_stories())
    return output

#reloader=True, 
run(host='0.0.0.0', port=8081, debug=True)