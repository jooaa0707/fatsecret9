import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import plotly.express as px
#import plotly as px
import plotly.graph_objects as go
from datetime import datetime



# 페이지 기본 설정
st.set_page_config(
    page_icon="🐶",
    page_title="저녁뭐먹지?",
    layout="wide",
)

# 페이지 헤더, 서브헤더 제목 설정
st.header("DToC's에 오신걸 환영합니다👋")
st.subheader("오늘의 다이어트 랭킹을 확인해봅시다!!")

col1, col2 = st.columns([1, 2])

with col1:
    @st.cache
    def load_data():
        df = pd.read_csv('ranking.csv')
        return df

    rank_data = load_data()

    rank_data1 = rank_data.drop(['result'],axis='columns')

    rank_result = rank_data1
    st.date_input("🗓Today is",datetime.today())
    st.write("\n")
    st.write("\n")
    
    st.write("일일 칼로리 목표와 섭취결과")
    st.write("\n")
    st.table(rank_result)

with col2:
    @st.cache
    def load_data():
        df = pd.read_csv('ranking.csv')
        return df

    rank_data2 = load_data()
    rank_data2 = rank_data2.astype({'result': float, '이름' : object,'하루 목표량' : int,'섭취량' : int  })
    rank_result = rank_data2.sort_values(by='result', ascending=True)



    bar_trace = go.Bar(x=rank_result['이름'], y=rank_result['result'], width = 0.5)
    data = [bar_trace]


    fig = go.Figure(data=data)
    fig.update_layout(
        title={
            'text' : "얼마나 덜 먹었나",
            'x' : 0.5,
            'y' : 0.9,
            'xanchor': 'center',
            'yanchor': 'top', 
            }
        )
        
    



    st.plotly_chart(fig)



