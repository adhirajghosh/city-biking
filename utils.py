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
    precinct_data = load_precinct_data()

    # this wants a list, and gives a list :shrug
    point = gpd.points_from_xy([long], [lat])[0]

    bool_mask = precinct_data['geometry'].contains(point)

    precinct = precinct_data[bool_mask].index[0]

    return precinct