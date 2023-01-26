import os
import pandas as pd
import utils


def generate_ksi_df(path='data', save_csv=False):
    df14,df15,df16,df17,df18,df19 = [],[],[],[],[],[]


    for file in os.listdir(path):
        if file[:3] == 'KSI':
            df = pd.read_csv(path + '/' + file)
            if file[3:5] == '14':
                df['year'] = 2014
                df14.append(df)
            elif file[3:5] == '15':
                df['year'] = 2015
                df15.append(df)
            elif file[3:5] == '16':
                df['year'] = 2016
                df16.append(df)
            elif file[3:5] == '17':
                df['year'] = 2017
                df17.append(df)
            elif file[3:5] == '18':
                df['year'] = 2018
                df18.append(df)
            elif file[3:5] == '19':
                df['year'] = 2019
                df19.append(df)

    for count,i in enumerate([df14, df15, df16,df17,df18,df19]):
        i[1] = i[1].drop(columns=["injuries_car", "fatalities_car"])
        i[2] = i[2].drop(columns=["injuries_pedestrian", "fatalities_pedestrian"])

    df_main = pd.concat(df14).append(pd.concat(df15), ignore_index=True).append(pd.concat(df16), ignore_index=True).append(
        pd.concat(df17), ignore_index=True).append(pd.concat(df18), ignore_index=True).append(pd.concat(df19), ignore_index=True)
    df_main = df_main.sort_values(by=['precinct'])
    if save_csv:
        df_main.to_csv('data/ksi_nyc.csv', encoding='utf-8', index=False)
    return df_main

def concatenate_KSI_data():
    df14 = []
    df15 = []
    df16 = []

    path = 'data'

    for file in os.listdir(path):
        if file[:3] == 'KSI':
            df = pd.read_csv(path + '/' + file)
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

    df_main = pd.concat([df14,df15,df16])


    gj = utils.load_precinct_data()

    gj['injuries14'] = df14['injuries'].values
    gj['injuries15'] = df15['injuries'].values
    gj['injuries16'] = df16['injuries'].values
    gj.explore(column='injuries14', cmap='cividis')
    gj.explore(column='injuries15', cmap='cividis')
    gj.explore(column='injuries16', cmap='cividis')

    return df_main


