import streamlit as st
import pandas as pd

st.title("Cartographie RGPD des traitements")
df = pd.read_csv("../data/traitements.csv")
st.write("Voici l'ensemble des traitements collectés:")
st.dataframe(df)

st.subheader("Traitements non conformes (PIA Non ou Hors UE)")
non_conformes = df[(df["PIA"] != "Oui") | (df["Localisation"] != "France")]
st.dataframe(non_conformes)
