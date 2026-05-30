Title: Ultimate Pelican & Git Cheat Sheet
Date: 2026-05-30 12:50
Category: Reference
Slug: my-posting-cheat-sheet
Status: hidden

# Ultimate Pelican & Git Cheat Sheet

This hidden page serves as the master reference guide for managing, writing, and publishing to this blog.

---

## Clean Directory Structure
Your Pelican blog directory should look exactly like this. All old Jekyll remnants have been removed:

your-repo-name/
├── .github/
│   └── workflows/
│       └── pelican.yml      # Automated deployment instructions
├── content/
│   ├── CNAME                # Contains only: my.domain
│   ├── .nojekyll            # Tells GitHub to bypass Jekyll
│   └── markdown-cheat-sheet.md
├── pelicanconf.py           # Local settings (SITEURL = '')
├── publishconf.py           # Live settings (SITEURL = 'https://my.domain')
└── requirements.txt         # Lists python dependencies (pelican, markdown)

---

## Git Branching & Deployment Workflow

Because this is a personal github.io page, the repository splits raw source code from live HTML using branches. Never write code or posts on the main branch.

### 1. Daily Writing Setup
Before editing or adding posts, verify you are working on the source branch:
git checkout source

### 2. Save, Compile, and Publish Live
When you are ready to push your changes to your custom domain, run these three commands in order from your root folder:
git add .
git commit -m "Update blog content and reference sheets"
git push origin source

---

## Pelican Post Header Template

Every new .md file created inside the content/ folder must start with this text metadata block at the very top. Note that Pelican does NOT use triple dashes.

Title: Your Post Title Here
Date: 2026-05-30 12:00
Category: Tech
Slug: your-post-slug-for-the-url
Status: hidden  *(Optional: Remove this line to make the post public)*

Your content starts here...

### Core Metadata Fields:
* Title: The display name of your article.
* Date: Formatted as YYYY-MM-DD HH:MM.
* Category: Organizes your post into site sections.
* Slug: Controls the URL string (e.g., slug: my-post becomes my-post.html).
* Status: Set to hidden to restrict access to direct URL links only (excludes it from the homepage index and pagination).

---

## Markdown Syntax Reference

### Headers
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
