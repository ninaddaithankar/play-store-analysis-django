import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def get_stats(dataset_name='DEMOAPP/Data/CleanedData.csv'):
    df = pd.read_csv(dataset_name)
    no_of_apps = len(df.index)
    avg_rating = round(df['Rating'].mean(), 1)
    min_version = list(df['Android Version'].value_counts().index)
    min_version = min_version[0]
    non_zero_price = df['Price'].to_numpy().nonzero()
    non_zero_price = len(non_zero_price[0])
    total = len(df.Price.index)
    non_zero_price_ratio = round(non_zero_price/total*100)
    zero_price_ratio = 100-non_zero_price_ratio
    stats = [no_of_apps, avg_rating, min_version, zero_price_ratio, non_zero_price_ratio]
    return stats


def get_choices(dataset_name='DEMOAPP/Data/CleanedData.csv'):
    le=LabelEncoder()

    df = pd.read_csv(dataset_name)
    category_choices = df['Category'].unique()
    content_choices = df['Content Rating'].unique()
    genre_choices = df['Genres'].unique()
    category_encoded = le.fit_transform(category_choices)
    content_encoded = le.fit_transform(content_choices)
    genre_encoded = le.fit_transform(genre_choices)
    category_tuples = zip(category_encoded, category_choices)
    genre_tuples = zip(genre_encoded,genre_choices)
    content_tuples = zip(content_encoded, content_choices)
    return category_tuples,content_tuples,genre_tuples


