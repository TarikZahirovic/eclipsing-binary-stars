# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:01:09 2021

@author: Tarik Zahirovic
"""

import streamlit as st
import numpy as np
import pandas as pd
import math as mt

# st.sidebar.title("Menu")
st.title("Menu")

p1 = st.sidebar.number_input('Upisi prvi parametar?', value=0),
'Prvi parametar je:', p1

#p2 = st.sidebar.number_input('Upisi drugi parametar?')
#'Drugi parametar:', p2



st.sidebar.info("Vozdra narode")
number=st.sidebar.slider("Izaberi broj",0,100)


 df = pd.DataFrame({
   'first column': [1, 2, 3, 4],
   'second column': [10, 20, 30, 40]
 })

df

st.latex(r''' e^{i\pi} + 1 = 0 ''')

#if st.button('Add numbers'):
#	st.write('Total is: ' , p1+p2)

in_array = np.arange(0,10,0.01)
chart_data = pd.DataFrame(
     np.sin(in_array+p1),
     #np. random.randn(20, 1),
     columns=['a'])

st.line_chart(chart_data)

"Python"


# option = st.sidebar.selectbox(
#     'Upisi prvi parametar?',
#      df['first column'])

#'You selected:', option

