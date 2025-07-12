import streamlit as st

st.set_page_config(page_title="Language", page_icon="🤟")

with st.sidebar:
    st.write("""
    **Films in each language**
    
    There are $$360$$ films with English as the primary language. 
    To get the proportion, we divide $$360$$ by the total of $$503$$ films: $$360 ÷ 503 = 0.72$$. 
    About $$0.72$$ of the films have English as their primary language.
    """)

st.write("# Language 🤟")

st.header("Films in each language", divider="rainbow")

st.write("""
We know there are $$360$$ English-language films, but we have to do a little work to find the number of other 
single-language films. 
We can add the **four categories** for Spanish, Hindi, French, and "other single" ($$ 29 + 27 + 15 + 51 = 122 $$). Or 
we can subtract the English and 'multiple' categories from the total ($$ 503 - 360 - 21 = 122 $$). This means the 
ratio of English films to non-English single-language films is **360 to 122**. Since $$ 360 / 122 = 2.95 $$, this means there are almost **3 English films** for every non-English film.
""")

st.write("There are $$21$$ films that have multiple primary languages. Dividing $$21$$ by $$503$$ gives a proportion "
         "of "
         "$$0.04$$.")

st.write(
    "Our study on languages in films on Netflix revealed that out of $$503$$ films, $$360$$ have English as their "
    "primary language. This constitutes approximately $$72$$% of the total films. By examining the other language categories, "
    "we found $$29$$ films in Spanish, $$27$$ in Hindi, $$15$$ in French, and $$51$$ in other single languages, "
    "summing up to $$122$$ films. This means the proportion of non-English single-language films is about $$24$$% ($$ "
    "122/503 $$). Additionally, there are $$21$$ films with multiple primary languages, making up approximately $$4$$% "
    "of the total films. The ratio of English films to non-English single-language films is nearly $$3:1$$, "
    "highlighting the predominance of English-language films on Netflix.")

st.write("Of the $$21$$ films with multiple primary languages, $$16$$ are documentaries. This makes a lot of sense if "
         "the documentary makers are using a different language than the documentary subjects.")