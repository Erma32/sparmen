import os, sys, re
#
#   Creates a full 'Sparmen.html' from all html in songHTML
#   Uses multiple templates found in \templates\
#   This code should be written so that it may run more than once.
#


templateURL = '/home/mumrah/github/sparmen/templates/SparmenTemplate.html'
templateFILE = open(templateURL, 'r')
template = templateFILE.read()

f = open('/home/mumrah/github/sparmen/templates/template2.html', 'r')
spexTemplate = f.read()
spexTemplate

HTML_DIR = '/home/mumrah/github/sparmen/sparmen/songHTML/'
dict = {}

singleSONG =  '<li>\n<a href=SONG_PATH>SONG_NAME</a>\n</li>\n'

for spex in os.listdir(HTML_DIR):
    dict[spex] = {'tag' : '#' + re.sub(r'\s+', '', spex)}

    list_of_songs = os.listdir(HTML_DIR + '/' + spex)
    list_of_songs.sort()

    allSongs = ''
    for song in list_of_songs:
        allSongs += re.sub(r'SONG_PATH', 'songHTML/' + spex +'/' + song, singleSONG)

    dict[spex]['songs'] = allSongs

# Move and replace within templates, multilayered :D:D:D
bigSpex = ''
for spex in dict.keys():
    tag = dict[spex]['tag']
    allSongs = dict[spex]['songs']

    oneSpex = re.sub(r'SPEX_SONGS', allSongs, spexTemplate)
    oneSpex = re.sub(r'SPEX_TAG', dict[spex]['tag'], oneSpex)
    bigSpex += oneSpex

w = open('/home/mumrah/github/sparmen/sparmen/SparmenTest.html', 'w')
html = re.sub(r'ALL_SONGS_TAG', bigSpex, template)
w.write(html)
w.close()
