import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_graph(dataset_name='DEMOAPP/Data/CleanedData.csv'):
    df = pd.read_csv(dataset_name)

#Category front graph

    plt.figure(figsize=(30, 10))
    fig=sns.set_style({'axes.spines.top':False,'axes.spines.right': False,'axes.spines.left': False,'axes.spines.bottom': False,'font.family': 'frutiger'})
    fig = sns.countplot(x=df['Category'], palette="hls")
    plt.tick_params(labelcolor='white')
    plt.yticks(fontsize=15)
    fig.set_xticklabels(fig.get_xticklabels(), rotation=90, fontsize=18)
    fig.set_ylabel('Frequency', color='white', fontsize=35)
    fig.grid(False)
    plt.savefig('DEMOAPP/static/images/graphs/categoryHistogram.png', transparent=True, pad_inches=0, bbox_inches='tight')

#Android Version vs Rating Scatter

    plt.figure(figsize=(12, 10))
    scatterfig=sns.set()
    scatterfig = sns.set_style(
        {'axes.spines.top': False, 'axes.spines.right': False, 'axes.spines.left': False, 'axes.spines.bottom': False})
    scatterfig = sns.scatterplot(x='Android Version', y='Rating',color = 'purple',data=df)
    plt.tick_params(labelcolor='white',labelsize=15)
    scatterfig.set_ylabel('Rating', color='white', fontsize=30)
    scatterfig.set_xlabel('Android Version', color='white',fontsize=30)
    scatterfig.grid(False)
    plt.title('Android Version vs Rating',color='white',fontsize=35,pad=20)

    plt.savefig('DEMOAPP/static/images/graphs/androidRatingScatter.png', transparent=True, pad_inches=0, bbox_inches= 'tight' )


#Ratings Histogram Graph

    plt.figure(figsize=(12, 11))
    g = sns.set_style(
        {'axes.spines.left': False, 'axes.spines.right': False, 'axes.spines.top': False, 'axes.spines.bottom': False})
    g = sns.kdeplot(df.Rating, color='#CCFF99', shade=True)

    #g.set_xlabel('Ratings', color='white', fontsize=25, labelpad=20)
    plt.title('Ratings Histogram', color='white', fontsize=45, pad=20)
    plt.legend(fontsize=20)
    g.set_xticklabels(labels=['0', '1', '2', '3', '4', '5'], color='white', fontsize=20)
    g.set_yticklabels(labels=['0.0', '0.2', '0.4', '0.6', '0.8', '1.0', '1.2'], color='white', fontsize=15)
    g.grid(False)

    plt.savefig('DEMOAPP/static/images/graphs/ratingHistogram.png', transparent=True, pad_inches=0, bbox_inches='tight')

#PIECHART

    plt.figure(figsize=(10,11))
    my_circle=plt.Circle( (0,0), 0.7, color = '#051116')
    ax=df['Content Rating'].value_counts().plot(kind='pie',fontsize=12,labels=None,wedgeprops={"edgecolor":(0.10,0.10,0.15),'linewidth': 1, 'linestyle': '-', 'antialiased': True},colors = ['yellowgreen',(0.68,0.31,1),'gold', 'lightskyblue', 'lightcoral'])

    labels=['Everyone', 'Teen', 'Everyone 10', 'Mature', 'Adults only 18','Unrated']
    plt.legend(labels, loc='best',fontsize = 'medium')

    plt.axis('off')
    plt.title('Content Rating',fontsize=40,color = 'white',pad=20)
    p=plt.gcf()
    p.gca().add_artist(my_circle)

    plt.savefig('DEMOAPP/static/images/graphs/contentRatingPie.png', transparent=True,pad_inches=0,bbox_inches='tight')

#Category vs Price

    plt.figure(figsize=(13, 11))
    ax = df.groupby('Category')['Price'].mean().nlargest(10).sort_values().plot('bar', width=0.6, color='#E179CC',
                                                                                fontsize=17)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax1 = plt.axes()
    x_axis = ax1.xaxis
    x_axis.set_label_text('foo')
    x_axis.label.set_visible(False)
    plt.title('Price vs Category', color='white', fontsize=50,pad=0)
    ax.grid(False)
    plt.savefig('DEMOAPP/static/images/graphs/categoryPriceBar.png', transparent=True,pad_inches=0,bbox_inches='tight')

#Genre vs Installs Line

    plt.figure(figsize=(25, 7))
    ax = sns.set_style(
        {'axes.spines.left': False, 'axes.spines.right': False, 'axes.spines.top': False, 'axes.spines.bottom': False})
    ax = df.groupby('Genres')['Installs'].sum().nlargest(10).sort_values().plot('line', color='gold', fontsize=20,
                                                                                linewidth=5)
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=20, color='white')
    plt.tick_params(labelcolor='white')
    plt.title('Genres vs Installs', color='white', fontsize=35)
    plt.xlabel('Genres', color='#051116')
    plt.ylabel('Installs', color='white', fontsize=20)
    ax.grid(False)
    plt.savefig('DEMOAPP/static/images/graphs/genreInstallsLine.png', transparent=True, bbox_inches='tight')

#Android Version Histogram Density

    plt.figure(figsize=(12, 10))
   # value = df['Android Version'].value_counts()
    line2 = sns.kdeplot(df['Android Version'],
        color='#39EFFF',shade=True)
    plt.legend(fontsize=15)
    plt.tick_params(labelcolor='white', labelsize=15)
    plt.xlabel('Android Version', color='white', fontsize=25)
    plt.ylabel('Frequency', color='white', fontsize=20)
    plt.title('Android Version Frequency', color='white', fontsize=35,pad=10)
    plt.grid(False)
    plt.savefig('DEMOAPP/static/images/graphs/androidHistogramLine.png', transparent=True, pad_inches=0, bbox_inches='tight')
