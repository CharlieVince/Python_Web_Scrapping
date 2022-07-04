import requests, json
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
df_result = pd.json_normalize(json_data['jobs'])
df_result.sort_values(by=['salario2'],inplace=True,ascending=False)

print(df_result)