import os
import sys
import time
import datetime
import os.path as osp
from geopandas.tools import sjoin
import pickle
import pandas as pd
import numpy as np
import warnings
from utils import *

all_precincts = ['1', '5', '6', '7', '9', '10', '13', '14', '17', '18', '19', '20', '22',
                 '23', '24', '25', '26', '28', '30', '32', '33', '34', '40', '41', '42',
                 '43', '44', '45', '46', '47', '48', '49', '50', '52', '60', '61', '62',
                 '63', '66', '67', '68', '69', '70', '71', '72', '73', '75', '76', '77',
                 '78', '79', '81', '83', '84', '88', '90', '94', '100', '101', '102',
                 '103', '104', '105', '106', '107', '108', '109', '110', '111', '112',
                 '113', '114', '115', '120', '121', '122', '123']


def processCitibikeDataset(file='data/all_dfs.pkl'):
    all_dfs = pickle.load(open(file, 'rb'))

    bike_counts = np.zeros(shape=len(all_precincts), dtype='int64')

    for key in list(all_dfs.keys()):
        all_dfs[key] = all_dfs[key].loc[np.all(all_dfs[key].notna(), axis=1)]
        unique_precincts, counts = np.unique(all_dfs[key], return_counts=True)
        counts = counts[np.argsort(list(map(int, list(unique_precincts))))]

        diff = list(map(int, list(set(all_precincts) - set(unique_precincts))))
        diff.sort()
        diff = list(map(str, diff))

        for precinct in diff:
            idx = all_precincts.index(precinct)
            counts = np.insert(counts, idx, 0)

        bike_counts = np.vstack([bike_counts, counts / 2])

    bike_counts = bike_counts[1:]

    df = pd.DataFrame(bike_counts, columns=all_precincts)

    keys = ['201' + str(Y) + '-' + str(M).rjust(2, '0') for Y in range(4, 10) for M in range(1, 13)]
    df.index = list(all_dfs.keys())
    diff = list(set(keys) - set(all_dfs.keys()))
    diff.sort()

    for key in diff:
        aux = np.empty(shape=len(all_precincts))
        aux[:] = np.NaN
        df.loc[key] = aux.copy()

    df = df.sort_index()
    df.index = pd.DatetimeIndex(df.index)

    for column in df.columns:
        df.loc[:, column] = df.loc[:, column].interpolate(method='polynomial', order=5)

    return df

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
