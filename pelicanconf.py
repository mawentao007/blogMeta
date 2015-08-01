#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marvin'
SITENAME = u'Marvin\'s Blog'

PATH = 'content'

TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = u'en'

DIRECT_TEMPLATES = ('about','categories', 'index','archives')
#POST_LIMIT = 6

ARTICLES_HOME_PAGE = 'index'

SUMMARY_MAX_LENGTH = 10


DEFAULT_DATE_FORMAT = ('%d/%b/%Y %a')

# Blogroll
#LINKS = (('Archives', 'http://scalaboy.top/archives.html'),)

SOCIAL = (('weibo', 'http://weibo.com/p/1005051799756001'),
         ('github','https://github.com/mawentao007'),)



#THEME = "./themes/flat"
THEME = "./themes/notmyidea"


PLUGIN_PATHS = ["tag_cloud", "./plugins/tag-cloud"]
PLUGINS = ["tag_cloud"]
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100


DEFAULT_PAGINATION = 8

#直接将该目录下的文件拷贝到output目录
#注意路径是相对content目录的！
#STATIC_PATHS = "./images"
STATIC_PATHS = ['images',]

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

