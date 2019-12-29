#!/usr/bin/env python3
import os
from shutil import copy

current_dir = os.path.dirname(os.path.realpath(__file__))
leaflet_fullscreen_dir = os.path.join(current_dir, "node_modules", "leaflet.fullscreen")
geoadmin_static_dir = os.path.join(current_dir, "geolocation_portal", "geoadmin", "static", "geoadmin")

files = ['Control.FullScreen.css', 'Control.FullScreen.js', 'icon-fullscreen-2x.png', 'icon-fullscreen.png']

for file in files:
    src = os.path.join(leaflet_fullscreen_dir, file)
    target = os.path.join(geoadmin_static_dir, file)
    copy(src, target)
