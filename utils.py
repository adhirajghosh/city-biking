import os
import time
import pandas as pd
import numpy as np
import geopandas as gpd
from functools import lru_cache

@lru_cache() #only load the data once, output of this function is saved, if it is called multiple times
def load_precinct_data():
    '''
    returns a geopandas geodataframe with the Precincts as index.
    there are 77 precincts, but the ids go up to 123.
    '''
    PRECINCTS_GJ = 'data/nyc/Police Precincts.geojson'

    with open(PRECINCTS_GJ) as f:
        precincts_gpd = gpd.read_file(f)
    precincts_gpd = precincts_gpd.set_index("precinct")
    return precincts_gpd

def get_precinct_id(lat, long):
    '''
    this takes a list of latitudes and a list of longitudes
    returns a list of precinctIDs

    returns a string, if any coordinate pair is not in any precinct
    '''
    precinct_data = load_precinct_data()


    points = gpd.points_from_xy(long, lat)
    precincts = []

    for point in points:
        bool_mask = precinct_data['geometry'].contains(point)
        if not sum(bool_mask) == 1:
            precincts.append(-1)
        else:
            precincts.append(precinct_data[bool_mask].index[0])

    return precincts


def int_to_color(rgbint):
    return (rgbint // 256 // 256 % 256, rgbint // 256 % 256, rgbint % 256, 0)


def make_array(string, length):
    '''
    Convert Strings to arrays
    '''
    return np.array(string.split(" ")).reshape((-1, length))

def unify_into_df(borough_strings, columns):
    '''
    Creates a dataframe out of all the data
    '''
    return pd.DataFrame([
        *make_array(borough_strings[0], len(columns)),
        *make_array(borough_strings[1], len(columns)),
        *make_array(borough_strings[2], len(columns)),
        *make_array(borough_strings[3], len(columns)),
        *make_array(borough_strings[4], len(columns))],
        columns=columns)
