import os
import pandas as pd
import shutil
def read_predcsv(pred_path):
    return pd.read_csv(pred_path)


def move_file(filenames,root_dir,new_dir,sub_folder_name):
    save_dir = new_dir+sub_folder_name
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for file in filenames:
        start_path = root_dir+file
        end_path = save_dir+file
        shutil.move(start_path,end_path)

if __name__=="__main__":
    pred_path = "Data/transfer_01_predictions.csv"
    df = read_predcsv(pred_path)
    ones = df[df["[Birds]Vs[EverythingElse]_Prediction"]==1]["wav_file"]
    zs = df[df["[Birds]Vs[EverythingElse]_Prediction"]==0]["wav_file"]
    move_file(ones,"Data/Transfer_01_split/","Segregated_Sounds/","1/")
    move_file(zs, "Data/Transfer_01_split/", "Segregated_Sounds/", "0/")



