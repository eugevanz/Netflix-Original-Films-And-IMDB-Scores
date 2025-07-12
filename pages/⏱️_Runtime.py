import streamlit as st

st.set_page_config(page_title="Runtime", page_icon="⏱️")

with st.sidebar:
    st.write("""
    **The summary for the runtime variable**
    
    In a left-skewed distribution, the mean is typically less than the median because the lower tail pulls the mean down. Therefore, the median runtime is likely greater than $$92.5$$ minutes. The left skew might be caused by a few films with very short runtimes, which could be outliers. These outliers can impact the mean significantly more than they would impact the median.
    """)

st.write("# Runtime ⏱️")

st.header("The summary for the runtime variable", divider="rainbow")

st.write("""
There are two aspects of this distribution plot that might lead to concern about using the mean and standard deviation:

- The distribution is left-skewed — it has a long tail of low values on the left side. These values might influence 
the mean to be lower.
- There is a single high value of just above 200 minutes. This value might be an outlier that influences the mean to 
be higher.
""")

st.write("""
A standard deviation of $$28.4$$ minutes indicates a relatively high variability in the runtime. This suggests that 
while the average runtime is around 92.5 minutes, there is a significant spread around this mean.
""")

st.write("""
We could use statistics that are more robust to outliers and skewness, such as the median and interquartile range (
IQR). The median is the middle value and the IQR is the range of the middle 50% of the data ($$Q3 - Q1$$).
""")

st.write("""
The mean describes a typical runtime as in the low 90s. The standard deviation describes the distribution as having wide variability, with runtimes an average of almost 30 minutes different than the mean. These measurements are not wrong, but they don’t help us do a good job of summarizing what we’re seeing in the distribution.
""")
