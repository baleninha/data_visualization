import plotly.express as px
import pandas as pd
import numpy as np


data = pd.read_csv(r'C:\Users\baleninha\Downloads\httpsearthquake_usgs_govearthquakesmap.csv')

# filtrar los datos relevantes
df = data[['latitude', 'longitude', 'mag', 'place']]

fig = px.scatter_mapbox(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="place",
    hover_data={"mag": True},
    color="mag",  # usamos magnitud para colorear los puntos
    size="mag",   # usamos magnitud para el tamaño del punto
    size_max=15,  # escalamos el tamaño al doble
    color_continuous_scale="Viridis",
    mapbox_style="open-street-map",
    zoom=1,
    center={"lat": 0, "lon": 0}
)


##########

df = data[['latitude', 'longitude', 'mag', 'place']].copy()
df['scaled_size'] = df['mag'] ** 5 

fig = px.scatter_mapbox(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="place",
    hover_data={"mag": True},
    color="mag",  
    size= "scaled_size",  
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

fig.write_html("./static_web/mapa_terremotos.html")
