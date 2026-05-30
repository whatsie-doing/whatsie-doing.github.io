AUTHOR = "What's His Face"
SITENAME = 'Whatsie Doing?'
SITEURL = ""

THEME = 'themes/newbird'

# Elegant specific tweaks for that clean Minima top-nav feel
LANDING_PAGE_ABOUT = False
PROJECTS = []

# Tells Elegant to use a classic linear blog stream layout on the homepage
HOMEPAGE_ARTICLE_SUMMARY_SPLIT = True

# Forces the home feed to show actual written summaries/excerpts instead of a title archive list
SUMMARY_MAX_LENGTH = 50

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.footnotes': {},
    },
    'output_format': 'html5',
}



# Blogroll
LINKS = [
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
]

# Social widget
# SOCIAL = [
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# ]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
