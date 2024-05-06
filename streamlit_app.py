import streamlit as st
import random
import time
import matplotlib.pyplot as plt

# Streamlit 세션 상태 초기화
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.times = []

def random_random(s: int, t: int):
    return random.randint(s, t)

def next_question():
    st.session_state.a = random_random(1, 5)
    st.session_state.b = random_random(1, 5)
    st.session_state.c = random_random(1, 5)
    st.session_state.start_time = time.time()

st.title("Mathematics Quiz Show!!")
st.write(f"Question {st.session_state.current_question + 1} of 10")

# 문제 번호 증가 및 새 문제 로드
if st.session_state.current_question < 10:
    if st.button('Start' if st.session_state.current_question == 0 else 'Next Question', key=f"button_{st.session_state.current_question}"):
        if st.session_state.current_question > 0:  # 첫 번째 문제가 아닐 때
            elapsed_time = time.time() - st.session_state.start_time
            st.session_state.times.append(elapsed_time)  # 시간 기록 저장
        next_question()
        st.session_state.current_question += 1

if 0 < st.session_state.current_question <= 10:
    st.latex(f"{st.session_state.a}^2 + {st.session_state.b} + {st.session_state.c} = ")
    answer = st.text_input("Enter your answer:", key=f"answer_{st.session_state.current_question}")

    if answer:
        correct_answer = st.session_state.a**2 + st.session_state.b + st.session_state.c
        if int(answer) == correct_answer:
            st.success("Correct! 🎉")
            st.session_state.score += 1
        else:
            st.error("Incorrect. Try again!")

# 결과 표시 및 퀴즈 재시작
if st.session_state.current_question == 10:
    if len(st.session_state.times) == 9:  # 마지막 문제의 시간 추가
        elapsed_time = time.time() - st.session_state.start_time
        st.session_state.times.append(elapsed_time)
    if st.button("Show Results"):
        st.write("Quiz completed!")
        st.write(f"Your score: {st.session_state.score} / 10")
        fig, ax = plt.subplots()
        ax.plot(range(1, 11), st.session_state.times, marker='o')
        ax.set_xlabel('Question Number')
        ax.set_ylabel('Time Taken (seconds)')
        ax.set_title('Time Taken for Each Question')
        st.pyplot(fig)

    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.times = []
