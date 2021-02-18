import os
import pandas as pd


def read_predcsv(pred_path):
    return pd.read_csv(pred_path)



if __name__=="__main__":
    pred_path = "Data/transfer_01_predictions.csv"
    df = read_predcsv(pred_path)
    print(df.head())
