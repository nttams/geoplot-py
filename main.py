import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import geodatasets
import matplotlib.pyplot as plt

file_paths = [
    "resources/uberh3_vnm_res_4.csv",
    "resources/uberh3_rus_res_4.csv",
    "resources/uberh3_usa_res_4.csv"
]
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'cyan', 'magenta', 'yellow']

world = gpd.read_file(geodatasets.data.naturalearth.land['url'])
fig, ax = plt.subplots(figsize=(12, 6))
world.plot(ax=ax, color='lightgrey')

for i, file_path in enumerate(file_paths):
    df = pd.read_csv(file_path, delimiter=',', low_memory=False)
    geometry = [Point(xy) for xy in zip(df['lng'], df['lat'])]
    gdf = GeoDataFrame(df, geometry=geometry)
    gdf.plot(ax=ax, 
             marker='o',
             markersize=0.001,
             color=colors[i % len(colors)],
             label=file_path.split('/')[-1])

plt.legend()
plt.show()
