import os, sys, re
from os import listdir
from os.path import isfile, join
#
#   Converts all txt in songTXT to html in songHTML
#
#   This code should be written so that i may be run more than once.
#


wk_dir = "/home/mumrah/github/sparmen/"

def html_write(path, path2, spex, song):
    try:
        #   Read song.txt
        f = open(path + song, 'r')

        # Extract title and melody. Has to be First & Second row.
        title = f.readline();
        melody = f.readline();print(title, melody)

        txt = f.read()
        f.close()

        #   Add <br /> instead of \n     [txt -> html]
        song_html = re.sub(r'\n', r'<br />\n', txt)

        h = open('/home/mumrah/github/sparmen/templates/songHTML.html', 'r')
        html = h.read()

        #   Fill in template
        html = re.sub(r'SONG_TITLE',title,      html)
        html = re.sub(r'SONG_MELODY',melody,    html)
        html = re.sub(r'SONG_TEXT',song_html,   html)
        html = re.sub(r'SONG_SPEX',spex,       html)

        #   Write html to song.html
        song2 = song[:-4] + '.html' # remove .txt,replace .html
        w = open(path2 + song2, 'w')
        w.write(html)
        w.close()
    except:
        print('Did not write {}'.format(song))


# Get list directories, create in songHTML (spex)
dir_list = os.listdir(wk_dir + 'pythonCode/songTXT/')

try:
    os.mkdir(wk_dir + 'pythonCode/songHTML/')
except:
    pass

for directory in dir_list:
    try:
        os.mkdir(wk_dir + 'pythonCode/songHTML/' + directory)
    except:
        print('{} already exists'.format(directory))
        pass

dir_list.sort()

dir_list_long = [wk_dir + 'pythonCode/songTXT/' + i + '/' for i in dir_list]
dir_list_long2 = [wk_dir + 'sparmen/songHTML/' + i + '/' for i in dir_list]

for readpath, writepath, spex in zip(dir_list_long, dir_list_long2, dir_list):
    for song in os.listdir(readpath):
        spex2 = re.sub(r'_', r' ', spex)
        html_write(readpath, writepath, spex2, song)
