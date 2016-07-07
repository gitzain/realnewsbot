import sqlite3
db = sqlite3.connect('news.db')
#db.execute("CREATE TABLE news (id INTEGER PRIMARY KEY, title TEXT NOT NULL, link TEXT NOT NULL, source TEXT NOT NULL)")
db.execute("INSERT INTO news (title,link,source) VALUES ('title2','http://test.com/linktostory2.html', 'Test Source 2')")
db.commit()