# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RRIS Intelligence'
copyright = '2022, Rehabilitation Research Institute of Singapore (RRIS)'
author = 'KY'
release = '1.0'
version = '1.0'
language = 'en'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_copybutton', 'sphinx.ext.intersphinx']

templates_path = ['_templates']
exclude_patterns = []

source_parsers = {
    '.md': 'myst_parser.docutils_',
}

source_suffix = ['.rst', '.md']

intersphinx_mapping = {
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    't3doc': ('https://rris-doc-testing.readthedocs.io/en/latest/', None),
}

today_fmt = '%d %b %Y, %H:%M'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_favicon = 'Asset/ntu-icon.png'
html_style = 'css/my_theme.css'
