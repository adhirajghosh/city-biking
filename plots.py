import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl


def plot_overview(df, groupby, save=False):
    fig, axs = plt.subplots(3)

    sns.scatterplot(y=df.groupby(groupby).sum().bike_count, x=df.groupby(groupby).sum().index, color='y', ax=axs[0])
    axs[0].legend(['bike count'])

    sns.scatterplot(y=df.groupby(groupby).sum().crashes, x=df.groupby(groupby).sum().index, color='y', ax=axs[1])
    sns.scatterplot(y=df.groupby(groupby).sum().injuries, x=df.groupby(groupby).sum().index, color='r', ax=axs[1])
    sns.scatterplot(y=df.groupby(groupby).sum().fatalities, x=df.groupby(groupby).sum().index, color='k', ax=axs[1])
    axs[1].legend(['absolute crashes', 'absolute injuries', 'absolute fatalities'])
    axs[1].set_ylabel('ksi count')

    sns.scatterplot(y=df.groupby(groupby).sum().crashes / df.groupby(groupby).sum().bike_count,
                    x=df.groupby(groupby).sum().index, color='y', ax=axs[2])
    sns.scatterplot(y=df.groupby(groupby).sum().injuries / df.groupby(groupby).sum().bike_count,
                    x=df.groupby(groupby).sum().index, color='r', ax=axs[2])
    sns.scatterplot(y=df.groupby(groupby).sum().fatalities / df.groupby(groupby).sum().bike_count,
                    x=df.groupby(groupby).sum().index, color='k', ax=axs[2])
    axs[2].legend(['relative crashes', 'relative injuries', 'relative fatalities'])
    axs[2].set_ylabel('relative ksi count')

    if save:
        plt.savefig('plot_overview.png')
    plt.show()


def plot_nlargest_nyc(df, precinct_data, column, n_largest, relative=False, save=False):
    if relative:
        precincts_max = pd.Series(
            df.groupby('precinct').sum().loc[:, column] / df.groupby('precinct').sum().bike_count).nlargest(
            n_largest).index
        label_max = str(n_largest) + ' precincts with highest relative ' + column
    else:
        precincts_max = df.groupby('precinct').sum().loc[:, column].nlargest(n_largest).index
        label_max = str(n_largest) + ' precincts with highest ' + column

    cmap = plt.cm.jet  # define the colormap
    # extract all colors from the .jet map
    cmaplist = [cmap(i) for i in range(cmap.N)]
    # force the first color entry to be grey
    cmaplist[-1] = (.5, .5, .5, 0.7)

    # create the new map
    cmap = mpl.colors.LinearSegmentedColormap.from_list(
        'Custom cmap', cmaplist, cmap.N)

    label = []
    for i in precinct_data.index:
        if i in list(map(str, precincts_max)):
            label.append(label_max)
        elif i in list(map(str, df.precinct)):
            label.append('Available precincts')
        else:
            label.append('No data')

    precinct_data.loc[:, 'labels'] = label

    if save:
        plt.savefig('plot_nlargest_nyc.png')

    precinct_data.plot(column='labels', legend=True, cmap=cmap)


def plot_nlargest(df, column, n_largest, relative=False, save=True):
    if relative:
        precincts_max = pd.Series(
            df.groupby('precinct').sum().loc[:, column] / df.groupby('precinct').sum().bike_count).nlargest(
            n_largest).index
    else:
        precincts_max = df.groupby('precinct').sum().loc[:, column].nlargest(n_largest).index

    fig, ax = plt.subplots(1)
    sns.scatterplot(y=df.loc[df.precinct.isin(precincts_max)].bike_count,
                    x=df.loc[df.precinct.isin(precincts_max)].year, color='b', ax=ax, label='bike_count')
    sns.scatterplot(y=df.loc[df.precinct.isin(precincts_max)].crashes, x=df.loc[df.precinct.isin(precincts_max)].year,
                    color='y', ax=ax, label='crashes')
    sns.scatterplot(y=df.loc[df.precinct.isin(precincts_max)].injuries, x=df.loc[df.precinct.isin(precincts_max)].year,
                    color='r', ax=ax, label='injuries')
    sns.scatterplot(y=df.loc[df.precinct.isin(precincts_max)].fatalities,
                    x=df.loc[df.precinct.isin(precincts_max)].year, color='k', ax=ax, label='fatalities')
    ax.set_ylabel('bike and ksi count')

    ax.legend()

    if save:
        plt.savefig('plot_nlarge.png')
    plt.show()