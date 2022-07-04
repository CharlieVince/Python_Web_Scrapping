import requests, json
from os import remove
import pandas as pd

payload = {
    #Departamento
    'sids': '1',
    #Categoria
    'aids': '4',
    #pagination
    'rpp': '400',
    #Pagina
    'p': '1'
}

data = requests.post('https://gt.transdoc.com/trabajos/busqueda/ajax_search/', data=payload)

json_data = json.loads(data.text)
df = pd.json_normalize(json_data['jobs'])
df.sort_values(by=['salario2'],inplace=True)

print(df)