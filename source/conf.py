# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sistemas e Sinais'
copyright = '2023, Bernardo Barancelli Schwedersky'
author = 'Bernardo Barancelli Schwedersky'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
#html_theme = 'karma_sphinx_theme'
#html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']
html_title = 'Sistemas e Sinais'

extensions.append('sphinx_exec_code')
extensions.append('sphinx_togglebutton')
 
exec_code_source_folders = ['../my_src']

# Codigo para compilar - Ir para pasta do projeto C:\Users\obern\OneDrive\ProjetoSphinx\.venv\Scripts
# Ativar o venv - activate
# Compilar - sphinx-build -b html docs/source/ docs/build/html