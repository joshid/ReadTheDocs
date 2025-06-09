# Installation

Install ReadTheDocs
```bash
python -m venv .venv
source .venv/bin/activate

pip install myst-parser
pip install sphinx sphinx-autobuild
pip install sphinx_rtd_theme
pip install sphinx-book-theme
pip install sphinx-collapse
pip install sphinx-copybutton
pip install sphinx-rtd-dark-mode
pip install sphinx-togglebutton

pip install -r requirements.txt
```

The software above is:
- sphinx: The core documentation generator
- sphinx-autobuild: Adds live-reload functionality for development
- sphinx_rtd_theme: The Read the Docs theme for Sphinx
- sphinx-collapse: Adds collapsible content sections
- sphinx-rtd-dark-mode: Adds dark mode support for the RTD theme
- sphinx-togglebutton: Adds toggle buttons for content sections
- sphinx-copybutton: Adds a "copy" button to code blocks 
- sphinx-book-theme: A modern, responsive Sphinx theme originally developed for Jupyter Book with features like collapsible navigation, light/dark mode toggle, mobile-responsive design, and strong support for Jupyter notebooks in documentation

# Generate site

Generate manually
```bash
make html
open _build/html/index.html
```

Watch the files and rebuild when you make changes
```bash
sphinx-autobuild . _build/html
open http://127.0.0.1:8000
```

# Creating a new project

*Do NOT do this on an existing project.*

To create a project from scratch run the following:
```bash
pip install sphinx sphinx-autobuild
sphinx-quickstart
```

# Reference
- https://pypi.org/project/sphinx-rtd-dark-mode/
- https://www.sphinx-doc.org/en/master/usage/quickstart.html
- [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
