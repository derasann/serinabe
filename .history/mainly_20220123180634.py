import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)

st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,]
)