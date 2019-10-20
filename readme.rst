minify-fontawesome - pelican plugin
===================================

minify-fontawesome is a plugin for the `pelican
<https://github.com/getpelican/pelican>`_ static site generator that copies
fontawesome fonts and css into your output folder, *excluding* those that are
not found in your site.

If you only use a small number of icons it can reduce fontawesome CSS from
~70KB to ~5KB, and fonts from ~90KB to ~2KB.

At the end of site generation, the plugin identifies which icons are being used
and copies the CSS and font definitions of these icons into
*output_path/static/css/fa.css* and *output_path/static/webfonts/*
respectively.

To enable, `download fontawesome <https://fontawesome.com/download>`_ and set
this variable in your pelicanconf.py to the path where fontawesome is saved
(for example):

.. code-block:: python

   MINIFY_FONTAWESOME = '/home/user/fontawesome-free-5.11.2-web'

Fontforge must be installed, and is available in many linux distribution
repositories.

Much like with normal fontawesome usage, the CSS file should be linked in html
headers, i.e. put this into page templates:

.. code-block:: html

    <link rel="stylesheet" href="{{ SITEURL }}/theme/css/fa.css"/>

RST roles
---------

This plugin also adds 3 small RST roles that can be used to include font
awesome icons in RST drafts:

.. code-block:: RST

   Here is a solid icon :fas:`blender-phone`
   Here is a regular icon :far:`meh-rolling-eyes`
   Here is a brand icon :fab:`github`

Troubleshooting
---------------

If you are writing using the local devserver and new fonts are not showing in
your draft, your browser has likely cached an older version of the generated
font. Many browsers have a way to force a refresh of all requests, including
fonts, which will fix this. In Firefox this is Ctrl-F5 instead of just F5 to
refresh.

This plugin has only been tested with fontawesome-free-5.11.2-web so far.
