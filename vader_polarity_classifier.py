from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


def clean_data(df):
    """Remove NaN values and empty strings"""
    df.dropna(inplace=True)
    df.drop_duplicates(subset=None, inplace=True)

    blanks = []  # start with an empty list

    for i, date, rating, title, opinion, attraction in df.itertuples():
        if type(opinion) == str:
            if opinion.isspace():
                blanks.append(i)

    df.drop(blanks, inplace=True)


def class_asigner(values):
    """Asign a class between 1 and 5 to each value"""
    class_list = []

    for value in values:
        class_value = round(value * 2.4999) + 3
        class_list.append(class_value)

    return class_list


def dataset_setup():
    """Preprosess the dataset for Rest_mex_DL_EDA algorithm"""

    sid = SentimentIntensityAnalyzer()
    df = pd.read_csv('./datasets/reviews.csv')

    clean_data(df)

    # calculate polarity
    df['Full Opinion'] = df.Title + ' ' + df.Opinion
    df['Score'] = df['Full Opinion'].apply(
        lambda opinion: sid.polarity_scores(opinion))
    df['Compound'] = df['Score'].apply(
        lambda score_dict: score_dict['compound'])
    df['Polarity'] = class_asigner(df['Compound'])

    df.to_csv('./datasets/dataset_vader.csv', index=False)

    # # sort columns
    # df_reorder = df[['Title', 'Opinion', 'Polarity', 'Attraction']]

    # # save file
    # writer = pd.ExcelWriter('./datasets/dataset.xlsx')
    # df_reorder.to_excel(writer, index = False)
    # writer.save()


if __name__ == "__main__":
    dataset_setup()
