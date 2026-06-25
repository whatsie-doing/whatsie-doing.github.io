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
# Bambu spools are ~230g empty. 
# Override per-filament for other brands.
FILAMENT_TARE_G = 250

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

#######
# Function to sort filaments by HSV
import colorsys
from itertools import groupby

def group_by_material_and_sort_by_hue(filament_list):
    def get_color_sort_key(item):
        hex_val = item.get('hex', '000000')
        hex_str = str(hex_val).lstrip('#')
        try:
            r, g, b = tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
            h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
            
            # Check for neutral/achromatic colors (Black, White, Gray)
            # Thresholds can be adjusted if a very faint tint is getting misclassified
            if s < 0.15 or v < 0.15:
                # Group number 1: Neutrals (sorted by brightness/value)
                # We use a tuple (group_id, sort_value)
                return (1, v) 
            else:
                # Group number 0: Vibrant colors (sorted by Hue rainbow order)
                return (0, h)
                
        except (ValueError, IndexError):
            return (1, 0)  # Fallback for malformed hex strings (defaults to black)

    # Sort by material name string, then by our custom color tuple
    # Because (0, h) comes before (1, v), colors will always print before neutrals
    sorted_raw = sorted(
        filament_list, 
        key=lambda x: (x.get('material', 'Unknown'), get_color_sort_key(x))
    )

    # Group them by material for the nested Jinja loop
    grouped_data = []
    for material, group in groupby(sorted_raw, key=lambda x: x.get('material', 'Unknown')):
        grouped_data.append({
            'material': material,
            'items': list(group)
        })
        
    return grouped_data

JINJA_FILTERS = {
    'group_filaments': group_by_material_and_sort_by_hue
}

###########
# End filament function
