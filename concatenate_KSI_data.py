import geopandas as gpd
import os
import pandas as pd
import utils
import matplotlib
import folium
import mapclassify



df14 = []
df15 = []
df16 = []

PATH = 'data'

for file in os.listdir(PATH):
    if file[:3] == 'KSI':
        df = pd.read_csv(PATH + '/' + file)
        if file[3:5] == '14':
            df14.append(df)
        elif file[3:5] == '15':
            df15.append(df)
        elif file[3:5] == '16':
            df16.append(df)

df14 = pd.concat(df14)[['injuries','precinct']]
df15 = pd.concat(df15)[['injuries','precinct']]
df16 = pd.concat(df16)[['injuries','precinct']]

df14 =df14.groupby("precinct").sum()
df15 =df15.groupby("precinct").sum()
df16 =df16.groupby("precinct").sum()

gj = utils.load_precinct_data()

gj['injuries14'] = df14['injuries'].values
gj['injuries15'] = df15['injuries'].values
gj['injuries16'] = df16['injuries'].values
gj.explore(column='injuries14', cmap='cividis')
gj.explore(column='injuries15', cmap='cividis')
gj.explore(column='injuries16', cmap='cividis')