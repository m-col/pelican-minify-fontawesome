minify-fontawesome - pelican plugin
===================================

minify-fontawesome is a plugin for the `pelican
<https://github.com/getpelican/pelican>`_ static site generator that extracts
only icons used in your website from fontawesome source files upon site
generation. If you only use a small number of icons it reduces served CSS from
around 70KB to around 5KB.

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
