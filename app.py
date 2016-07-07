import sqlite3
from bottle import route, run, template

def add_news(title, link, source):
	db = sqlite3.connect('news.db')
	c = db.cursor()
	c.execute("insert into news (title,link,source) values (?,?,?)", (title,link,source))
	db.commit()
	c.close()

@route('/news')
def show_news():
    db = sqlite3.connect('news.db')
    c = db.cursor()
    c.execute("SELECT title,link,source FROM news")
    data = c.fetchall()
    c.close()
    output = template('display_news', rows=data)
    return output

@route('/add/<title>')
def addy_news(title):
	add_news(title,"http","what")
	return show_news()

run(host='0.0.0.0', port=8080)

