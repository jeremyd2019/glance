# -*- coding: utf-8 -*-
# Copyright (c) 2010 OpenStack Foundation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# Glance documentation build configuration file, created by
# sphinx-quickstart on Tue May 18 13:50:15 2010.
#
# This file is execfile()'d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

import openstackdocstheme


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path = [
    os.path.abspath('../..'),
    os.path.abspath('../../bin')
    ] + sys.path

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['stevedore.sphinxext',
              'sphinx.ext.viewcode',
              'oslo_config.sphinxext',
              'oslo_config.sphinxconfiggen',
              'openstackdocstheme',
              'sphinxcontrib.apidoc',
              ]

# openstackdocstheme options
repository_name = 'openstack/glance'
bug_project = 'glance'
bug_tag = 'documentation'

# sphinxcontrib.apidoc options
apidoc_module_dir = '../../glance'
apidoc_output_dir = 'contributor/api'
apidoc_excluded_paths = [
    'tests/*',
    'tests',
    'db/sqlalchemy/*',
    'db/sqlalchemy']
apidoc_separate_modules = True

config_generator_config_file = [
    ('../../etc/oslo-config-generator/glance-api.conf',
     '_static/glance-api'),
    ('../../etc/oslo-config-generator/glance-cache.conf',
     '_static/glance-cache'),
    ('../../etc/oslo-config-generator/glance-manage.conf',
     '_static/glance-manage'),
    ('../../etc/oslo-config-generator/glance-scrubber.conf',
     '_static/glance-scrubber'),
]


# Add any paths that contain templates here, relative to this directory.
# templates_path = []

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
copyright = u'2010-present, OpenStack Foundation.'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
#exclude_trees = ['api']
exclude_patterns = [
    # The man directory includes some snippet files that are included
    # in other documents during the build but that should not be
    # included in the toctree themselves, so tell Sphinx to ignore
    # them when scanning for input files.
    'cli/footer.txt',
    'cli/general_options.txt',
    'cli/openstack_options.txt',
]

# The reST default role (for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['glance.']

# -- Options for man page output --------------------------------------------

# Grouping the document tree for man pages.
# List of tuples 'sourcefile', 'target', u'title', u'Authors name', 'manual'

man_pages = [
    ('cli/glanceapi', 'glance-api', u'Glance API Server',
     [u'OpenStack'], 1),
    ('cli/glancecachecleaner', 'glance-cache-cleaner', u'Glance Cache Cleaner',
     [u'OpenStack'], 1),
    ('cli/glancecachemanage', 'glance-cache-manage', u'Glance Cache Manager',
     [u'OpenStack'], 1),
    ('cli/glancecacheprefetcher', 'glance-cache-prefetcher',
     u'Glance Cache Pre-fetcher', [u'OpenStack'], 1),
    ('cli/glancecachepruner', 'glance-cache-pruner', u'Glance Cache Pruner',
     [u'OpenStack'], 1),
    ('cli/glancecontrol', 'glance-control', u'Glance Daemon Control Helper ',
     [u'OpenStack'], 1),
    ('cli/glancemanage', 'glance-manage', u'Glance Management Utility',
     [u'OpenStack'], 1),
    ('cli/glancereplicator', 'glance-replicator', u'Glance Replicator',
     [u'OpenStack'], 1),
    ('cli/glancescrubber', 'glance-scrubber', u'Glance Scrubber Service',
     [u'OpenStack'], 1)
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
# html_theme_path = ["."]
# html_theme = '_theme'
html_theme = 'openstackdocs'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = ['_theme']
html_theme_path = [openstackdocstheme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# Add any paths that contain "extra" files, such as .htaccess or
# robots.txt.
html_extra_path = ['_extra']

# If false, no module index is generated.
html_use_modindex = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'glancedoc'


# -- Options for LaTeX output ------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
# documentclass [howto/manual]).
latex_documents = [
    ('index', 'Glance.tex', u'Glance Documentation',
     u'Glance Team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
