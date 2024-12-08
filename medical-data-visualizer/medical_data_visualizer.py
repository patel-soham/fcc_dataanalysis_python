import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
#df['overweight'] = np.where((df['weight'] / (df['height'] / 100)**2) > 25, 1, 0) 
df['overweight'] = ((df['weight'] / (df['height'] / 100)**2) > 25).astype('int8')

# 3
#df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
#df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)
df['cholesterol'] = (df['cholesterol'] > 1).astype('int8')
df['gluc'] = (df['gluc'] > 1).astype('int8')

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    cat = ['cardio', 'variable', 'value']

    # 6
    df_cat = df_cat.groupby(cat).size().reset_index().rename(columns={0:'total'})

    # 7
    plot = sns.catplot(df_cat, x='variable', y='total', col='cardio', kind='bar', hue='value')

    # 8
    fig = plot.figure

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    conditions = ((df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & \
        (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & \
            (df['weight'] <= df['weight'].quantile(0.975)))
    df_heat = df[conditions]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))
    print(mask.shape, corr.shape)

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='0.1f')


    # 16
    fig.savefig('heatmap.png')
    return fig
