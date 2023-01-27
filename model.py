import pandas as pd
import matplotlib.pyplot as plt
from patsy import dmatrices
import statsmodels.api as sm
from utils import *
import numpy as np
from sklearn.metrics import mean_squared_error


def train_test_set_year(df):
    mask = np.ones(len(df), dtype=bool)
    mask[5::6] = False

    df_train = df[mask]
    df_test = df[~mask]
    print('Training data set length='+str(len(df_train)))
    print('Testing data set length='+str(len(df_test)))
    expr = """injuries ~ year + precinct + crashes+ bike_count"""
    y_train, X_train = dmatrices(expr, df_train, return_type='dataframe')
    y_test, X_test = dmatrices(expr, df_test, return_type='dataframe')
    X_train = X_train.drop(columns=['Intercept'])
    X_test = X_test.drop(columns=['Intercept'])
    return X_train, y_train, X_test, y_test

def train_test_zeroshot(df, train_size=0.8):
    count  = int(train_size*len(df))
    while(True):
        if df['precinct'][count-1]!= df['precinct'][count]:
            break
        else:
            count = count-1
    mask = np.zeros(len(df), dtype=bool)
    mask[0:count] = True

    df_train = df[mask]
    df_test = df[~mask]
    print('Training data set length='+str(len(df_train)))
    print('Testing data set length='+str(len(df_test)))
    expr = """injuries ~ year + precinct + crashes+ bike_count"""
    y_train, X_train = dmatrices(expr, df_train, return_type='dataframe')
    y_test, X_test = dmatrices(expr, df_test, return_type='dataframe')
    X_train = X_train.drop(columns=['Intercept'])
    X_test = X_test.drop(columns=['Intercept'])
    return X_train, y_train, X_test, y_test


def poisson_train_predict(X_train, y_train, X_test, print_summary=True):
    poisson_training_results = sm.GLM(y_train, X_train, family=sm.families.Poisson()).fit()
    poisson_predictions = poisson_training_results.get_prediction(X_test)
    predictions_summary_frame = poisson_predictions.summary_frame()
    if print_summary:
        print(poisson_training_results.summary())
        print(predictions_summary_frame)
    return predictions_summary_frame


def pred_analysis(predictions_summary_frame, X_test, y_test, if_rms=True):
    predicted_counts = predictions_summary_frame['mean']
    actual_counts = y_test['injuries']
    fig = plt.figure()
    fig.suptitle('Predicted versus actual injuries')
    predicted, = plt.plot(X_test.precinct, predicted_counts, 'go-', label='Predicted injuries')
    actual, = plt.plot(X_test.precinct, actual_counts, 'ro-', label='Actual injuries')
    plt.legend(handles=[predicted, actual])
    plt.show()
    plt.clf()
    fig = plt.figure()
    fig.suptitle('Scatter plot of Actual versus Predicted counts')
    plt.scatter(x=predicted_counts, y=actual_counts, marker='.')
    plt.xlabel('Predicted counts')
    plt.ylabel('Actual counts')
    plt.show()
    if if_rms:
        rms = np.sqrt(mean_squared_error(y_test['injuries'], predicted_counts))
        return rms


def train_pred_individual(X_train, y_train, X_test, y_test, if_rms=True):
    preds = []
    for i in range(1, len(y_test) + 1):
        poisson_training_results = sm.GLM(y_train[0:i * 5], X_train[0:i * 5], family=sm.families.Poisson()).fit()

        poisson_predictions = poisson_training_results.get_prediction(X_test[i - 1:i])

        predictions_summary_frame = poisson_predictions.summary_frame()['mean']
        preds.append(predictions_summary_frame)
    predicted_counts = preds
    actual_counts = y_test['injuries']
    fig = plt.figure()
    fig.suptitle('Predicted versus actual injuries')
    predicted, = plt.plot(X_test.precinct, predicted_counts, 'go-', label='Predicted injuries')
    actual, = plt.plot(X_test.precinct, actual_counts, 'ro-', label='Actual injuries')
    plt.legend(handles=[predicted, actual])
    plt.show()
    plt.clf()
    fig = plt.figure()
    fig.suptitle('Scatter plot of Actual versus Predicted counts')
    plt.scatter(x=predicted_counts, y=actual_counts, marker='.')
    plt.xlabel('Predicted counts')
    plt.ylabel('Actual counts')
    plt.show()

    preds_df = pd.concat(preds)
    diff_df = (np.abs(preds_df - y_test['injuries']))
    y_test['predictions'] = preds_df
    y_test['diff'] = diff_df
    if if_rms:
        rms = np.sqrt(mean_squared_error(y_test['injuries'], predicted_counts))
        return y_test, rms
    else:
        return y_test