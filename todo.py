import numpy as np
import os
import datetime
import re
import pandas as pd
url = '/home/markus/Downloads/vivaldi/xlsx/'
def fest(file):
    if re.findall(r'Kläm', file):
        return 'Klämfest'
    if re.findall(r'Resp', file):
        return 'Respektive'
    if re.findall(r'.em', file):
        return 'Temafest'
    if re.findall(r'.ickoff', file):
        return 'Kickoff'
    if re.findall(r'.vslutning', file):
        return 'Avslutning'
    if re.findall(r'remiär', file):
        return 'Premiär'
    else:
        return file


df
df = pd.read_excel(url + file)


# %%
store = {}
for file in os.listdir(url):
    store[file] = {'fest' : '', 'deltagare' : '', 'datum' : ''}

    timestamp= os.path.getmtime(url+file)
    date = datetime.datetime.fromtimestamp(timestamp)
    df = pd.read_excel(url+file)
    deltagare= len(df) - 1
    store[file]['fest']= fest(file)
    store[file]['deltagare']= deltagare
    store[file]['datum']= date


alla_fester= pd.DataFrame(store.values())
respect = alla_fester[alla_fester['fest']=='Respektive']
klamcheck = alla_fester[alla_fester['fest']=='Klämfest']
tema = alla_fester[alla_fester['fest']=='Temafest']
alla_fester


import matplotlib.pyplot as plt

plt.plot(respect[['datum', 'deltagare']])


respect = respect.sort_values(by='datum')
respect

tema = tema.sort_values(by='datum')

tema
klamcheck.sort_values('datum', ascending=[bool])
plt.plot(respect['datum'],respect['deltagare'],'+k')
