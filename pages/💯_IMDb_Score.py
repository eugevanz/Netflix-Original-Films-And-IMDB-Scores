import streamlit as st

st.set_page_config(page_title="IMDB Score", page_icon="💯")

with st.sidebar:
    st.write("""
    **Distribution of IMDb scores**
    
    With this mostly symmetrical distribution, the values are distributed evenly around the mean, but a slight positive 
    skew indicates that there are a few lower values pulling the tail of the distribution to the left. With a standard 
    deviation of $$1.0$$, most data points are within 1 unit of the mean, indicating relatively low variability. The 
    frequency range from about $$1$$ to approximately $$75$$ suggests a wide spread of occurrence for different values 
    within this distribution.
    """)

st.write("# IMDB Score 💯")

st.header("Distribution of IMDb scores", divider="rainbow")

st.write("""
The distribution of IMDb scores is mostly symmetrical in a bell shape, indicating a normal distribution. There are a 
couple of very low scores, but they are not far from the rest of the distribution, so they may not be extreme enough 
to be considered outliers. Since the distribution is fairly symmetrical, we can rely on the mean of $$6.3$$ to give 
us a good idea of what a typical IMDb rating is. With a standard deviation of $$1$$, we know there is some variation in 
scores, but most scores fall between $$4$$ and $$8$$ on the $$1-10$$ scale.
""")