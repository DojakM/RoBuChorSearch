import pandas as pd
import streamlit as st
import re
from stvis import pv_static

import load_files


def generateInterface():
    st.title("Rottenburg Posaunenchor")
    st.dataframe()

if __name__ == '__main__':
    noneCheck = st.file_uploader("Hierhin die Excel ziehen:", type=([".xlsx"]))
    try:
        load_files.load_excel(noneCheck)
    except:
        st.text("Bitte gebe die richtige Exceltabelle ein")
    if noneCheck is not None:
        generateInterface()