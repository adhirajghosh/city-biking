import os
import time
import numpy as np
import geopandas

@lru_cache() #only load the data once, output of this function is saved, if it is called multiple times
def load_precinct_data():
    PRECINCTS_GJ = 'data/nyc/Police Precincts.geojson'

    with open(PRECINCTS_GJ) as f:
        precincts_gpd = gpd.read_file(f)
    return precincts_gpd

def get_precinct(lat, long):
    precinct_data = load_precinct_data()

    # this wants a list, and gives a list :shrug
    point = gpd.points_from_xy([long], [lat])[0]

    bool_mask = precinct_data['geometry'].contains(point)

    # from the precinct series, the values need to be grabbed, a list of length one, containing the int we want
    precinct = precinct_data[bool_mask]['precinct'].values[0]

    return precinct


