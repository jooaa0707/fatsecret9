
import streamlit as st
import pandas as pd
import numpy as np

cal_data = pd.read_excel('/Users/mira/Documents/GitHub/calorie9/fatsecret/fatsecret.xlsx')
cal_search=cal_data.loc[cal_data['name'].str.contains('삼겹살')]
cal_search2=cal_search.sort_values(by='cal2',ascending=True)
cal_search3=cal_search2.T


cal_data2