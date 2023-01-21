import os
import time
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
            return 'The following Point is not in any police precinct: ' + str(point)
        precincts.append(precinct_data[bool_mask].index[0])

    return precincts