# coding: utf-8

import pandas as pd

def check():
    df = pd.read_csv('train.csv')
    print(df['val_loss'].min())
    print(df['val_loss'].idxmin())
