import streamlit as st
import random

st.set_page_config(page_title="Guess A Number", page_icon="🎮", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #0f0f1a;
        }
        .title {
            text-align: center;
            font-size: 3rem;
            font-weight: 800;
            color: #a78bfa;
            text-shadow: 0 0 20px #7c3aed;
            margin-bottom: 0.2rem;
        }
        .subtitle {
            text-align: center;
            font-size: 1.1rem;
            color: #c4b5fd;
            margin-bottom: 2rem;
        }
        .attempts-box {
            text-align: center;
            font-size: 1.1rem;
            background: #1e1b4b;
            border: 1px solid #4c1d95;
            border-radius: 12px;
            padding: 0.8rem;
            color: #ddd6fe;
            margin-bottom: 1rem;
        }
        .hint-box {
            text-align: center;
            background: #1e3a5f;
            border: 1px solid #3b82f6;
            border-radius: 12px;
            padding: 0.8rem;
            color: #bfdbfe;
            margin-top: 1rem;
        }
        .win-box {
            text-align: center;
            font-size: 1.5rem;
            font-weight: 700;
            background: #064e3b;
            border: 1px solid #10b981;
            border-radius: 16px;
            padding: 1.5rem;
            color: #6ee7b7;
            margin-bottom: 1.5rem;
        }
        div.stButton > button {
            width: 100%;
            border-radius: 10px;
            font-weight: 600;
            font-size: 1rem;
            padding: 0.6rem;
            background: #7c3aed;
            color: white;
            border: none;
            transition: 0.2s;
        }
        div.stButton > button:hover {
            background: #6d28d9;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 50)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.hint_used = False

def reset_game():
    st.session_state.target = random.randint(1, 50)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.hint_used = False

st.markdown('<div class="title">🎮 Number Guessing Game</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Guess the secret number between 1 and 50!</div>', unsafe_allow_html=True)

if st.session_state.game_over:
    st.markdown(f"""
        <div class="win-box">
            🥳 You got it!<br>
            Guessed in <span style="color:#34d399">{st.session_state.attempts} attempts</span>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🔄 Play Again"):
        reset_game()
        st.rerun()
else:
    st.markdown(f"""
        <div class="attempts-box">
            🎯 Attempts so far: <strong>{st.session_state.attempts}</strong>
        </div>
    """, unsafe_allow_html=True)

    user_input = st.number_input("Enter your guess:", min_value=1, max_value=50, step=1)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Submit Guess"):
            st.session_state.attempts += 1
            if user_input < st.session_state.target:
                st.warning("Too LOW ⬇️ Think bigger!")
            elif user_input > st.session_state.target:
                st.warning("Too HIGH ⬆️ Think smaller!")
            else:
                st.session_state.game_over = True
                st.rerun()

    with col2:
        if not st.session_state.hint_used:
            if st.button("💡 Get Hint"):
                st.session_state.hint_used = True

    if st.session_state.hint_used:
        parity = "even" if st.session_state.target % 2 == 0 else "odd"
        st.markdown(f"""
            <div class="hint-box">
                💡 Hint: The number is <strong>{parity}</strong>
            </div>
        """, unsafe_allow_html=True)