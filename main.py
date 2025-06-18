import streamlit as st

st.title("건축물 추천 웹앱")
st.write("입력한 건축적 특징에 맞는 건축물을 추천해드립니다.")

# 사용자 입력
style = st.selectbox("건축 양식 선택", ["고딕", "르네상스", "현대", "브루탈리즘", "하이테크"])
material = st.selectbox("주 재료 선택", ["콘크리트", "유리", "석재", "철", "목재"])
era = st.selectbox("건축 시기", ["고대", "중세", "근대", "현대", "21세기"])
use = st.selectbox("용도", ["주거", "상업", "종교", "공공", "기타"])

# 데이터 예시
buildings = [
    {"name": "노트르담 대성당", "style": "고딕", "material": "석재", "era": "중세", "use": "종교"},
    {"name": "바르셀로나 파빌리온", "style": "현대", "material": "유리", "era": "근대", "use": "공공"},
    {"name": "퐁피두 센터", "style": "하이테크", "material": "철", "era": "현대", "use": "공공"},
    {"name": "빌라 사보아", "style": "현대", "material": "콘크리트", "era": "근대", "use": "주거"},
    {"name": "브루탈리즘 국립도서관", "style": "브루탈리즘", "material": "콘크리트", "era": "현대", "use": "공공"},
]

# 필터링
results = [b for b in buildings if b["style"] == style and b["material"] == material and b["era"] == era and b["use"] == use]

# 결과 출력
st.subheader("추천 건축물:")
if results:
    for r in results:
        st.markdown(f"✅ **{r['name']}**")
else:
    st.warning("해당 조건을 만족하는 건축물이 없습니다.")
