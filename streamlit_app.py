
import streamlit as st
import random

st.set_page_config(page_title="67 Survival", page_icon="💀")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #100020, #310052);
    color: white;
}
h1 {
    text-align: center;
    color: #ffcc00 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("💀 67 SURVIVAL GAME 💀")
st.markdown("### 🗿 SURVIVE THE 67 APOCALYPSE")

# Initialize game
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.hp = 3
    st.session_state.game_over = False
    st.session_state.started = False
    st.session_state.player = "🗿"
    st.session_state.message = "Press START to begin!"

def start_game():
    st.session_state.score = 0
    st.session_state.hp = 3
    st.session_state.game_over = False
    st.session_state.started = True
    st.session_state.message = "GO GO GO!"

def move(direction):
    if st.session_state.game_over:
        return

    event = random.randint(1, 100)

    if event <= 50:
        st.session_state.score += 67
        st.session_state.message = "🔥 +67 POINTS! SIX SEVEN!"
    elif event <= 80:
        st.session_state.hp -= 1
        st.session_state.message = "💣 BOOM! YOU GOT HIT!"
    else:
        st.session_state.score += 134
        st.session_state.message = "🗿 DOUBLE 67 BONUS!"

    if st.session_state.hp <= 0:
        st.session_state.game_over = True
        st.session_state.message = "💀 GAME OVER! YOU GOT BRAINROTTED!"

# Dashboard
c1, c2 = st.columns(2)

with c1:
    st.metric("🏆 SCORE", st.session_state.score)

with c2:
    st.metric("❤️ LIVES", max(0, st.session_state.hp))

st.divider()

# Game screen
if not st.session_state.started:
    st.markdown("# 🗿")
    st.markdown("### Ready to become the 67 LEGEND?")
    st.button("▶️ START GAME", on_click=start_game)

elif st.session_state.game_over:
    st.error("💀 GAME OVER")
    st.markdown(f"# FINAL SCORE: {st.session_state.score}")
    st.button("🔄 PLAY AGAIN", on_click=start_game)

else:
    st.markdown("""
    <div style="
        background:#16002c;
        border:3px solid #ff00ff;
        border-radius:20px;
        padding:30px;
        text-align:center;
    ">
        <div style="font-size:65px">🗿</div>
        <h2 style="color:#ffff00">67 WORLD</h2>
        <div style="font-size:40px">💎　💣　💎</div>
        <h3 style="color:white">COLLECT 67 OR DIE</h3>
    </div>
    """, unsafe_allow_html=True)

    st.info(st.session_state.message)

    st.write("### 🎮 Choose your move!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("⬅️ LEFT", on_click=move, args=("left",), use_container_width=True)

    with col2:
        st.button("⬆️ JUMP", on_click=move, args=("jump",), use_container_width=True)

    with col3:
        st.button("➡️ RIGHT", on_click=move, args=("right",), use_container_width=True)

    st.caption("Every move has a random outcome. Good luck 💀")

st.divider()
st.caption("67 SURVIVAL™ | Brainrot Studios 2026")
