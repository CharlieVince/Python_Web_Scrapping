import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://datatables.net/examples/styling/bootstrap4"
data = requests.get(url).text


soup = BeautifulSoup(data, 'html.parser')

for table in soup.find_all('table'):
    print(table.get('class'))

tables = soup.find_all('table')
table = soup.find('table', class_='table')

df = pd.DataFrame(columns=['Name', 'Position',
                           'Office', 'Age', 'Start date', 'Salary'])

for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')

    if(columns != []):
        name = columns[0].text.strip()
        position = columns[1].text.strip()
        office = columns[2].text.strip()
        age = columns[3].text.strip()
        start_date = columns[4].text.strip()
        salary = columns[5].text.strip()

        df = df.append({'Name': name, 'Position': position, 'Office': office,
                        'Age': age, 'Start date': start_date, 'Salary': salary}, ignore_index=True)

print(df)
