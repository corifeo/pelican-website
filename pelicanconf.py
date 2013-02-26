# -*- coding: utf-8 -*-
AUTHOR = u'Francesco Manzoni'
SITENAME = u'francescomanzoni.com'
SUBTITLE = u'Security, coding, reasonably priced love and a hard-boiled egg'
TIMEZONE = 'Europe/Rome'

THEME = 'octopussy'
THEME_STATIC_PATHS = (['static'])
DIRECT_TEMPLATES = (('index', 'categories', 'archives'))
# Move upload and static files to output directory
STATIC_PATHS = (['uploads'])
FILES_TO_COPY = (
	('extra/robots.txt', 'robots.txt'),
	('extra/0x49ABF9BF.asc', 'static/0x49ABF9BF.asc'),
	('extra/htaccess', '.htaccess'))


RELATIVE_URLS = False

DEFAULT_PAGINATION = 5
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'blog'
DEFAULT_LANG = u'en'

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_LANG_URL = '{category}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{category}/{slug}-{lang}.html'
CATEGORY_URL = '{slug}.html'
CATEGORY_SAVE_AS = '{slug}.html'

# It's a single user blog, dont need author pages
AUTHOR_URL = False
AUTHOR_SAVE_AS = False

FEED_RSS = 'feeds/all.rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
                                             

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/corifeo'),
         ('github', 'http://github.com/corifeo'),)

PLUGINS = ['pelican.plugins.pelican-gist']
