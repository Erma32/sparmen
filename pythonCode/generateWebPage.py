import os, sys, re
from itertools import cycle

spexString ='''
<button class="collapsible">SPEX</button>
<div class="content">
SONGS
</div>
'''
spexString2 ='''
<button class="collapsible4">SPEX</button>
<div class="content">
SONGS
</div>
'''
SS = cycle([spexString,spexString2])

oneSong = '''
  <button class="collapsible3">SONGTITLE</button>
  <div class="content2">
    SONGTEXT
  </div>
'''
oneSong2 = '''
  <button class="collapsible5">SONGTITLE</button>
  <div class="content2">
    SONGTEXT
  </div>
'''
OS = cycle([oneSong, oneSong2])

titleBox = '''<button class="collapsible2">YEAR</button>
<div class="content2">

</div>
'''

urlToSongs = '/home/mumrah/PycharmProjects/sparmen/pythonCode/songTXT/'
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
    currentSpexString = re.sub(r'SPEX',
                               str(spexCounter)+ '&nbsp'*5 + re.sub(r'[_]', ' ', button),next(SS))

    storeSongs = []
    songCounter = 0
    for song in spexDict[button]['urls']:
        list_of_songs = os.listdir(song)
        list_of_songs.sort()
        y = re.findall(r'\d\d', song)[-1]
        storeSongs.append(re.sub('YEAR', re.findall(r'\d\d\d\d', song)[-1], titleBox))
        if y[0] == '0':
            y = y[1]

        for song2 in list_of_songs:
            songCounter += 1
            f = open(song + song2, 'r')
            songName = '<b>' + str(spexCounter) +  '.' + str(songCounter)  + '&nbsp'*5+ f.readlines(1)[0] + '</b>'
            songText = f.read()
            f.close()
            songText = re.sub(r'\n', '<br>', songText)
            m = re.split(r'<br>',songText)
            m[0] = '<i><b><small>' + m[0] + '</small></b></i><br>'
            songText = '<br>'.join(m)
            currentSong = re.sub(r'SONGTITLE', songName, next(OS))
            storeSongs.append(re.sub(r'SONGTEXT', songText, currentSong))

    currentSpexString = re.sub(r'SONGS', ''.join(storeSongs), currentSpexString)

    if len(currentSpexString) > 1000:
        monsterString += currentSpexString



webPageURL = '/home/mumrah/PycharmProjects/sparmen/pythonCode/webPageMarkus/pageTemplate.html'
webPageURL2 = '/home/mumrah/PycharmProjects/sparmen/pythonCode/webPageMarkus/webPage.html'
f = open(webPageURL, 'r')
webPageTemplate = f.read()
f.close()
webPageString = re.sub(r'MONSTERSTRINGHERE',monsterString, webPageTemplate)


w = open(webPageURL2, 'w')
w.write(webPageString)
w.close()
