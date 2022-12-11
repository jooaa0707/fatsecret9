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





col1, col2, col3 = st.columns([1,1,1])
with col1:
    with st.container():
        st.write("먼저 당신의 목표 칼로리를 계산해드립니다.")
        height = st.number_input('키를 입력하세요',160)
        weight = st.number_input('몸무게를 입력하세요',50)
        age = st.number_input('나이를 입력하세요',35)
        basal_netabolism=round(655.1 + (9.56 * weight) + (1.85 * height) - (4.68 *age),1)

        purpose_cal= 300+basal_netabolism

    goal = purpose_cal
    st.write("\n")
    st.write("\n")
    st.write("\n")
    # 칼로리 계산 끝
    st.write("혜윤님의 오늘 하루 목표 칼로리는",goal)

with col2:
    text_input_1 = st.text_input(
        "🍚아침 먹은 음식을 입력해주세요 👉","훈제란"
    )

    text_input_2 = st.text_input(
        "🍚점심 먹은 음식을 입력해주세요 👉","불고기"
    )

    text_input_3 = st.text_input(
        "🍟간식 먹은 음식을 입력해주세요 👉","프로틴칩"
    )

    

with col3:

    st.write('오늘 저녁에 뭘 먹을 수 있냐면요....^^')

    
    cal_data = pd.read_csv('fatsecret9.csv')

    breakfast=cal_data.loc[cal_data['name'].str.contains(text_input_1)].head(1)
    lunch=cal_data.loc[cal_data['name'].str.contains(text_input_2)].head(1)
    snack=cal_data.loc[cal_data['name'].str.contains(text_input_3)].head(1)

    din = goal-(breakfast['cal2'].values[0]+lunch['cal2'].values[0]+snack['cal2'].values[0])
    #din = goal-(cal_data[cal_data['name']==text_input_1].cal2.values[0]+cal_data[cal_data['name']==text_input_2].cal2.values[0]+cal_data[cal_data['name']==text_input_3].cal2.values[0])
    st.write('남은 저녁 칼로리는')
    st.write(din,'kcal')

    cal_search_basket=cal_data[cal_data['basket']==1]
    cal_search_basket_rec=cal_search_basket[cal_search_basket['cal2']< din].head(5).sort_values(by='cal2',ascending=False)
    st.table(cal_search_basket_rec[['name','cal2']])

    text_input_4 = st.text_input(
    "🥗 저녁으로 뭘 먹겠나요? 👉","호유란"
    )
    st.write('오늘의 남은 칼로리는??')
    din_hope = cal_data.loc[cal_data['name'].str.contains(text_input_4)].head(1)
    din2 = din - din_hope['cal2'].values[0]
    st.write(din2,'kcal')
    if din2 > 0:
        st.success('목표 칼로리 성공!', icon="✅")
    else:
        st.warning('목표 칼로리 실패', icon="⚠️")

    #cal_search3=cal_search2.T
    # 컬럼 나머지 부분에 라인차트 생성
   # st.table(cal_search3)

