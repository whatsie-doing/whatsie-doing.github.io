AUTHOR = "What's His Face"
SITENAME = 'Whatsie Doing?'
SITEURL = ""

THEME = 'themes/newbird'

# Elegant specific tweaks for that clean Minima top-nav feel
# LANDING_PAGE_ABOUT = False
# PROJECTS = []

# Tells Elegant to use a classic linear blog stream layout on the homepage
# HOMEPAGE_ARTICLE_SUMMARY_SPLIT = True

# Forces the home feed to show actual written summaries/excerpts instead of a title archive list
SUMMARY_MAX_LENGTH = None

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Custom format overrides
CUSTOM_CSS = 'static/custom.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGINS = ['minchin.pelican.plugins.summary','pelican.plugins.yaml_metadata']

# Pelican Summary plugin overrides
SUMMARY_END_MARKER = '<!-- more -->'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.footnotes': {},
    },
    'output_format': 'html5',
}

STATIC_PATHS = ['images']

# Default empty-spool tare weight in grams.
# Bambu spools are ~230g empty. Override per-filament for other brands.
FILAMENT_TARE_G = 230

# Net weight below which a spool (with no spares) triggers a reorder warning.
FILAMENT_LOW_THRESHOLD_G = 200

# Net weight of a full spool of filament (not including spool weight).
FILAMENT_FULL_G = 1000


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
