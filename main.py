import streamlit as st
import load_files


def generateInterface():
    st.title("Rottenburg Posaunenchor")
    st.dataframe()

if __name__ == '__main__':
    noneCheck = st.file_uploader("Hierhin die Excel ziehen:", type=([".xlsx"]))
    warn = st.text("")
    try:
        file = load_files.load_excel(noneCheck)
    except:
        warn.text("Bitte gebe die richtige Exceltabelle ein")
    if noneCheck is not None:
        warn.text("")
        generateInterface()