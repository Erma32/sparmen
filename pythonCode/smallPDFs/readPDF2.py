import re, os,sys
# %%
wk_dir = '/home/mumrah/github/sparmen/pythonCode/smallPDFs/'

txts = [file for file in os.listdir(wk_dir) if re.search(r'.txt', file)]

dict = {}

for filename in txts:
    T = re.search(r'VT|HT|Kivik',filename)
    if T:
        T = T.group()
    else:
        print('VT/HT info missing in title \n{}'.format(filename))

    year = re.search(r'\d\d\d\d', filename)
    if year:
        year = year.group()
    else:
        print('year info missing in title \n{}'.format(filename))

    title = re.search(r'^(.+)\s[(]', filename).group(1)

    # Read
    f = open(wk_dir + filename, 'r')
    string = f.read()

    string = re.sub(r'\d\d[.]\d', '', string)

    dict[title + ' ' + '('+  T +' '+ year+ ')'] = {'string' : string}


for spex in dict.keys():
    # split by song
    string = dict[spex]['string']
    stringBySong = re.split(r'\n\d+[.]{0,1}\s{0,1}', string)
    popThese = []
    for i, row in enumerate(stringBySong):
        if len(row) < 100:
            popThese.append(i)
    for pop in popThese[::-1]:
        stringBySong.pop(pop)

    dict[spex]['songs'] = {i+1 : row for i,row in enumerate(stringBySong)}
    # Check and create directory

    dir_path = '/home/mumrah/github/sparmen/pythonCode/songTXT/{}/'.format(spex)
    if os.path.isdir(dir_path):
        pass
    else:
        os.mkdir(dir_path)
    for i, row in enumerate(stringBySong):
        w = open(dir_path + str(i+1) + '.txt', 'w+')
        w.write(row)
        w.close()
