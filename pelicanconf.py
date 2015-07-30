#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marvin'
SITENAME = u'Marvin\'s Blog'

PATH = 'content'

TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = u'en'

#ARCHIVE_LIST=TrueLINKS = (('Pelican', 'http://getpelican.com/'),


#TEMPLATE_PAGES = {'blog.html': 'blog.html'}
#DEFAULT_PAGINATION = True
#PAGINATED_DIRECT_TEMPLATES = ('blog-index',)
#STATIC_PATHS = ['images', 'extra/CNAME']
DIRECT_TEMPLATES = ('about','categories', 'index','archives')
#POST_LIMIT = 6

ARTICLES_HOME_PAGE = 'index'

SUMMARY_MAX_LENGTH = 30


DEFAULT_DATE_FORMAT = ('%d/%b/%Y %a')
#ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"
# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Archives', 'http://scalaboy.top/archives.html'),)

# Social widget
#SOCIAL = (('twitter', 'http://twitter.com/ametaireau'),
#          ('lastfm', 'http://lastfm.com/user/akounet'),
#          ('github', 'http://github.com/ametaireau'),)
SOCIAL = (('weibo', 'http://weibo.com/p/1005051799756001'),
         ('github','https://github.com/mawentao007'),)

#DEFAULT_PAGINATION = 10

#TEMPLATE_PAGES = {'src/books.html': 'dest/books.html',
#                  'src/resume.html': 'dest/resume.html'}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#THEME = "./themes/flat"
THEME = "./themes/notmyidea"


PLUGIN_PATHS = ["tag_cloud", "./plugins/tag-cloud"]
PLUGINS = ["tag_cloud"]
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100





#TIMEZONE = 'Europe/Paris'

#DEFAULT_LANG = u'en'


# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget


DEFAULT_PAGINATION = 3



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
