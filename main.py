import requests
from bs4 import BeautifulSoup
import pandas as pd

#mendefinisikan url yang dituju dan
url = 'https://www.worldometers.info/coronavirus/'

#merequest akses ke web
r = requests.get(url)

#mengambil semua html dari website
soup = BeautifulSoup(r.text, 'lxml')

#mengambil data dari tag table
table = soup.find('table', id='main_table_countries_today')

#mengambil heading dari table
heading = []
for i in table.find_all('th'):
    head = i.text
    heading.append(head)

heading[13] = 'Tests/1M pop'

#mengekpor ke dataframe
df_corona = pd.DataFrame(columns=heading)

#mengisi tabel df_corona
for j in table.find_all('tr')[1:]:
    data_baris = j.find_all('td')
    baris = [tr.text for tr in data_baris]
    panjang = len(df_corona)
    df_corona.loc[panjang] = baris

#delete baris 0 - 6
df_corona.drop(df_corona.index[0:7], inplace=True)
#delete baris 222 - 228
df_corona.drop(df_corona.index[222:229], inplace=True)

#reset index agar mulai dari 0
df_corona.reset_index(inplace=True, drop=True)

#menghilangkan kolom #
df_corona.drop('#', axis=1, inplace=True)


#save dataframe to format csv
df_corona.to_csv('data_corona.csv', index=False)


