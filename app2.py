import os
import importlib
import subprocess
import sys
import numpy as np
import pandas as pd
import streamlit as st

def install_and_import(package_name, import_name=None):
    module_name = import_name or package_name
    try:
        return importlib.import_module(module_name)
    except ImportError:
        print(f"Le module '{module_name}' n'est pas installé. Installation en cours...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        return importlib.import_module(module_name)
        
px = install_and_import("plotly-express", import_name="plotly.express")
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
    if state_select=="Global en Inde":
        fig=px.scatter_mapbox(newdf, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4, size_max=35, mapbox_style="carto-positron", width=1200, height=700, hover_name="District")
        st.plotly_chart(fig, use_container_width=True)
    else:
        fig = px.scatter_mapbox(newdf[newdf['State']==state_select], lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,
                                size_max=35, mapbox_style="carto-positron", width=1200, height=700,
                                hover_name="District")
        st.plotly_chart(fig, use_container_width=True)
