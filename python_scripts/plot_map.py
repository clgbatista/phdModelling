import os as os

script_name = os.path.basename(__file__)
print('=========================================================')
print('         Runnning <'+script_name+'> script\n')

import pandas as pd

file_path = 'output/coverage/coverageCON1.csv'
coverage = pd.read_csv(file_path)
coverage.rename(columns={'value':'CON1'}, inplace = True)

file_path = 'output/coverage/coverageCON2.csv'
coverage["CON2"] = pd.read_csv(file_path,usecols=['value'])

file_path = 'output/coverage/coverageCON3.csv'
coverage["CON3"] = pd.read_csv(file_path,usecols=['value'])

file_path = 'output/coverage/coverageCON4.csv'
coverage["CON4"] = pd.read_csv(file_path,usecols=['value'])

file_path = 'output/coverage/coverageCON5.csv'
coverage["CON5"] = pd.read_csv(file_path,usecols=['value'])

file_path = 'output/coverage/coverageCON6.csv'
coverage["CON6"] = pd.read_csv(file_path,usecols=['value'])

file_path = 'output/coverage/coverageSCD1.csv'
coverage["SCD1"] = pd.read_csv(file_path,usecols=['value'])

file_path = 'output/coverage/coverageSCD2.csv'
coverage["SCD2"] = pd.read_csv(file_path,usecols=['value'])

file_path = 'output/coverage/coverageCBERS.csv'
coverage["CBERS"] = pd.read_csv(file_path,usecols=['value'])

import plotly as plt
import plotly.express as px
import json
import kaleido

f = open('libs/geojson/brazil-states.geojson')
brazil = json.load(f)

state_id_map = {}
for feature in brazil ['features']:
 feature['id'] = feature['properties']['name']
 state_id_map[feature['properties']['sigla']] = feature['id']

sats = ['CON1', 'CON2', 'CON3', 'CON4', 'CON5', 'CON6', 'SCD1', 'SCD2', 'CBERS']
# sats = ['CON1']

for target in sats:

    print("MAP -- "+target)
    output_file = "output/figs/"+target+".png"

    fig = px.choropleth_mapbox(coverage,
                            geojson=brazil,
                            locations='admin',
                            color=target,
                            # color_continuous_scale="Viridis",
                            #    range_color=(0, 2.4),
                            mapbox_style="carto-darkmatter",
                            zoom=2,
                            center = {"lat": -15.5958, "lon": -56.0969},
                            opacity=0.5,
                            labels={'value':'coverage'},
                            title="Coverage -- Satellite "+target,
                            width=500,
                            height=500
                            )
    fig.update_geos(fitbounds = 'locations', visible = False)
    # fig.write_image(target+".png")
    fig.show()

    print("Saved to "+output_file)