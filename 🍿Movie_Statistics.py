import streamlit as st
import pandas as pd

df = pd.read_feather("clean_df.feather")

print(df.head())
st.set_page_config(page_title="Movie Statistics", page_icon="🍿")

with st.sidebar:
    st.title("Netflix Original Films & IMDb Scores")

    st.write("""
    **Explore Netflix data with an understanding of summary statistics**
    
    You can:
    - Interpret summary statistics in context
    - Make choices about which summary statistics are appropriate based on the situation
    """)

st.write("# Movie Statistics 🍿")

st.header("Explore Netflix data with an understanding of summary statistics", divider="rainbow")

st.write("""
### Explore data about films and documentaries produced by Netflix. 
The dataset used is a modified version of one found on the website Kaggle. 
Your dataset includes 503 films with the following variables:

| Syntax | Description |
| ----------- | ----------- |
| Title | title of the film |
| Genre | genre of the film |
| Language | primary language of the film |
| Year | year the film premiered |
| Runtime | length of the film in minutes |
| Score | film rating of 1 to 10 (worst to best) from the IMDb website
""")
