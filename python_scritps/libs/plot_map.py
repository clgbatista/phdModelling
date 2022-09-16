import pandas as pd

data = pd.read_csv('geojson/brazil_geo.json')

import plotly.express as px

fig = px.choropleth()