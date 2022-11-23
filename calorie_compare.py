# app.py

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from time import sleep


# 페이지 기본 설정
st.set_page_config(
    page_icon="🐶",
    page_title="저녁뭐먹지?",
    layout="wide",
)

# 로딩바 구현하기


# 페이지 헤더, 서브헤더 제목 설정
st.header("😍DToC's에 오신걸 환영합니다👋")
st.subheader("칼로리 비교하는 습관을 가집시다!!")


col1, col2 = st.columns([1, 2])

with col1:
    genre = st.radio(
        "🍎어떤 순서로 검색할까요?",
        ('칼로리', '단백질', '당'))

    if genre == '칼로리':
        st.write('You selected 칼로리.')

    else:
        st.write("You didn't select 칼로리.")
    
    text_input = st.text_input(
        "🍋메뉴를 입력하세요 👇","삼겹살"
    )


    if text_input:
        st.write("You entered: ", text_input)

    st.image('ok.jpeg')

with col2:
    cal_data = pd.read_excel('fatsecret.xlsx')
    cal_search=cal_data.loc[cal_data['name'].str.contains(text_input)]
    cal_search2=cal_search.sort_values(by='cal2',ascending=True)
    cal_search3=cal_search2.T
    # 컬럼 나머지 부분에 라인차트 생성
    st.table(cal_search3)

    
