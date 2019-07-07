import os, sys, re
import pandas as pd
import xlsxwriter
dict = {}
for dir in os.listdir('/home/mumrah/github/sparmen/pythonCode/songTXT'):
    split = re.split(r'_', dir)
    for word in split:
        S = re.search(r'([(])(.*)', word)
        Y = re.search(r'\d\d\d\d', word)
        if S:
            sem = S.group(2)
        if Y:
            year = int(Y.group())
    if year not in dict.keys():
        dict[year] = {'Karnevalen' : False, 'Kivik': False, 'VT' : False, 'HT' : False}
    else:
        pass

    dict[year][sem] = True
    print(sem,year)
years = [year for year in dict.keys()]
years.sort()


df = pd.DataFrame(dict); df = df.T; df.sort_index()
df.to_excel('/home/mumrah/github/sparmen/pythonCode/whichSpex.xlsx', engine='xlsxwriter')


for year in years:
    print(year, dict[year])
