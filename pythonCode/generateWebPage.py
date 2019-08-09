import os, sys, re

spexString ='''
<button class="collapsible">SPEX</button>
<div class="content">
SONGS
</div>
'''

oneSong = '''
  <button class="collapsible">SONGTITLE</button>
  <div class="content2">
    SONGTEXT
  </div>
'''

urlToSongs = '/home/markus/sparmen/pythonCode/songTXT/'
monsterString = ''

# sort those fuckers by year. Fuck you 2023
spexPlural = os.listdir(urlToSongs)
test = [[j1,j2] for j1,j2 in zip(spexPlural, [re.search(r'\d\d\d\d', i).group(0) for i in spexPlural])]
test[37][1] = '2013'
test.sort(key = lambda t:t[1])

spexCounter = 0
spexDict = {}

for spex, year in test:
    spexName = re.split(r'[(]', spex)[0]
    if spexName not in spexDict.keys():
        spexCounter += 1
        spexDict[spexName] = {'num' : spexCounter, 'spex' : spexName, 'urls' : []}
    spexDict[spexName]['urls'].append(urlToSongs + spex +'/')

for button in spexDict.keys():
    spexCounter = spexDict[button]['num']
    currentSpexString = re.sub(r'SPEX',str(spexCounter)+ '&nbsp'*5 + re.sub(r'[_]', ' ', button),spexString)
    storeSongs = []
    songCounter = 0
    for song in spexDict[button]['urls']:
        list_of_songs = os.listdir(song)
        list_of_songs.sort()
        y = re.findall(r'\d\d', song)[-1]
        if y[0] == '0':
            y = y[1]
        for song2 in list_of_songs:
            songCounter += 1
            f = open(song + song2, 'r')
            songName = str(spexCounter) +  '.' + str(songCounter) + '.' + y + '&nbsp'*5+ f.readlines(1)[0]
            songText = f.read()
            f.close()
            songText = re.sub(r'\n', '<br>', songText)
            currentSong = re.sub(r'SONGTITLE', songName, oneSong)
            storeSongs.append(re.sub(r'SONGTEXT', songText, currentSong))
    currentSpexString = re.sub(r'SONGS', ''.join(storeSongs), currentSpexString)
    if len(currentSpexString) > 1000:
        monsterString += currentSpexString



webPageURL = '/home/markus/sparmen/pythonCode/webPageMarkus/pageTemplate.html'
webPageURL2 = '/home/markus/sparmen/pythonCode/webPageMarkus/webPage.html'
f = open(webPageURL, 'r')
webPageTemplate = f.read()
f.close()
webPageString = re.sub(r'MONSTERSTRINGHERE',monsterString, webPageTemplate)


w = open(webPageURL2, 'w')
w.write(webPageString)
w.close()
