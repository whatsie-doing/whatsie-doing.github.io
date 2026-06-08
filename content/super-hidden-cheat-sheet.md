Title: Ultimate Pelican & Git Cheat Sheet
Date: 2026-05-30 12:50
Category: Reference
Slug: my-posting-cheat-sheet
Status: hidden

This page is cobbled together from a few poorly-attributed (by me) places so I can try to keep track of this stuff. 

<!-- more -->

And, yes, to my shame some of it did come via Google's AI suggestions. 

---

# Git Branching & Deployment Workflow

Because this is a personal github.io page, the repository splits raw source code from live HTML using branches. Never write code or posts on the main branch.

## 1. Daily Writing Setup
For the love of all that's holy, I hope someday I can remember this without looking it up. Today is not that day. 
```zsh
source .venv/bin/activate
```
And to deactivate it, a simple... 
```zsh
deactivate
```

Before editing or adding posts, verify you are working on the source branch:
```zsh
git checkout source
```

## 2. New Post

### Pelican Post Header Template

Every new .md file created inside the content/ folder must start with this text metadata block at the very top. Note that Pelican does NOT use triple dashes.

```md
Title: Your Post Title Here
Date: 2026-05-30 12:00
Category: Tech
Slug: your-post-slug-for-the-url
Status: hidden  *(Optional: Remove this line to make the post public)*

Post content starts here...
```

### Core Metadata Fields:
* `Title: `The display name of your article.
* `Date: `Formatted as YYYY-MM-DD HH:MM.
* `Category: `Organizes your post into site sections.
* `Slug: `Controls the URL string (e.g., slug: my-post becomes my-post.html).
* `Status: `Set to hidden to restrict access to direct URL links only (excludes it from the homepage index and pagination).

###
Somewhere, I found a nifty little addtion to `.zshrc` that'll help with a new post. 
```zsh
# Pelican Post Generator Alias
newpost() {
    # If you forget to provide a filename, it defaults to 'new-post'
    local filename="${1:-new-post}"
    
    # 1. Standardize the name into clean URL-safe slugs (lowercase, replacing spaces with dashes)
    local slug=$(echo "$filename" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
    
    # 2. Copy your template directly to the content folder
    cp template.md "content/${slug}.md"
    
    # 3. Automatically inject the exact current date/time into the header
    sed -i '' "s/Date:.*/Date: $(date '+%Y-%m-%d %H:%M')/" "content/${slug}.md"
    
    # 4. Open the file immediately so you can start writing
    nano "content/${slug}.md"
}
```
When I type `newpost "New Title Goes Here"` it will copy my template to the `/content` folder so I don't have to remember my header tags each time. 

## 3. Local testing
While testing format changes, it's handy to keep the http server running locally.

```python
python -m http.server 8000 --directory output 
```
I prefer this over `pelican --listen output` because I can check the mobile interface from my phone at the same time. 

Every time I save some tweak or another, I run the following
```zsh
rm -rf output/* && rm -rf cache/* && pelican content -s pelicanconf.py
```
It feels entirely likely that something about this is overkill, but it's the steps I started with so it's the steps I continue with. 

## 4. Save, Compile, and Publish Live
When it's time to be done tweaking things and just commit for once:
```zsh
git add .
git commit -m "Bug Fixes and Performance Improvements"
git push origin source
```

---

## Markdown Syntax Reference

```md
# H1 Header
## H2 Header
### H3 Header

### Text Styles
*This text will be italic*
**This text will be bold**
~~This text will have a strikethrough~~

### Lists
* Unordered list item 1
* Unordered list item 2
    * Indent 4 spaces for a sub-item

1. Ordered list item 1
2. Ordered list item 2

### Links and Images
[Clickable Text Link](https://my.domain)  
![Image Alt Text](https://via.placeholder.com/150)

### Code Blocks
To display inline code within a sentence, wrap it in single backticks: `print("Hello World")`.

To display a multi-line block of code, wrap it in triple backticks and specify the programming language for syntax highlighting.
```
