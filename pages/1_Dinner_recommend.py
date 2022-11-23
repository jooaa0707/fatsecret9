## pages/1_Docs.py

import streamlit as st
import pandas as pd
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



#st.text_input('아침')
#st.text_input('점심')
#st.text_input('저녁')
    
      # 데이터 로딩 함수는 여기에!
# 페이지 컬럼 분할(예: 부트스트랩 컬럼, 그리드)

# Store the initial value of widgets in session state


col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.button("🍚아침 입력")
    text_input_1 = st.text_input(
        "아침 먹은 음식을 입력해주세요 👉",
    )

    st.button("🍚점심 입력")
    text_input_2 = st.text_input(
        "점심 먹은 음식을 입력해주세요 👉",
    )

    st.button("🍟간식 입력")
    text_input_3 = st.text_input(
        "간식 먹은 음식을 입력해주세요 👉",
    )

with col2:

    st.write('오늘 저녁에 뭘 먹을 수 있냐면요....^^')
    cal_data = pd.read_excel('fatsecret.xlsx')
    cal_search_basket=cal_data[cal_data['basket']==1]
    cal_search_basket_rec=cal_search_basket[cal_search_basket['cal2']< 300]
    st.table(cal_search_basket_rec[['name','cal2']])
    #cal_search3=cal_search2.T
    # 컬럼 나머지 부분에 라인차트 생성
   # st.table(cal_search3)

with col3:
    st.metric(label="칼로리 검색횟수", value='3등', delta=-1,
    delta_color="inverse")

    st.metric(label="목표칼로리 달성", value='1등', delta=2,
    delta_color="off")


