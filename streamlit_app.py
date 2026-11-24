import streamlit as st
import random
import time

st.set_page_config(page_title="67 游乐场", page_icon="🎮", layout="centered")

# --- 初始化游戏数据 ---
if "energy" not in st.session_state:
    st.session_state.energy = 0
if "clicks" not in st.session_state:
    st.session_state.clicks = 0
if "secret_num" not in st.session_state:
    st.session_state.secret_num = random.randint(1, 100)
if "guess_count" not in st.session_state:
    st.session_state.guess_count = 0

st.title("🎮 67 精神状态游乐场")
st.caption("欢迎来到 67 游戏厅，请管好你的理智！")

# 使用 Tabs 切换三个小游戏
tab1, tab2, tab3 = st.tabs(["⚡ 游戏1：蓄力冲刺 67", "🎯 游戏2：精准狙击 67", "🃏 游戏3：67 命运抽卡"])

# ==========================================
# 游戏 1：蓄力冲刺 67（运气 + 手速）
# ==========================================
with tab1:
    st.subheader("目标：把 67 能量槽精准充到 67！")
    st.write("每次点击会随机增加或减少能量，**刚好凑齐 67 就算通关**，超过 67 就会直接爆炸！")

    # 进度条展示当前能量
    progress_val = min(max(st.session_state.energy / 67, 0.0), 1.0)
    st.progress(progress_val)
    
    col1, col2 = st.columns(2)
    col1.metric("当前能量值", f"{st.session_state.energy} / 67")
    col2.metric("已操作次数", f"{st.session_state.clicks} 次")

    # 判定胜负状态
    if st.session_state.energy == 67:
        st.balloons()
        st.success(f"🎉 牛啊！你只用了 {st.session_state.clicks} 次就精准凑出了 67！你是真正的 67 之神！")
        if st.button("再玩一局", key="win_reset"):
            st.session_state.energy = 0
            st.session_state.clicks = 0
            st.rerun()

    elif st.session_state.energy > 67:
        st.error(f"💥 轰隆！能量达到 {st.session_state.energy}，超过 67 炸膛了！你疯得太彻底了！")
        if st.button("抢救一下（重新开始）", key="lose_reset"):
            st.session_state.energy = 0
            st.session_state.clicks = 0
            st.rerun()

    else:
        # 游戏进行中的操作按钮
        btn_col1, btn_col2, btn_col3 = st.columns(3)
        
        with btn_col1:
            if st.button("🔥 猛充 (+5 ~ +15)", use_container_width=True):
                gain = random.randint(5, 15)
                st.session_state.energy += gain
                st.session_state.clicks += 1
                st.toast(f"猛充成功！能量 +{gain}")
                st.rerun()

        with btn_col2:
            if st.button("🤏 微调 (+1 ~ +3)", use_container_width=True):
                gain = random.randint(1, 3)
                st.session_state.energy += gain
                st.session_state.clicks += 1
                st.toast(f"小心翼翼！能量 +{gain}")
                st.rerun()

        with btn_col3:
            if st.button("🧊 冷静 (-1 ~ -6)", use_container_width=True):
                loss = random.randint(1, 6)
                st.session_state.energy = max(0, st.session_state.energy - loss)
                st.session_state.clicks += 1
                st.toast(f"强行冷静！能量 -{loss}")
                st.rerun()

# ==========================================
# 游戏 2：精准狙击（猜数字整活版）
# ==========================================
with tab2:
    st.subheader("猜猜系统心里想的 1~100 之间的数字")
    guess = st.number_input("输入你猜的数字：", min_value=1, max_value=100, value=67, step=1)
    
    if st.button("发射猜测！", type="primary"):
        st.session_state.guess_count += 1
        target = st.session_state.secret_num
        
        # 特殊彩蛋：不管答案是啥，只要输入 67 就有专属吐槽
        if guess == 67 and target != 67:
            st.toast("虽然你很爱 67，但这次答案还真不是 67 哈哈哈哈！", icon="🤣")

        if guess < target:
            st.warning(f"📉 太小了！往大了猜！（已猜 {st.session_state.guess_count} 次）")
        elif guess > target:
            st.warning(f"📈 太大了！往小了猜！（已猜 {st.session_state.guess_count} 次）")
        else:
            st.snow()
            st.success(f"🎯 猜中了！答案就是 **{target}**！你一共猜了 {st.session_state.guess_count} 次！")
            st.session_state.secret_num = random.randint(1, 100)
            st.session_state.guess_count = 0
            st.info("系统已经偷偷换了一个新数字，随时可以继续猜！")

# ==========================================
# 游戏 3：67 命运盲盒抽卡
# ==========================================
with tab3:
    st.subheader("测试你今天的 67 欧气")
    cards = [
        ("SSR 👑 67 创世神", "全服唯一！今天你干啥都会 676767！", "error"),
        ("SR 🔥 发疯小能手", "精神状态极其美丽，建议原地大喊三声 67。", "warning"),
        ("R 😎 冷静路人甲", "你居然还没被 67 洗脑？快多按几下按钮！", "info"),
        ("N 🥔 摸鱼土豆", "今天适合躺平，什么都不干，只负责喊 67。", "success")
    ]
    
    if st.button("✨ 消耗 67 点理智抽一张卡", use_container_width=True):
        with st.spinner("正在洗牌，注入 67 灵魂..."):
            time.sleep(0.6)
        title, desc, msg_type = random.choices(cards, weights=[10, 30, 35, 25])[0]
        
        st.markdown(f"### 你抽到了：【{title}】")
        if msg_type == "error":
            st.balloons()
            st.error(desc)
        elif msg_type == "warning":
            st.warning(desc)
        elif msg_type == "info":
            st.info(desc)
        else:
            st.success(desc)
