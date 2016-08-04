class Ingest:
  #########################################
  # define our feeds
  #########################################
  feeds = [
      'http://feeds.bbci.co.uk/news/rss.xml',
      'http://rss.cnn.com/rss/edition_world.rss',
      'http://news.yahoo.com/rss/',
      'http://feeds.news24.com/articles/News24/World/rss',
      'https://www.rt.com/rss/news/'
  ]

  def get_feeds:
    return feeds