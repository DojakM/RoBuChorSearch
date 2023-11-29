import streamlit as st
import pandas as pd

def load_standard():
    df = pd.read_pickle("./df.pkl")
    return df

st.set_page_config(layout="wide")
st.title("Liederliste")
vz_list = ["6#","5#","4#","3#","2#","1#","0","1b","2b","3b","4b","5b","6b"]
tabelle = load_standard()
ros = st.sidebar.radio("Ansicht", ["Volle", "Mit Buch", "Ohne Buch"])
filter_buch = st.sidebar.text_input("Buchsuche")
filter_lied = st.sidebar.text_input("Liedersuche")
isToggled = st.sidebar.toggle("Vorzeichenfilter")
values = st.sidebar.slider("Vorzeichen", -6, 6, [0,0])
vz = tabelle["Vorzeichen"]
vz_dict = {}
iter = -6
for i in vz_list:
    vz_dict.update({i: iter})
    iter+=1
mask = vz.isin(vz_list)
omask = ~mask
tab = vz[mask].map(vz_dict)

if ros=="Volle":
    curr_tab = tabelle
    curr_tab = curr_tab[curr_tab["Buchtitel"].str.contains(filter_buch, regex=False)]
    curr_tab = curr_tab[curr_tab["Liedtitel"].str.contains(filter_lied, regex=False)]
    if isToggled:
        masker = (tab>=values[0])&(tab<=values[1])
        curr_tab = curr_tab[masker&mask]
    st.dataframe(curr_tab)
elif ros == "Mit Buch":
    curr_tab = tabelle[tabelle.columns.difference(["Verlag", "Verlagsnummer", "Autor", "Herausgeber", "Jahr",
                                                     "GEMA"])]
    curr_tab = curr_tab[curr_tab["Buchtitel"].str.contains(filter_buch, regex=False)]
    curr_tab = curr_tab[curr_tab["Liedtitel"].str.contains(filter_lied, regex=False)]
    if isToggled:
        masker = (tab >= values[0]) & (tab <= values[1])
        curr_tab = curr_tab[masker & mask]
    st.dataframe(curr_tab)
else:
    curr_tab = tabelle.iloc[:,-5:-1]
    curr_tab = curr_tab[curr_tab["Liedtitel"].str.contains(filter_lied, regex=False)]
    if isToggled:
        masker = (tab >= values[0]) & (tab <= values[1])
        mask = masker | omask
        curr_tab = curr_tab[mask]
    st.dataframe(curr_tab)

