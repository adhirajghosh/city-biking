import os
import sys
import time
import datetime
import os.path as osp
from geopandas.tools import sjoin
import pandas as pd
import numpy as np
import warnings
from torch.utils.data import Dataset
from utils import *


def pickleCitibikeDataset():
    precinct_data = load_precinct_data()
    precinct_data = precinct_data.drop(columns=['shape_area', 'shape_leng'])

    df_columns = ['startstation_latitude', 'startstation_longitude', 'endstation_latitude', 'endstation_longitude']
    all_dfs = {}

    path = "data/"
    if not os.path.isfile(path + "citi-data.pkl"):
        for file in os.listdir(path):
            year = file[:4]

            if file[4] == '-':
                month = file[5:7]
            else:
                month = file[4:6]

            if year.isnumeric() and int(year) < 2020:
                df = pd.read_csv(path + file)

                # select only certain columns
                data_columns = df.columns.to_numpy()[[5, 6, 9, 10]].tolist()
                df = df.loc[:, data_columns]
                df.columns = df_columns

                geometry = gpd.points_from_xy(df.startstation_longitude.to_numpy(), df.startstation_latitude.to_numpy())
                df = gpd.GeoDataFrame(df, crs='epsg:4326', geometry=geometry)

                df = sjoin(df, precinct_data, how='left')
                df = df.rename(columns={'index_right': 'start_precinct_id'})
                df = df.drop(columns=['startstation_longitude', 'startstation_latitude', 'geometry'])

                geometry = gpd.points_from_xy(df.endstation_longitude.to_numpy(), df.endstation_latitude.to_numpy())
                df = gpd.GeoDataFrame(df, crs='epsg:4326', geometry=geometry)

                df = sjoin(df, precinct_data, how='left')
                df = df.rename(columns={'index_right': 'end_precinct_id'})
                df = df.drop(columns=['endstation_longitude', 'endstation_latitude', 'geometry'])

                all_dfs[year + '-' + month] = df.copy()

      pickle.dump(all_dfs, open('citibike_data.pkl', 'wb'))  
    

def getCitibikeDataset(file='citibike_data.pkl):
    return pickle.load(file)
