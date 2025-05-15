import os
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

bdir = os.path.dirname(__file__)
df=pd.read_csv(os.path.join(bdir, "", "india.csv"), sep=',')
newdf=df

st.set_page_config(layout="wide")

states=list(newdf['State'].unique())
states.insert(0, "Global en Inde")
st.sidebar.title("Visualisation de la population indienne")

state_select=st.sidebar.selectbox("Selectionnez un état", states)
primary=st.sidebar.selectbox("Sélectionnez le paramètre primaire", sorted(list(newdf.columns[5:])))
secondary=st.sidebar.selectbox("Sélectionnez le paramètre secondaire", sorted(list(newdf.columns[5:])))
plot=st.sidebar.button("Afficher le graphe")

if plot:
    st.text("La taille représente le paramètre primaire")
    st.text("La couleur représente le paramètre secondaire")
    lg=newdf
    if state_select!="Global en Inde": lg=newdf[newdf['State']==state_select]
    fig=px.scatter_geo(lg, lat="Latitude", lon="Longitude", size=primary, color=secondary, projection="natural earth", width=1200, height=700, hover_name="District")
    st.plotly_chart(fig, use_container_width=True)
