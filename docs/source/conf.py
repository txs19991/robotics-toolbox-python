# spatialmath
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'Robotics Toolbox Python'
copyright = '2020, Jesse Haviland and Peter Corke'
author = 'Jesse Haviland and Peter Corke'

print(__file__)
# The full version, including alpha/beta/rc tags
with open('../../RELEASE', encoding='utf-8') as f:
    release = f.read()

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.inheritance_diagram',
    'sphinx_autorun',
    ]
    #'recommonmark',
    #'sphinx.ext.autosummary',
    #     'sphinx_markdown_tables',  


autosummary_generate = True
autodoc_member_order = 'bysource'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['test_*']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
'github_user': 'petercorke',
    #'github_repo': 'spatialmath-python',
    #'logo_name': False,
    'logo_only': False,
    #'description': 'Spatial maths and geometry for Python',
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'analytics_id': 'G-11Q6WJM565',
    }
html_logo = '../figs/RobToolBox_RoundLogoB.png'
html_last_updated_fmt = '%d-%b-%Y'
show_authors = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# autodoc_mock_imports = ["numpy", "scipy"] 

# extensions = ['rst2pdf.pdfbuilder']
# pdf_documents = [('index', u'rst2pdf', u'Sample rst2pdf doc', u'Your Name'),]
autorun_languages = {}
autorun_languages['pycon_output_encoding'] = 'UTF-8'
autorun_languages['pycon_initial_code'] = [
        "from spatialmath import SE3", 
        "SE3._color = False",
        "import numpy as np",
        "np.set_printoptions(precision=4, suppress=True)",
        ]