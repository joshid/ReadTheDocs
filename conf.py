# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "FlightClaim"
copyright = "2025 Jose N. Hidalgo"
author = "Jose N. Hidalgo"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# https://sphinx-collapse.readthedocs.io/en/latest/usage.html

extensions = [
    "sphinx_book_theme",
    "sphinx_collapse",
    "sphinx_togglebutton",
    # 'sphinx_rtd_dark_mode', # do NOT enable this for sphinx_book_theme
    "myst_parser",  # Added for Markdown support
]

# Only when sphinx_rtd_dark_mode is enabled
# default_dark_mode = True

# MyST parser configuration
myst_enable_extensions = [
    "colon_fence",
    "tasklist",
    "deflist",
    "fieldlist",
]

#
# templates_path = ['_templates']

exclude_patterns = [
    ".DS_Store",
    ".venv",
    "_build",
    "xchapters",
    "MORE",
    "README.md",
    "foo.txt",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_book_theme

html_theme_options = {
    # "default_mode": "dark"
}

html_theme_path = [sphinx_book_theme.get_html_theme_path()]

html_theme = "sphinx_book_theme"
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'

html_static_path = ["_static"]
