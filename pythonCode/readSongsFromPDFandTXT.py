import re, os,sys
from PyPDF2 import PdfFileReader
#
#   Iterates through all pdfs and txts in provided directories
#   Looks to split the massive string  into a list. Splits by numbers.
#   This way it finds both spex by year (\d\d\d\d) and songs ( [d]{1,2} ).
#   These are separated even more further into the code.
#
#   A massive amount of .txt files are created, all with poor grammatical
#   formatting. These are to be formatted by hand. Once this process is begun
#   this script is NEVER run again. Once there are formatted .txt files
#   other scripts take over and formats into HTML, with the same formatting as
#   the .txt
#

# spex available in sångbok.pdf
yearToSpex = {
'19980':'En_Karnevalssaga_(Karnevalen_1998)',
'19990':'Odysseus_Återkomst_(VT_1999)',
'19991':'Amasonernas_Återkomst_(HT_1999)',
'20000':'Alexander_Den_Store_Återkommer_(VT_2000)',
'20001':'Gaius-Caligula_(HT_2000)',
'20010':'Marco_Polo_(VT_2001)',
'20011':'Tutankhanmun_(HT_2001)',
'20020':'En_Karnevalssaga_(VT_2002)',
'20021':'Fantomen_på_YstadOperan_(Karnevalen_2002)',
'20022':'Pizarro_(HT_2002)',
'20030':'Amasonernas_Återkomst_(VT_2003)',
'20031':'DIII_(HT_2003)',
'20040':'Marco_Polo_(HT_2004)',
'20042':'Sherlock_Holmes_(VT_2004)',
'20041':'Fantomen__på_YstadOperan_(Karnevalen_2002)',
'20050':'Tutankhanmun_(VT_2005)',
'20051':'Frankenstein_(Kivik_2005)',
'20052':'Tors_Hammare_(HT_2005)',
'20060':'En_Karnevalssaga_(VT_2006)',
'20061':'Frankenstein_(HT_2006)',
'20062':'Leonardo_(HT_2006)',
'20063':'Livet_i_Revy_(Karnevalen_2006)',
'20064':'Platon_och_Dualismen_(Karnevalen_2006)',
}

for value in yearToSpex.values():
    string = '/home/mumrah/github/sparmen/pythonCode/songTXT/{}'.format(value)
    if os.path.isdir(string):
        pass
    else:
        os.mkdir(string)
del string

path_pdf = '/home/mumrah/github/sparmen/pythonCode/sångbok.pdf'
PAGES = []

f = open(path_pdf, 'rb')
pdf = PdfFileReader(f)

for pagenum in range(pdf.getNumPages()):
    page =pdf.getPage(pagenum)
    try:
        PAGES.append(page.extractText())
    except:
        pass

# Create superlong string with entire PDF
monsterString = ''
for page in PAGES:
    monsterString += page

# SplitByYear
pdfByYear = re.split(r'(\d\d\d\d)\n\n', monsterString)

f.close()
del monsterString, pdf, f, PAGES

spexDict = {}

def iteration(sD, year):
    j = 0
    for i in sD.keys():
        if re.search(year, i):
            j += 1
    return j

currentSpex = 'Anthem'
for row in pdfByYear:
    # Check whether we're looking at a SONG or a new SPEX. 4 numbers in row <=> new spex, else song
    isYear = [re.search(r'^\d\d\d\d', row).group() if re.search(r'^\d\d\d\d', row) else False][0]
    if isYear:
        iter = iteration(spexDict, isYear)
        isYear = isYear+str(iter)
        spexDict[isYear] = {}
        currentSpex = isYear
    else:
        # split by song
        pdfBySong = re.split(r'\n(\d+)[.]{0,1}\s{0,1}\W', row)
        spexDict[currentSpex] = {i[0] : i[1] for i in enumerate(pdfBySong)}

# Popping some that just wont work with current regex. Add these manually!
spexDict.pop('Anthem')
spexDict.pop('19920')
spexDict.pop('20065')

if yearToSpex.keys() == spexDict.keys():
    for spex in spexDict.keys():
        for key in spexDict[spex].keys():
            i = spexDict[spex][key]
            l1 = re.search(r'^\d+', i)
            if l1:
                n = l1.group()
            else:
                l2 = re.search(r'^Från', i)
                if len(i) > 100 or l2:
                    i = re.sub(r'\n\n', r'\n', i)
                    w = open('/home/mumrah/github/sparmen/pythonCode/songTXT/{}/'.format(yearToSpex[spex])  + n + '.txt', 'w')
                    w.write(i)
                    w.close()
else:
    print('yearToSpex.keys() != spexDict.keys() \nNot Writing Anything!')

# %%
wk_dir = '/home/mumrah/github/sparmen/pythonCode/smallPDFs/'

txts = [file for file in os.listdir(wk_dir) if re.search(r'.txt', file)]

dict = {}

for filename in txts:
    #Check year, semester and title from filename
    T = re.search(r'VT|HT|Kivik',filename)
    if T:
        T = T.group()
    else:
        print('VT/HT info missing in title \n{}'.format(filename))

    #check year
    year = re.search(r'\d\d\d\d', filename)
    if year:
        year = year.group()
    else:
        print('year info missing in title \n{}'.format(filename))

    #Define Title
    title = re.search(r'^(.+)\s[(]', filename).group(1)

    # Read
    f = open(wk_dir + filename, 'r')
    string = f.read()
    string = re.sub(r'\d\d[.]\d', '', string)

    entry = title + ' ' + '('+  T +' '+ year+ ')'
    entry = re.sub(r'\s+', '_', entry)

    dict[entry] = {'string' : string}


for spex in dict.keys():
    # 'string' is a full spex
    string = dict[spex]['string']
    # split by song
    stringBySong = re.split(r'\n\d+[.]{0,1}\s{0,1}', string)

    popThese = []
    for i, row in enumerate(stringBySong):
        # Remove if there are any shorter than 100 chars.
        # Many old spex reused and wrote "Song from spex X". These are removed.
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

    # Final step. Write all spex and song into txts. Rewrites existing.
    for i, row in enumerate(stringBySong):
        w = open(dir_path + str(i+1) + '.txt', 'w+')
        w.write(row)
        w.close()
