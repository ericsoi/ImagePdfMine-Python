#!/bin/bash
sudo apt-get install python3 -y
printf "\n\n"
sudo apt-get install python3-pip
printf "\n\n"
sudo apt-get install swig -y
printf "\n\n"
sudo apt-get install libmagickwand-dev -y
printf "\n\n"
sudo apt-get install python3-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev -y
printf "\n\n"
pip3 install -r requirements.txt
<<<<<<< HEAD
replace '<policy domain="coder" rights="none" pattern="PDF" />' '<policy domain="coder" rights="read" pattern="PDF" />' -- /etc/ImageMagick-6/policy.xml
cd ..
echo "Enter pdf file path"
read file
./extractscript.py $file
=======
>>>>>>> 2a3e2939e05f4e5375d4471097550b2d12c75bb4
