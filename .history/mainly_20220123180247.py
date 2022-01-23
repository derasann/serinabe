import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
})

st.dataframe(df)

