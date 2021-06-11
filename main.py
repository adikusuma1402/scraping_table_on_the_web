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

