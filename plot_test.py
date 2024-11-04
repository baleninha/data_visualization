import plotly.express as px
import pandas as pd
import numpy as np


data = pd.read_csv(r'C:\Users\baleninha\Downloads\httpsearthquake_usgs_govearthquakesmap.csv')

# Filtramos los datos esenciales
df = data[['latitude', 'longitude', 'mag', 'place']]

# Crear el scatter_mapbox
fig = px.scatter_mapbox(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="place",
    hover_data={"mag": True},
    color="mag",  # Usamos magnitud para colorear los puntos
    size="mag",   # Usamos magnitud para el tamaño del punto
    size_max=15,  # Escalamos el tamaño al doble
    color_continuous_scale="Viridis",
    mapbox_style="open-street-map",
    zoom=1,
    center={"lat": 0, "lon": 0}
)


##########

df = data[['latitude', 'longitude', 'mag', 'place']].copy()
df['scaled_size'] = df['mag'] ** 5 # Ajusta el factor multiplicativo según el tamaño que desees

# Crear el scatter_mapbox con tamaño ajustado
fig = px.scatter_mapbox(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="place",
    hover_data={"mag": True},
    color="mag",  # Colorear los puntos según la magnitud
    size= "scaled_size",  # Usar la columna escalada para el tamaño
    color_continuous_scale="Viridis",
    mapbox_style="open-street-map",
    zoom=1,
    center={"lat": 0, "lon": 0}
)
#######################

fig.update_layout(
    title="Mapa de Terremotos",
    title_x=0.5,
    
    mapbox=dict(
        style="open-street-map",
        zoom=1,
        center={"lat": 0, "lon": 0}
    ),

)

fig.update_layout(title="Mapa de Terremotos", title_x=0.5)
fig.show()

# Guardar como archivo HTML y abrir en navegador
fig.write_html("./static_web/mapa_terremotos.html")