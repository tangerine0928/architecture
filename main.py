import streamlit as st

st.title("🏛️ 건축 정보 블로그 / 매거진")

# 간단한 데이터 예시 (실제론 DB나 마크다운 파일 연동 추천)
posts = [
    {
        "title": "고딕 건축의 특징과 역사",
        "category": "역사적 건축물",
        "content": "고딕 건축은 첨탑과 스테인드글라스가 특징입니다...",
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Notre_Dame_de_Paris_2013-07-24.jpg"
    },
    {
        "title": "친환경 건축 디자인 트렌드",
        "category": "친환경 건축",
        "content": "최근 건축에서는 태양광 패널, 녹색 지붕 등 친환경 요소가 중요해졌습니다...",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Green_roof_on_the_building_in_The_Hague_01.jpg"
    },
    {
        "title": "현대 브루탈리즘의 매력",
        "category": "현대 건축",
        "content": "브루탈리즘은 거친 콘크리트 외관과 단순한 기하학적 형태가 특징입니다...",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Bruce_Robinson_Brutalism.jpg"
    }
]

# 카테고리 선택
categories = ["전체"] + sorted(set(post["category"] for post in posts))
selected_category = st.sidebar.selectbox("카테고리 선택", categories)

# 검색 기능
search_term = st.sidebar.text_input("검색어 입력")

# 필터링
filtered_posts = [
    post for post in posts
    if (selected_category == "전체" or post["category"] == selected_category) and
       (search_term.lower() in post["title"].lower() or search_term.lower() in post["content"].lower())
]

# 포스트 목록 보여주기
for idx, post in enumerate(filtered_posts):
    with st.expander(f"{post['title']} [{post['category']}]"):
        st.image(post["image"], use_container_width=True)
        st.write(post["content"])
