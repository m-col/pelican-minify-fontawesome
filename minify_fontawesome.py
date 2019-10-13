# -*- coding: utf-8 -*-
#
# pelican-minify-fontawesome
# 
# Copyright (C) 2019 mcol@posteo.net
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import fontforge as ff
import os
from pelican import signals
import re


def copy_glyphs(source, dest, css_blocks):
    """
    Copy only used icons from the font files into the output folder.
    """
    used_icons = []
    for block in css_blocks:
        used_icons.append(re.search('content:"(.*?)"', block).group(0))

    return  #TODO
    for root, dirs, files in os.walk(source):
        for f in files:
            if f.endswith('woff'):
                font = ff.open(os.path.join(root, f))
                for icon in used_icons:
                    if font.findEncodingSlot(icon):
                        font.selection.select(
                            ("more", None),
                            icon,
                        )
                font.copy()
                new_font = ff.font()
                new_font.paste()
                new_font.fontname = font.fontname
                new_font.generate(os.path.join(dest, f))


def get_classes(folder):
    """
    Gets a list of CSS classes defined in all html files within a folder.
    """
    fa_classes = []
    all_classes = []

    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith('html'):
                with open(os.path.join(root, f), "r") as fd:
                    matches = re.findall('class=[\'"](.*?)[\'"]', fd.read())
                    if matches:
                        for match in matches:
                            all_classes.extend(match.split())
    
    for cls in set(all_classes):
        if cls.startswith('fa'):
            fa_classes.append(cls)

    return fa_classes


def copy_css(output_path, css_file):
    """
    Copy css for only used icons over to output folder. Returns the css blocks
    corresponding to these icons so we know which icons to copy from the font
    files.
    """
    with open(css_file, 'r') as fd:
        contents = fd.read()

    base_css = re.sub('\.fa-[\w-]+:before.*?}', '', contents)

    css_blocks = []
    for cls in get_classes(output_path):
        match = re.search(f'\.{cls}:before.*?}}', contents)
        if match:
            css_blocks.append(match.group(0))

    css = base_css + ''.join(css_blocks)
    css_file = os.path.join(output_path, 'theme', 'css', 'fa.css')
    with open(css_file, 'w') as fd:
        fd.write(css)

    return css_blocks


def main(instance):
    FONT_PATH = instance.settings.get('MINIFY_FONTAWESOME', None)
    if not FONT_PATH or not os.path.isdir(FONT_PATH):
        return

    output_path = instance.output_path
    css_file = os.path.join(FONT_PATH, 'css', 'all.min.css')

    css_blocks = copy_css(
        output_path,
        css_file,
    )

    copy_glyphs(
        os.path.join(FONT_PATH, 'webfonts'),
        os.path.join(output_path, 'static', 'webfonts'),
        css_blocks,
    )


def register():
    signals.finalized.connect(main)
