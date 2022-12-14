# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RRIS Intelligent Robotics'
copyright = '2023, Rehabilitation Research Institute of Singapore (RRIS)'
author = 'KY'
release = '1.0'
version = '1.0'
language = 'en'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 
              'sphinx_copybutton', 
              'sphinx.ext.intersphinx', 
              'sphinx_tabs.tabs', 
              'sphinxcontrib.youtube',
              'sphinx_design',
              'sphinx_substitution_extensions']

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

rst_prolog = """
.. |rris_copyright| replace:: Copyright 2023, Rehabilitation Research Institute of Singapore (RRIS)
.. |rris_license|   replace:: Proprietary, Rehabilitation Research Institute of Singapore (RRIS)
.. |rris_kuanyuee|  replace:: :ref:`Kuan Yuee <rris_staff_kuanyuee>`
.. |rris_janne|     replace:: :ref:`J-Anne <rris_staff_janne>`
.. |rris_lilei|     replace:: :ref:`Li Lei <rris_staff_lilei>`
.. |rris_marcus|    replace:: :ref:`Marcus <rris_staff_marcusleong>`
.. |rris_chinxian|  replace:: :ref:`Chin Xian <rris_staff_chinxian>`
.. |rris_weeching|  replace:: :ref:`Wee Ching <rris_staff_weeching>`
.. |rris_bangyi|    replace:: :ref:`Bang Yi <rris_staff_bangyi>`
.. |lang_cpp|       replace:: :bdg-secondary:`C++`
.. |lang_py3|       replace:: :bdg-secondary:`Python3`
.. |lang_js|        replace:: :bdg-secondary:`JavaScript`
.. |lang_css|       replace:: :bdg-secondary:`CSS`
.. |lang_html|      replace:: :bdg-secondary:`HTML`
.. |ros_melodic|    replace:: :bdg-primary:`ROS1` :bdg-primary-line:`melodic`
.. |ros_noetic|     replace:: :bdg-primary:`ROS1` :bdg-primary-line:`noetic`
.. |ros_foxy|       replace:: :bdg-info:`ROS2` :bdg-info-line:`foxy`
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_favicon = 'Asset/ntu-icon.png'
html_style = 'css/my_theme.css'
html_show_sourcelink = False
