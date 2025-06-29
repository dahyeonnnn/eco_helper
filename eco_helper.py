import streamlit as st

st.title("🌱 AI 친환경 질문 도우미")

user_input = st.text_area("AI에게 할 질문을 입력해보세요!")

unnecessary_phrases = [
    "안녕하세요", "부탁드려요", "감사합니다", 
    "좋은 하루 되세요", "혹시", "좀", 
    "실 수 있을까요", "해주실 수 있나요?"
]

found_phrases = [phrase for phrase in unnecessary_phrases if phrase in user_input]

if user_input:
    base_score = 100
    length_penalty = len(user_input) // 25
    phrase_penalty = len(found_phrases) * 5
    final_score = max(0, base_score - length_penalty - phrase_penalty)

    st.subheader("🧠 분석 결과")
    st.write(f"✏️ 총 글자 수: **{len(user_input)}자**")
    st.write(f"🗑️ 불필요한 표현: {', '.join(found_phrases) if found_phrases else '없어요!'}")
    st.write(f"🌿 친환경 질문 점수: **{final_score} / 100점**")

    improved_question = user_input
    for phrase in found_phrases:
        improved_question = improved_question.replace(phrase, "")
    improved_question = improved_question.strip()

    if improved_question != user_input:
        st.subheader("🔄 추천 수정 문장:")
        st.success(improved_question)
else:
    st.info("질문을 입력해 주세요!")
