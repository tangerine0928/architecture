import streamlit as st
from openai import OpenAI

# OpenAI 클라이언트 생성 (본인의 API 키 넣기)
client = OpenAI(api_key="YOUR_API_KEY")

st.title("🏛️ 건축 아이디어 비주얼라이저")

purpose = st.selectbox("건축물의 용도 선택:", ["박물관", "카페", "학교", "주택", "병원", "도서관", "기타"])
theme = st.text_input("건축 디자인 주제를 입력하세요 (예: 미래지향, 자연친화 등)")

if st.button("이미지 생성하기"):
    if purpose and theme:
        prompt = f"A building designed as a {purpose}, with a {theme} theme, highly detailed architectural rendering"
        try:
            response = client.images.generate(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            image_url = response.data[0].url
            st.image(image_url, caption=f"건축물: {purpose}, 주제: {theme}")
            st.write(f"프롬프트: {prompt}")
        except Exception as e:
            st.error(f"이미지 생성 중 오류가 발생했습니다: {e}")
    else:
        st.warning("모든 항목을 입력해주세요.")
