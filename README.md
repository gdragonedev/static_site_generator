# Static Site Generator
This tool will convert any provided markdown files, and accompanying content into a static site. It will mirror the source file(s) structure for the output, and serve it locally.

## Goals
This tool is meant to be able to quickly convert any markdown content to HTML. While it works well as a standalone concept. I plan to modify this in the future to take my notes/recipes from Obsidian, as markdown, and update/add entries on my personal website. This way I can easily share them with friends and family, while keeping my recipies up to date when I make changes!

## Quick Start

### Update the file paths in main.py with content to be genereated into HTML, run 'main.sh', and view the site locally in your browser!

## Usage

### 1. Update the file paths in main.py as follows:
- dir_path_static: local directory containing static content to be used on the site like images, and CSS files.
- dir_path_public: local directory where final generated content will be placed (this dir will be wiped/created upon running each time).
- dir_path_content: local directory containing the markdown files, and structure to be converted.
- template_path: the .html template that will be used to build the markdown files

### 2. From the root of the project run:

```
./main.sh
```

### 3. View the site locally:

```
http://localhost:8888/
```

## Contributing

### Clone the repo

```
git clone https://github.com/gdragonedev/static_site_generator@latest
cd static_site_generator
```
### Add your own content to generate; see Usage above for instructions.
Test content has been included if you wish to use that!

### Run the tool

```
./main.sh
```

### Run the tests

```
./test.sh
```

### View Generated Site

```
http://localhost:8888/
```
