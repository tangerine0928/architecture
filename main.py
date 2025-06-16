import streamlit as st
import openai

# OpenAI API 키 설정 (본인 키로 변경)
openai.api_key = "YOUR_API_KEY"

st.set_page_config(page_title="건축 아이디어 비주얼라이저", layout="wide")

st.title("🏛️ 건축 아이디어 비주얼라이저")
st.write("건축물의 목적과 주제를 입력하면 그에 맞는 건축 이미지를 생성해드립니다.")

# 사용자 입력
purpose = st.selectbox("건축물의 용도를 선택하세요:", ["박물관", "카페", "학교", "주택", "병원", "도서관", "기타"])
theme = st.text_input("건축 디자인의 주제를 입력하세요 (예: 미래지향, 자연친화, 미니멀 등)")

if st.button("이미지 생성하기"):
    if purpose and theme:
        prompt = f"A building designed as a {purpose}, with a {theme} theme, highly detailed architectural rendering"
        
        try:
            # 최신 OpenAI 이미지 생성 API 호출
            response = openai.images.generate(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            image_url = response.data[0].url
            
            st.image(image_url, caption=f"건축물 용도: {purpose}, 주제: {theme}")
            st.write(f"프롬프트: {prompt}")
            
        except Exception as e:
            st.error(f"이미지 생성 중 오류가 발생했습니다: {e}")
    else:
        st.warning("모든 항목을 입력해주세요.")
