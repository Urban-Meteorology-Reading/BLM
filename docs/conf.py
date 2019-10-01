# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
# from pybtex.richtext import Tag,String
from pybtex.style.sorting.author_year_title import SortingStyle as Sorter
from pybtex.style.template import (
    join, words, field, optional, first_of,
    names, sentence, tag, optional_field, href
)
from pybtex.style.formatting import toplevel, BaseStyle
from pybtex.plugin import register_plugin
from pybtex.style.formatting.unsrt import Style as UnsrtStyle, pages, date, Text

import platform
import datetime
import sphinx_rtd_theme
import nbsphinx
import sphinxcontrib.bibtex

# -- Project information -----------------------------------------------------

project = u'BLM'
doc_name = u'Boundary-Layer Meteorology'
copyright = u'2019, Prof Sue Grimmond & Dr Ting Sun'
author = u'Prof Sue Grimmond & Dr Ting Sun'

# The short X.Y version
version = u'2019 Autumn'
# The full version, including alpha/beta/rc tags
release = datetime.date.today().isoformat()


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinxcontrib.bibtex',
    # 'rinoh.frontend.sphinx',
    # 'sphinxfortran.fortran_autodoc',
    # 'sphinxfortran.fortran_domain',
    'sphinx.ext.githubpages'

]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'
master_doc_latex = 'index_latex'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .

# Exclude build directory and Jupyter backup files:
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# Don't add .txt suffix to source files (available for Sphinx >= 1.5):
html_sourcelink_suffix = ''

# Execute notebooks before conversion: 'always', 'never', 'auto' (default)
nbsphinx_execute = 'always'

# Use this kernel instead of the one stored in the notebook metadata:
nbsphinx_kernel_name = 'python3'

# List of arguments to be passed to the kernel that executes the notebooks:
nbsphinx_execute_arguments = ['--InlineBackend.figure_formats={"png", "pdf"}']

# If True, the build process is continued even if an exception occurs:
nbsphinx_allow_errors = True

# Controls when a cell will time out (defaults to 30; use -1 for no timeout):
nbsphinx_timeout = 60

# Default Pygments lexer for syntax highlighting in code cells:
nbsphinx_codecell_lexer = 'ipython3'

# Width of input/output prompts used in CSS:
nbsphinx_prompt_width = '8ex'

# If window is narrower than this, input/output prompts are on separate lines:
nbsphinx_responsive_width = '700px'

# tags.add('html')
# if tags.has('html'):
#     exclude_patterns = ['references.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# default interpretation of `role` markups
default_role = 'math'

# math options
numfig = True
math_numfig = True
numfig_secnum_depth = 1
math_eqref_format = "Eq.{number}"

# some text replacement defintions
rst_prolog = """
.. |km^-1| replace:: km\ :sup:`-1`
.. |mm^-1| replace:: mm\ :sup:`-1`
.. |m^-1| replace:: m\ :sup:`-1`
.. |m^-2| replace:: m\ :sup:`-2`
.. |m^-3| replace:: m\ :sup:`-3`
.. |m^2| replace:: m\ :sup:`2`
.. |m^3| replace:: m\ :sup:`3`
.. |s^-1| replace:: s\ :sup:`-1`
.. |kg^-1| replace:: kg\ :sup:`-1`
.. |K^-1| replace:: K\ :sup:`-1`
.. |W^-1| replace:: W\ :sup:`-1`
.. |h^-1| replace:: h\ :sup:`-1`
.. |ha^-1| replace:: ha\ :sup:`-1`
.. |QF| replace:: Q\ :sub:`F`
.. |Qstar| replace:: Q\ :sup:`*`
.. |d^-1| replace:: d\ :sup:`-1`
.. |d^-2| replace:: d\ :sup:`-2`
.. |)^-1| replace:: )\ :sup:`-1`
.. |Recmd| replace:: **Recommended in this version.**
.. |NotRecmd| replace:: **Not recommended in this version.**
.. |NotAvail| replace:: **Not available in this version.**
.. |NotUsed| replace:: **Not used in this version.**
"""
# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes"]


# This is processed by Jinja2 and inserted before each notebook
nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base='docs') %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::

        This page was generated from `{{ docname }}`__.
        Interactive online version:
        :raw-html:`<a href="https://mybinder.org/v2/gh/Urban-Meteorology-Reading/BLM/master?filepath={{ docname }}"><img alt="Binder badge" src="https://mybinder.org/badge.svg" style="vertical-align:text-bottom"></a>`
        Slideshow:
        :raw-html:`<a href="https://nbviewer.jupyter.org/format/slides/github/Urban-Meteorology-Reading/BLM/tree/master/{{ docname }}"><img alt="Binder badge" src="https://img.shields.io/badge/render-nbviewer-orange.svg" style="vertical-align:text-bottom"></a>`

    __ https://github.com/Urban-Meteorology-Reading/BLM/blob/master/{{ docname }}

.. raw:: latex

    \vfil\penalty-1\vfilneg
    \vspace{\baselineskip}
    \textcolor{gray}{The following section was generated from
    \texttt{\strut{}{{ docname }}}\\[-0.5\baselineskip]
    \noindent\rule{\textwidth}{0.4pt}}
    \vspace{-2\baselineskip}
"""

# This is processed by Jinja2 and inserted after each notebook
nbsphinx_epilog = r"""
.. raw:: latex

    \textcolor{gray}{\noindent\rule{\textwidth}{0.4pt}\\
    \hbox{}\hfill End of
    \texttt{\strut{}{{ env.doc2path(env.docname, base='doc') }}}}
    \vfil\penalty-1\vfilneg
"""

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#
html_static_path = ['_static']
html_context = {
    'css_files': [
        '_static/fix-eq.css',  # override wide tables in RTD theme
    ],
}

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
numfig = True
# html_logo = 'assets/img/SUEWS_LOGO.png'

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'BLM_doc'


# -- Options for LaTeX output ------------------------------------------------
# this can be one of ['pdflatex', 'xelatex', 'lualatex', 'platex']
if platform.system() == 'Darwin':
    latex_engine = 'lualatex'
else:
    latex_engine = 'pdflatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
\usepackage[titles]{tocloft}
\usepackage{ragged2e}
\addto\captionsenglish{\renewcommand{\bibname}{References}}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
\newcolumntype{T}{L}
\setlength{\tymin}{40pt}
''',


    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

latex_show_pagerefs = False

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc,
     'BLM-UoR.tex',
     doc_name,
     author,
     'manual'),
]
# latex_logo = 'assets/img/SUEWS_LOGO.png'

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'BLM-UoR', u'BLM-UoR',
     [author], 1),
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'BLM-UoR', u'BLM-UoR',
     author, 'BLM-UoR', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------
# rinoh_documents = [('index',            # top-level file (index.rst)
#                     'target',           # output (target.pdf)
#                     'Document Title',   # document title
#                     'John A. Uthor')]   # document author

# Fix equation formatting in the RTD-theme
def setup(app):
    app.add_stylesheet('fix-eq.css')


# Custom bibliography stuff for sphinxcontrib.bibtex
class MySort(Sorter):

    def sort(self, entries):
        entry_dict = dict(
            (self.sorting_key(entry), entry)
            for entry in entries
        )
        sorted_keys = sorted(entry_dict, reverse=True)
        sorted_entries = [entry_dict[key] for key in sorted_keys]
        return sorted_entries

    def sorting_key(self, entry):
        if entry.type in ('book', 'inbook'):
            author_key = self.author_editor_key(entry)
        elif 'author' in entry.persons:
            author_key = self.persons_key(entry.persons['author'])
        else:
            author_key = ''
        return (entry.fields.get('year', ''),
                author_key,
                entry.fields.get('title', ''))


class MyStyle(UnsrtStyle):
    default_sorting_style = 'author_year_title'
    # default_label_style = 'number'

    def get_book_template(self, e):
        template = toplevel[
            self.format_author_or_editor(e),
            self.format_btitle(e, 'title'),
            self.format_volume_and_series(e),
            sentence[
                field('publisher'),
                self.format_edition(e),
                date
            ],
            optional[sentence[self.format_isbn(e)]],
            self.format_web_refs(e),

            # tag('strong')[optional_field('note')],
        ]

        return template


# reading list style
class RLStyle(UnsrtStyle):
    default_sorting_style = 'author_year_title'
    default_label_style = 'number'

    def get_book_template(self, e):
        template = toplevel[
                self.format_author_or_editor(e),
                self.format_btitle(e, 'title'),
                self.format_volume_and_series(e),
                sentence[
                    field('publisher'),
                    self.format_edition(e),
                    date
                ],
                optional[sentence[self.format_isbn(e)]],
                self.format_web_refs(e),

            tag('strong')[optional_field('note')],
            ]

        return template

    # format_online = format_article
    # format_book = format_article



register_plugin('pybtex.style.formatting', 'refs', MyStyle)
register_plugin('pybtex.style.formatting', 'rl', RLStyle)
# register_plugin('pybtex.style.sorting', 'year_author_title', MySort)
