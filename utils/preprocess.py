from keras_preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from nltk.corpus import stopwords
import pandas as pd
import os
import nltk
import sys

nltk.download('stopwords')
nltk.download('punkt')


def removing_stop_words(texts):
    # Removing stop words
    stop_words = set(stopwords.words('spanish'))
    for i, text in enumerate(texts):
        tokens = nltk.word_tokenize(text)
        # print(tokens)
        sentence = [word for word in tokens if word not in stop_words]
        texts[i] = ' '.join(sentence)


def tokenizer(texts):
    max_nb_words = 2000
    tokenizer = Tokenizer(num_words=max_nb_words)
    tokenizer.fit_on_texts(texts)
    sequences_train = tokenizer.texts_to_sequences(texts)
    print(sequences_train)


if __name__ == "__main__":
    # texts = [
    #     'No nos gustó este lugar, la música era muy mala!',
    #     'Es básicamente para tragos y oír buena música',
    #     'Tuvimos la suerte de tener un buen bistec y langosta cena servida en una temperatura comestible',
    #     'Ya habíamos estado y de verdad siguen muy bien, la cena fue excelente'
    # ]

    removing_stop_words(sys.argv[0])
    tokenizer(sys.argv[0])
