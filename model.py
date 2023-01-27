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


def poisson_train_predict(X_train, y_train, X_test, print_summary=True):
    poisson_training_results = sm.GLM(y_train, X_train, family=sm.families.Poisson()).fit()
    poisson_predictions = poisson_training_results.get_prediction(X_test)
    predictions_summary_frame = poisson_predictions.summary_frame()
    if print_summary:
        print(poisson_training_results.summary())
        print(predictions_summary_frame)
    return predictions_summary_frame


def pred_analysis(predictions_summary_frame, y_test):
    predicted_counts = predictions_summary_frame['mean']
    actual_counts = y_test['injuries']
    fig = plt.figure()
    fig.suptitle('Predicted versus actual injuries')
    predicted, = plt.plot(X_test.precinct, predicted_counts, 'go-', label='Predicted injuries')
    actual, = plt.plot(X_test.precinct, actual_counts, 'ro-', label='Actual injuries')
    plt.legend(handles=[predicted, actual])
    plt.show()
    rms = np.sqrt(mean_squared_error(y_test['injuries'], predicted_counts))
    return rms


def train_pred_individual(X_train, y_train, X_test, y_test):
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
    rms = np.sqrt(mean_squared_error(y_test['injuries'], predicted_counts))
    preds_df = pd.concat(preds)
    diff_df = (np.abs(preds_df - y_test['injuries']))
    y_test['predictions'] = preds_df
    y_test['diff'] = diff_df
    return y_test, rms
