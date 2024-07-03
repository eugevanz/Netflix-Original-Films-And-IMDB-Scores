import streamlit as st

st.set_page_config(page_title="Genre", page_icon="📊")

st.sidebar.success("""
**The summary for the genre variable**

From our analysis of IMDb scores across various film genres, we found that documentaries and films classified under “other” genres received the highest IMDb scores. In contrast, documentaries in other languages or with multiple primary languages tended to have lower IMDb scores.
""")

st.write("# Genre 📊")

st.header("The summary for the genre variable", divider="rainbow")

st.write("""
While documentaries generally perform well in terms of viewer ratings, language diversity within this genre might negatively impact their scores. Other genres, not specified as documentaries, scored lower overall, placing them in the lower spectrum of IMDb ratings. This trend highlights the strong positive reception for English-language documentaries compared to other film categories and language variations.
""")

st.write("""
Genre is a categorical variable — this variable gives information about a quality of the films that is non-numeric. We can describe categorical variables using frequencies, proportions, and ratios.

Our colleague might create a table showing the different genre categories, the count of films in each category (frequency), and the percentage of the total this count represents (proportion). Our colleague might also compare counts of genres to one another using ratios.
""")
