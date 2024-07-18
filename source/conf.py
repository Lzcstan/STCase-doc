# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'STCase'
copyright = '2024, Zhengchao Luo'
author = 'Zhengchao Luo'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['nbsphinx']

templates_path = ['_templates']
exclude_patterns = ['.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'insipid'
html_static_path = ['_static']
html_sidebars = {
   '**': [
       # 'github-badge.html',  # Custom template, see _templates/
       'home.html',
       'globaltoc.html',
   ],
   'tutorial/index': [
       # 'github-badge.html',  # Custom template, see _templates/
       'home.html',
       'globaltoc.html',
   ],
}