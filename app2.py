import streamlit as st
import pandas as pd
import numpy as np

# Charger le CSV depuis l’URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df = pd.read_csv(url)

# Sidebar
st.title("Bienvenue sur le site web de Priscilla")

# Liste déroulante des boroughs
borough = st.selectbox(
    "Indiquez votre arrondissement de récuprération  :",
    df["pickup_borough"].dropna().unique()
)

st.write("Tu as choisi :", borough)

# Dictionnaire Borough -> Image
images = {
    "Manhattan": "https://www.new-york-city.fr/wp-content/uploads/2020/11/Manahttan_principale-1024x768.jpg.webp",
    "Queens": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/d4/88/9a/caption.jpg?w=600&h=500&s=1",
    "Brooklyn": "https://we-love-new-york.com/wp-content/uploads/2024/02/prospect-heights-new-york.jpg",
    "Bronx": "https://decouvrir-new-york.fr/wp-content/uploads/2024/05/bronx-new-york-1024x683.jpg",
    "nan": "https://upload.wikimedia.org/wikipedia/commons/2/20/Point_d_interrogation.jpg"
}


# Afficher l'image correspondant
st.image(images[borough], width=800)

#filtered_df = df[df["pickup_borough"] == borough]

#st.dataframe(filtered_df.head())








