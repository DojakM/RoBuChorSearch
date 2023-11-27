import pandas as pd
import openpyxl

def load_standard():
    df = pd.read_pickle("./df.pkl")
    return df

def load_excel(file):
    df = pd.read_excel(file)
    return df