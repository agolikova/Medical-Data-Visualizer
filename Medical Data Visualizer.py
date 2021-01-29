import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Import data using pandas.csv (reads comma-separated values (csv) file into DataFrame)
df = pd.read_csv('medical_examination.csv')

#Add 'overweight' column, set values as 0 or 1 by calculating BMI
df['Overweight'] = (df['Weight'] / (df['Height']/100)**2).apply(lambda x: 1 if x > 25 else 0)

#Normalize data by making 0 always good & 1 always bad. If value of 'cholesterol' or 'gluc' = 1, make the value 0. If value > 1, make the value 1
df['Cholesterol'] = df['Cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['Glucose'] = df['Glucose'].apply(lambda x: 0 if x == 1 else 1)

def draw_cat_plot():
    """Returns & saves categorical plot showing outcomes for patient variables depending on presence/absence of cardiovascular disease"""

    #Create DataFrame for cat plot using values from 'Cholesterol', 'Glucose', 'Smoking', 'Alcohol', 'Active', & 'Overweight'
    #Group and reformat data to split it by 'CVD'. Show counts of each feature
    #pandas.melt() function reformats DataFrame so ≥1 columns are identifier variables (id_vars), all other columns are measured variables (value_vars) & unpivoted to row axis, leaving 2 non-identifier columns (‘variable’ & ‘value’)
    df_cat = pd.melt(df, var_name = 'variable', value_vars = ['Active','Alcohol','Cholesterol', 'Glucose','Overweight','Smoking'], id_vars = 'CVD')

    #Draw catplot with 'sns.catplot()' - interface for drawing categorical plots onto FacetGrid
    sns.set_style("whitegrid")
    g = sns.catplot(data=df_cat, kind="count", x="variable", hue="value", col="CVD", height=6.5).set_axis_labels("Variable", "Total")
    g.set(ylim=(0, 35000))
    g.tight_layout()

    fig = g.fig
    fig.savefig('catplot.png')

    return fig

def draw_heat_map():
    """Returns & saves heatmap showing correlation between patient variables"""

    #Clean data by filtering out specified patient segments that represent incorrect data
    df_heat = df[(df['Diastolic BP'] <= df['Systolic BP']) &
                 (df['Height'] >= df['Height'].quantile(0.025)) &
                 (df['Height'] <= df['Height'].quantile(0.975)) &
                 (df['Weight'] >= df['Weight'].quantile(0.025)) &
                 (df['Weight'] <= df['Weight'].quantile(0.965))
    ]

    del df_heat['ID']

    #pandas.DataFrame.corr() computes pairwise correlation of columns, returning correlation matrix
    corr = df_heat.corr()

    #Generate mask for upper triangle of array
    #numpy.triu() returns copy of matrix with elements below 0th diagonal zeroed
    mask = np.triu(corr)

    #Set up matplotlib figure & subplots using matplotlib.pyplot.subplots(), returns fig & ax
    fig, ax = plt.subplots(figsize = (9,7))

    #Draw heatmap with 'sns.heatmap()' - function used to plot rectangular data as colour-encoded matrix
    #Parameters used: dataset, mask: cells with missing values masked, fmt: str formatting code used when adding annotations, vmax:value to anchor colourmap, linewidths: width of lines dividing each cell,
    #square: if True sets Axes aspect to equal so cells square-shaped, cbar_kws: keyword arguments for matplotlib.figure.Figure.colorbar(), annot: if True writes data value in each cell, center: value at which colourmap centered
    sns.heatmap(corr, mask=mask, fmt='.2f', vmax =.35, linewidths=.5, square=True, cbar_kws={'shrink':0.5}, annot=True, center=0)

    fig.tight_layout()
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()
