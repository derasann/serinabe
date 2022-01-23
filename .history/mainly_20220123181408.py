import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 入門')

st.write('Display Image')

if st.checkbox('Show Image')

    img = Image.open('serira-men.JPG')
    st.image(img, caption='Good taste', use_column_width=True)

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)

st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']    
)
st.map(df)