#!/bin/bash
# Install packages.
pip3 install --upgrade moviepy
pip3 install --upgrade pyinstaller
# Create bin files.
pyinstaller --onefile giftovideo.py
# Move bin files.
mv dist/videoto* .
# Delete build files.
rm -rf build dist *.spec
