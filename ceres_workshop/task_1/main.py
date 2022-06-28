import json
import shutil

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

shutil.unpack_archive(
    "/home/joe/Repositories/ceres-workshop/data/strandings.zip"
)

df = pd.read_csv("resource.csv")
df["Length"] = pd.cut(
    pd.to_numeric(df["Length et"], errors="coerce"), bins=range(4, 20, 2)
)

"""with open("resource.csv") as file:
    reader = csv.reader(file)

    print(next(iter(reader)))
"""

uk_latlong = {
    "lataxis": {
        "range": (49, 62),
    },
    "lonaxis": {
        "range": (-11, 2),
    },
}

fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    color="Length",
    hover_data=["Date", "Location", "Common Name "],
    projection="equirectangular",
)
fig.update_geos(
    **uk_latlong,
    resolution=50,
    showcoastlines=True,
    coastlinecolor="RebeccaPurple",
    showocean=True,
    oceancolor="LightBlue",
    showland=True,
    landcolor="LightGreen"
)
fig.show()
