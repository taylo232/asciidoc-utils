#!/usr/bin/env python3

"""
(R)ichard's (AS)ciidoc (PUB)lish
Move html files in the current folder to the pub folder for writing and
optionally copy folders to ext website (ftp)
INPUT: [optional] switch to activate copy to website
OUTPUT: HTML files moved to pub folder. New index.html written in pub file (newest files at the top)
TODO: transfer to ftp site with cmdline switch
"""
import os
import glob
import shutil as f

####################################################
# change to your 'published' directory 
PUBDIR = '/home/<user>/writing/pub'
####################################################

CURDIR = os.getcwd()

# copy files to the distant pub directory
print("Copy web files to the pub directory")
for files in glob.glob(r'./*.html'):
    f.copy(files, PUBDIR)

# go to pub directory. remove existing index.html file
os.chdir(PUBDIR)

print("Creating new index page")
# get list of html files in date-modified order
FILES = glob.glob('*.html')
FILES.sort(key=os.path.getmtime, reverse=True)

INDEX = '<html><head><link rel="stylesheet" type="text/css" href="pub.css"><title>Writing</title></head><body><h2>RJT Writing</h2>'

for f in FILES:
    if f != 'index.html':
        INDEX = INDEX + '<p><a href="' + f + '">' + os.path.splitext(f)[0] + '</a></p>'

INDEX = INDEX + '</font></body></html>'


i = open('index.html', 'w')
i.write(INDEX)
i.close()

print("Done")
