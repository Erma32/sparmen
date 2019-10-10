import re, os

wk_dir = '/home/markus/sparmen (another copy)/sources2/temp' + '/'

sources = '/home/markus/sparmen (another copy)/sources2/temp/'
file = 'Titanic (VT 2016)'

if file not in os.listdir(wk_dir):
    os.mkdir(wk_dir + file)
else:
    pass

def splitbynum(mass):
    return re.split(r'\d{1,2}[\.]{1,1}', mass)

def splitter(file):
    f = open(sources + file +'.txt', 'r')
    m = f.read()
    f.close()
    return splitbynum(m)

def writer(m):
    songcounter = 0
    for song in m:
        songcounter += 1
        w = open(wk_dir + file + '/' +
                 '{}.txt'.format(songcounter), 'w')
        w.write(song)
        w.close()



m = splitter(file)
writer(m)
