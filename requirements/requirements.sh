#!/bin/bash
sudo apt-get install python3 -y
printf "\n\n"
sudo apt-get install pythin3-pip
printf "\n\n"
sudo apt-get install swig -y
printf "\n\n"
sudo apt-get install python3-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev -y
printf "\n\n"
pip3 install -r requirements.txt