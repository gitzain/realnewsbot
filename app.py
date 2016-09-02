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



def hello():
	t = threading.Timer(10.0, hello)
	t.start()
	get_latest_news_test()

t = threading.Timer(10.0, hello)
t.start() 

def get_latest_news_test(story_number=0):
	news.add_story("Threaded story " + str(story_number) ,time.strftime("%d/%m/%y %H:%M:%S"),"","random story text",[])
	story_number += 1







def get_latest_news():
	stories = reporter.get_stories(news)

	for story in stories:
		news.add_story(story.get_title(),story.get_date(),story.get_category(),story.get_story(),story.get_sources())

get_latest_news()


@route('/')
def show_news():
    output = template('header')+template('display_news', news=news.get_stories())
    return output

#reloader=True, 
run(host='0.0.0.0', port=8080, debug=True)