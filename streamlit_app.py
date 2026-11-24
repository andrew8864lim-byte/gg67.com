import streamlit as st
import random
import time

# 1. 页面基础配置（网页标签页都会变成67！）
st.set_page_config(
    page_title="67 宇宙官方认证中心",
    page_icon="6️⃣",
    layout="centered"
)

# 初始化状态记录（记录你按了多少次 67）
if "count_67" not in st.session_state:
    st.session_state.count_67 = 0

# 标题整活
st.title("6️⃣7️⃣ 67 宇宙发疯终端")
st.caption("警告：本应用含 67 量极高，精神状态不稳定者请勿轻易点击。")

# 2. 侧边栏：67 浓度调节器
with st.sidebar:
    st.header("⚙️ 67 控制台")
    st.metric(label="当前已发射 67 次数", value=f"{st.session_state.count_67} 次", delta="精神状态良好" if st.session_state.count_67 < 6 else "已彻底疯狂")
    
    intensity = st.select_slider(
        "选择你的 67 疯癫程度：",
        options=["微醺 67", "上头 67", "彻底疯狂 676767"]
    )
    
    if st.button("重置精神状态"):
        st.session_state.count_67 = 0
        st.rerun()

# 3. 核心互动区：升级版 Greet 按钮
st.subheader("👇 仪式感启动区")
user_name = st.text_input("输入你的大名（不填默认你是 67 代言人）：", placeholder="例如：67小王子")
display_name = user_name if user_name else "尊贵的 67 传人"

if st.button("🚀 狠狠地 Greet 一下 (67!)", use_container_width=True, type="primary"):
    st.session_state.count_67 += 1
    
    # 假装很正经的加载进度条
    progress_text = "正在连接 67 星球基站，检测幽默细胞..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    my_bar.empty() # 加载完清空进度条

    # 屏幕特效（气球或下雪随机触发）
    if random.choice([True, False]):
        st.balloons()
    else:
        st.snow()

    # 搞笑随机语录库
    jokes = [
        f"Hello, {display_name}! 6767676767！今天也是被 67 硬控的一天！",
        f"报告 {display_name}：你的大脑已被 67 占领，现在打字只会输出 676767...",
        f"别问为什么是 67，问就是 6 翻了，7 飞了！{display_name} 给我冲！",
        f"检测到 {display_name} 试图保持冷静……检测失败！67676767676767！",
        f"医生说我需要静养，但我一看到 {display_name} 就忍不住喊出：67——！"
    ]

    # 根据侧边栏选择的浓度输出不同效果
    if intensity == "微醺 67":
        st.info(random.choice(jokes))
    elif intensity == "上头 67":
        st.success(random.choice(jokes))
        st.code("67 " * 20, language="python")
    else:
        st.error("🚨 警告！67 浓度超标！系统即将崩溃！🚨")
        st.markdown(f"### {random.choice(jokes)}")
        st.code("67" * 67, language="text")

st.divider()

# 4. 附加搞笑小功能：今日 67 运势盲盒
st.subheader("🔮 今日 67 运势盲盒")
col1, col2 = st.columns(2)

with col1:
    if st.button("抽取今日 67 签文"):
        fortunes = [
            "【大吉】宜大喊 67，忌写代码（写了也有 Bug）。",
            "【特吉】今天你会遇到 67 件好事，前提是你先笑出声。",
            "【666】你距离 67 只差 1 点发疯。",
            "【777】运气爆棚，建议立刻去买张彩票（中了分我 67%）。"
        ]
        st.toast("抽签成功！", icon="🎉")
        st.warning(random.choice(fortunes))

with col2:
    # 互动滑块整活
    mood = st.slider("滑动测试你现在的含 67 量：", 0, 100, 67)
    if mood == 67:
        st.write("🎯 **天选之人！精准命中 67！**")
    elif mood > 67:
        st.write(f"📈 达到 {mood}%，已经超越 67 极限了！")
    else:
        st.write(f"📉 只有 {mood}%，建议多按几次上面的按钮补补。")
