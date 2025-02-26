from pathlib import Path
import json

import plotly.express as px

#Lê os dados como uma string e os converte em um objeto Python
path = Path('readable_allmonth_earthquakes.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#Transformara em algo mais legível
#path = Path('eq_data/readable_eq_data.geojson')
#readable_contents = json.dumps(all_eq_data, indent=4)
#path.write_text(readable_contents)

#Examina todos os terremotos no conjunto de dados
all_eq_dicts = all_eq_data['features']
titulonovo = all_eq_data['metadata']['title']


mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)
    eq_titles.append(eq_title)


title = titulonovo
fig = px.scatter_geo(lat=lats, lon=lons, title=title,
        color=mags,
        color_continuous_scale='turbo',
        labels={'color': 'Magnitude'},
        projection= 'natural earth',
        hover_name=eq_titles,
    )
                    

fig.show()


#Criação de um grafico plotly
#baixei os dados https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
#no dia 26/02/2025, dados de todos os terremotos registrados do ultimo mês
#prmeiro tive que criar um código para formatalo  utf-8
#Compartilharei o código abaixo que o formatou
#depois desenvolvi o código que lia as str e as transformava em objetos
#depois criei uma variavel que examinava todos os terremotos no conjunto de dados
#Criei listas vazias e armazenei as informações, latitude, longitude magnitude
#eq_title para criar o texto flutuante com hover_name
#  com um loop for que os extraia do json
#depois com .scatter_geo do Plotly express e  criei um mapa de dispersão geográfica 
#projection define o paramêtro do mapa  a ser projetado
#fig.show() para exibir

#formatar abaixo
#from pathlib import Path
#import json

#path = Path('eq_data/all_month.geojson')
#contents = path.read_bytes()

#all_eq_data = json.loads(contents)

#path = Path('eq_data/readable_allmonth_earthquakes.geojson')
#readable_contents = json.dumps(all_eq_data, indent=4)
#path.write_text(readable_contents, encoding='utf-8')





