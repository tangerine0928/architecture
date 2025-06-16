main.py
requirements.txt
import streamlit as st
import openai  # DALL·E API 호출용

st.set_page_config(page_title="건축물 이미지 생성기", layout="wide")

st.title("🏛️ 건축 아이디어 비주얼라이저")
st.write("건축물의 목적과 주제를 입력하면 그에 맞는 건축 이미지를 생성해드립니다.")

# 입력
purpose = st.selectbox("건축물의 용도를 선택하세요:", ["박물관", "카페", "학교", "주택", "병원", "도서관", "기타"])
theme = st.text_input("건축 디자인의 주제를 입력하세요 (예: 미래지향, 자연친화, 미니멀 등)")

# 버튼
if st.button("이미지 생성하기"):
    if purpose and theme:
        prompt = f"A building designed as a {purpose}, with a {theme} theme, high detail, architectural rendering"
        
        # OpenAI DALL·E API 호출 (예시)
        openai.api_key = "YOUR_API_KEY"
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response["data"][0]["url"]
        
        st.image(image_url, caption=f"건축물 용도: {purpose}, 주제: {theme}")
    else:
        st.warning("모든 항목을 입력해주세요.")
