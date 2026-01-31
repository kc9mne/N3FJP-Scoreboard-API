#!/usr/bin/env python3
"""
Download Leaflet.js library for offline use
Run this once before Field Day to ensure map works without internet
"""

import os
import urllib.request

# Create www/lib directory if it doesn't exist
os.makedirs('www/lib', exist_ok=True)

print("Downloading Leaflet.js for offline use...")

# Download Leaflet CSS
leaflet_css_url = "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
print(f"Downloading {leaflet_css_url}")
urllib.request.urlretrieve(leaflet_css_url, 'www/lib/leaflet.css')

# Download Leaflet JS
leaflet_js_url = "https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
print(f"Downloading {leaflet_js_url}")
urllib.request.urlretrieve(leaflet_js_url, 'www/lib/leaflet.js')

# Download marker icons
marker_icon_url = "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png"
print(f"Downloading {marker_icon_url}")
os.makedirs('www/lib/images', exist_ok=True)
urllib.request.urlretrieve(marker_icon_url, 'www/lib/images/marker-icon.png')

marker_icon_2x_url = "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png"
print(f"Downloading {marker_icon_2x_url}")
urllib.request.urlretrieve(marker_icon_2x_url, 'www/lib/images/marker-icon-2x.png')

marker_shadow_url = "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png"
print(f"Downloading {marker_shadow_url}")
urllib.request.urlretrieve(marker_shadow_url, 'www/lib/images/marker-shadow.png')

print("\n✅ Leaflet downloaded successfully!")
print("All map resources are now available offline in www/lib/")
