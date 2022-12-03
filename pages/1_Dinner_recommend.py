## pages/1_Docs.py

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# 페이지 기본 설정
st.set_page_config(
    page_icon="🐶",
    page_title="저녁뭐먹지?",
    layout="wide",
)


# 페이지 헤더, 서브헤더 제목 설정
st.header("DToC's에 오신걸 환영합니다👋")
st.subheader("저녁에 뭘 먹을 수 있을지 확인해봅시다!!")

st.write("미라님의 오늘 하루 목표 칼로리는 1,800kcal")

goal = 1800


col1, col2, col3 = st.columns([1,1,1])

with col1:
    from datetime import datetime
    #datetime.today()            # 현재 날짜 가져오기
    st.date_input("🗓Today is",datetime.today())
    text_input_1 = st.text_input(
        "🍚아침 먹은 음식을 입력해주세요 👉","동의 훈제란"
    )

    text_input_2 = st.text_input(
        "🍚점심 먹은 음식을 입력해주세요 👉","고기듬뿍 불고기 백반"
    )

    text_input_3 = st.text_input(
        "🍟간식 먹은 음식을 입력해주세요 👉","치즈 프로틴칩"
    )

    

with col2:

    st.write('오늘 저녁에 뭘 먹을 수 있냐면요....^^')

    
    cal_data = pd.read_csv('fatsecret9.csv')
    din = goal-(cal_data[cal_data['name']==text_input_1].cal2.values[0]+cal_data[cal_data['name']==text_input_2].cal2.values[0]+cal_data[cal_data['name']==text_input_3].cal2.values[0])
    st.write('남은 저녁 칼로리는')
    st.write(din,'kcal')

    cal_search_basket=cal_data[cal_data['basket']==1]
    cal_search_basket_rec=cal_search_basket[cal_search_basket['cal2']< din].head(5).sort_values(by='cal2',ascending=False)
    st.table(cal_search_basket_rec[['name','cal2']])

    text_input_4 = st.text_input(
    "🥗 저녁으로 뭘 먹겠나요? 👉","호유란"
    )

    #cal_search3=cal_search2.T
    # 컬럼 나머지 부분에 라인차트 생성
   # st.table(cal_search3)

with col3:
    st.write('오늘의 남은 칼로리는??')
    din2 = din - cal_data[cal_data['name']==text_input_4].cal2.values[0]
    st.write(din2,'kcal')
    if din2 > 0:
        st.success('목표 칼로리 성공!', icon="✅")
    else:
        st.warning('목표 칼로리 실패', icon="⚠️")
    #st.metric(label="칼로리 검색횟수", value='3등', delta=-1,
    #delta_color="inverse")

    #st.metric(label="목표칼로리 달성", value='1등', delta=2,
    #delta_color="off")


