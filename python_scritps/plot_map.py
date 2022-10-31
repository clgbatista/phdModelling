import matplotlib.pyplot as plt
import pandas as pd
import plotly as plotly
import plotly.express as px
import json


input_dir = 'output\coverage\contact_table.csv'
geojson_file = 'libs\geojson\\brazil-states.geojson'

f = open(geojson_file)
brazil = json.load(f)

coverage = pd.read_csv(input_dir)

state_id_map = {}
for feature in brazil ['features']:
    feature['id'] = feature['properties']['name']
    state_id_map[feature['properties']['sigla']] = feature['id']

fig = px.choropleth_mapbox(coverage,
                           geojson=brazil,
                           locations='admin',
                           color='value',
                           # color_continuous_scale="Viridis",
                        #    range_color=(0, 2.4),
                           mapbox_style="carto-darkmatter",
                           zoom=2,
                           center = {"lat": -15.5958, "lon": -56.0969},
                           opacity=0.5,
                           labels={'value':'coverage'}
                          )
fig.update_geos(fitbounds = 'locations', visible = False)
# fig.write_image("fig1.png")
# fig.write_html("fig1.html")
fig.show()