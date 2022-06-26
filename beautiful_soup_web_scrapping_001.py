import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://pt.wikipedia.org/wiki/Lista_de_bairros_de_Manaus"
data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')


for table in soup.find_all('table'):
    print(table.get('class'))

tables = soup.find_all('table')
table = soup.find('table', class_='wikitable sortable')

df = pd.DataFrame(columns=['Neighborhood', 'Zone', 'Area', 'Population', 'Density', 'Homes_count'])

for row in table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    
    if(columns != []):
        neighborhood = columns[0].text.strip()
        zone = columns[1].text.strip()
        area = columns[2].span.contents[0].strip('&0.')
        population = columns[3].span.contents[0].strip('&0.')
        density = columns[4].span.contents[0].strip('&0.')
        homes_count = columns[5].span.contents[0].strip('&0.')

        df = df.append({'Neighborhood': neighborhood,  'Zone': zone, 'Area': area, 'Population': population, 'Density': density, 'Homes_count': homes_count}, ignore_index=True)

print(df)