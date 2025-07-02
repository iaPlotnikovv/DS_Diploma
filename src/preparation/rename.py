import pandas as pd
def rename_cols(df):
    """Переименовывает колонки в англ. компактный вид"""
    cols = df.columns
    new_cols = ["Experiment","Layer","TS","WFS","Amp","FreQ","e","h","Optimal"]
    
    return df.rename(columns=dict(zip(cols,new_cols)))