import streamlit as st
import pandas as pd
def load_excel(file):
    df = pd.read_excel(file)
    return df

st.set_page_config(layout="wide")
st.title("Buchliste")
noneCheck = st.file_uploader("Hierhin die Excel ziehen:", type=([".xlsx"]))
filter_buch = st.sidebar.text_input("Buchsuche")

if noneCheck is not None:
    table = load_excel(noneCheck)
    if "Nochmal anschauen" in table.columns:
        table.drop(["Nochmal anschauen"], axis=1, inplace=True)
    curr_tab = table[table["Titel"].str.contains(filter_buch, regex=False)]
    st.dataframe(curr_tab)

