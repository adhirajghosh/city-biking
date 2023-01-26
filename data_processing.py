import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline
import pickle

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

        bike_counts = np.vstack([bike_counts, counts/2])

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