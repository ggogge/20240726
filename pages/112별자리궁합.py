import streamlit as st
import pandas as pd
from datetime import datetime

# 별자리 계산 함수
def get_zodiac_sign(day, month):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return '염소자리'
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return '물병자리'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return '물고기자리'
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return '양자리'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return '황소자리'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return '쌍둥이자리'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return '게자리'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return '사자자리'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return '처녀자리'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return '천칭자리'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return '전갈자리'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return '사수자리'

# 별자리 궁합 데이터
zodiac_compatibility합 🎉")

selected_name = st.selectbox("학생 이름을 선택하세요", data['이름'])

if selected_name:
    student_row = data[data['이름'] == selected_name].iloc[0]
    student_zodiac = student_row['별자리']

    compatible_zodiacs = zodiac_compatibility[student_zodiac]
    compatible_students = data[data['별자리'].isin(compatible_zodiacs) & (data['이름'] != selected_name)]

    st.write(f"**{selected_name}** 학생의 별자리는 **{student_zodiac}**입니다. 🌟")
    st.write(f"**{student_zodiac}**와 잘 맞는 별자리는 **{', '.join(compatible_zodiacs)}**입니다. 🤝")

    st.write("### 잘 맞는 친구들:")
    for idx, row in compatible_students.iterrows():
        st.write(f"- **{row['이름']}** ({row['별자리']})")

    st.write("### 조언:")
    st.write("별자리가 잘 맞는 친구들과 함께 하는 활동을 통해 서로의 장점을 배울 수 있어요. 서로 다른 관점을 이해하고, 협력하여 더 나은 결과를 만들어내 보세요! 🌈")

st.write("💡 이 애플리케이션은 별자리를 기반으로 한 궁합 추천을 제공합니다. 재미로 참고하세요! 😊")
