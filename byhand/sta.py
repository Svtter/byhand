# coding: utf-8

import pandas as pd

def get_df():
    df = pd.read_csv('train.csv')
    print(df)

def check():
    df = pd.read_csv('train.csv')
    print(df['val_loss'].min())
    print(df['val_loss'].idxmin())


if __name__ == '__main__':
    check()
