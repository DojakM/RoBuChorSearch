import streamlit as st
import pip
pip.main(["install", "openpyxl"])
st.sidebar.success("Wählt die Sichtweise")
st.text("Bitte benutzt die Wähloberfläche links")
