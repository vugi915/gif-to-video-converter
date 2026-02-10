#!/bin/bash
# Install packages.
pip3 install --upgrade moviepy
pip3 install --upgrade questionary
pip3 install --upgrade pyinstaller
# Create bin file.
pyinstaller --onefile --copy-metadata imageio giftovideo.py
# Move bin file.
mv dist/giftovideo .
# Delete build files.
rm -rf build dist *.spec
