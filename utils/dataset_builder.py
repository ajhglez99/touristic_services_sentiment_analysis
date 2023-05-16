import numpy as np
import pandas as pd


def dataset_setup():
    df = pd.read_csv('./datasets/reviews.csv')
    
    df['Polarity'] = df.apply(lambda x: int(x['Rating'])/10, axis=1)
    
    # rearrange columns
    df_reorder = df[['Title', 'Opinion', 'Polarity', 'Attraction']]

    # save file
    writer = pd.ExcelWriter('./datasets/dataset.xlsx')
    df_reorder.to_excel(writer, index=False)
    writer.save()


def compare_rating_vs_polarity(df):
    # df = pd.read_csv('./datasets/dataset.csv')
    
    df['Compare'] = df.apply(
        lambda x: abs(int(x['Rating'])/10 - int(x['Polarity'])), axis=1)
    
    return df


if __name__ == "__main__":
    dataset_setup()
