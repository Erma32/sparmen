import os, sys, re
from itertools import cycle


spexString ='''
<button class="titlebutton1">SPEX</button>
<div class="content">
SONGS
</div>
'''

spexString2 ='''
<button class="titlebutton2">SPEX</button>
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

def genPage(showMelody=True):
    wk_dir = '/home/markus/sparmen/'
    # wk_dir = os.getcwd() + '/'
    urlToSongs = wk_dir + '/songTXT/'
    monsterString = ''

    # sort those fuckers by year. Fuck you 2023
    spexPlural = os.listdir(urlToSongs)
    test = [[j1, j2] for j1, j2 in zip(spexPlural, [re.search(r'\d\d\d\d', i).group(0) for i in spexPlural])]
    test[37][1] = '2013'
    test.sort(key=lambda t: t[1])

    spexCounter = 0
    spexDict = {}
    bigSongCounter = 0
    bigSpexCounter = 0
    sommarSpexCounter = 0
    karnevalsSpexCounter = 0

    for spex, year in test:
        spexName = re.split(r'[(]', spex)[0]
        bigSpexCounter += 1
        if spexName not in spexDict.keys():
            spexCounter += 1
            spexDict[spexName] = {'num': spexCounter, 'spex': spexName, 'urls': []}
            if spexName == 'Trollet_Återvander_':
                spexCounter += -1
                spexDict[spexName] = {'num': '1337', 'spex': spexName, 'urls': []}

        spexDict[spexName]['urls'].append(urlToSongs + spex + '/')

    for button in spexDict.keys():
        spexCounter = spexDict[button]['num']

        currentSpexString = next(SS)
        title = str(spexCounter)+ '&nbsp'*5 + re.sub(r'[_]', ' ', button) + '&nbsp'*5 + '['

        storeSongs = []
        songCounter = 0
        for song in spexDict[button]['urls']:

            list_of_songs = os.listdir(song)
            list_of_songs = [i.split('.', maxsplit=1) for i in list_of_songs]
            list_of_songs.sort(key=lambda x:int(x[0]))
            list_of_songs = ['.'.join(i) for i in list_of_songs]

            y = re.findall(r'\d\d', song)[-1]
            storeSongs.append(re.sub('YEAR', re.findall(r'\d\d\d\d', song)[-1], titleBox))
            sem = re.split('_', song)[-2][1:]

            if sem == 'Karnevalen':
                sem = 'K'
                karnevalsSpexCounter +=1
            elif sem == 'Kivik':
                sommarSpexCounter += 1
                sem = 'S'
            elif len(sem) != 2:
                sem = 'E'
            title += sem + y + ', '

            for song2 in list_of_songs:
                songCounter += 1

                f = open(song + song2, 'r')
                try:
                    sname = re.sub(r'\d+[.]\s', '', f.readlines(1)[0])

                    songName = '<b>' + str(spexCounter) +  '.' + str(songCounter)  + '&nbsp'*5+ sname + '</b>'
                    songText = f.read()
                except:
                    pass
                f.close()

                songText = re.sub(r'\n', '<br>', songText)
                m = re.split(r'<br>',songText)
                if showMelody == True:
                    m[0] = '<i><b><small>' + m[0] + '</small></b></i><br>'
                else:
                    m[0] = '\n'

                songText = '<br>'.join(m)
                currentSong = re.sub(r'SONGTITLE', songName, next(OS))
                storeSongs.append(re.sub(r'SONGTEXT', songText, currentSong))

        currentSpexString = re.sub(r'SPEX', title[:-2]+']', currentSpexString)
        currentSpexString = re.sub(r'SONGS', ''.join(storeSongs), currentSpexString)

        monsterString += currentSpexString
        bigSongCounter += songCounter

    #read webpage TEMPLATE
    f = open(wk_dir + 'pageTemplate.html', 'r')
    webPageTemplate = f.read()
    f.close()

    webPageString = re.sub(r'MONSTERSTRINGHERE',monsterString, webPageTemplate)

    # HTML är ju kul. Ersätter åäö med kompatiblare tecken.
    if 1==1:
        webPageString = re.sub(r'ä', '&auml', webPageString)
        webPageString = re.sub(r'å', '&aring', webPageString)
        webPageString = re.sub(r'ö', '&ouml', webPageString)
        webPageString = re.sub(r'Ä', '&Auml', webPageString)
        webPageString = re.sub(r'Å', '&Aring', webPageString)
        webPageString = re.sub(r'Ö', '&Ouml', webPageString)
        # Fuck you 2023
        webPageString = re.sub(r'202\s3', '2023', webPageString)

    #write webpage FULL
    w = open(wk_dir + 'webPage{}.html'.format(str(showMelody)), 'w')

    w.write(webPageString)
    w.close()


    # %% Renaming songs in folders
    for spex in os.listdir(urlToSongs):
        for song in os.listdir(urlToSongs + spex):
            f = open(urlToSongs + spex + '/' + song, 'r')
            digit = re.split('[.]', song)[0]
            m = f.readline()
            f.close()
            m = re.sub(r'[/\n\.]', '-', m)

            os.rename(urlToSongs + spex +'/' + song,
                      urlToSongs + spex +'/' + digit + '.' + m + '.txt')

genPage(showMelody=True)
genPage(showMelody=False)





