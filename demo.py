import streamlit as st
import time

# 设置页面配置，让界面变宽
st.set_page_config(layout="wide", page_title="千面智投 - 内容创作工作台")

# ================= 顶部导航栏 =================
st.markdown("### 千面智投")
col_nav1, col_nav2, col_nav3 = st.columns([1, 1, 1])
with col_nav3:
    st.markdown("小红书 · 抖音 · 公众号")

st.divider()  # 分割线

# ================= 主体三栏布局 =================
col1, col2, col3 = st.columns([1, 2, 1.5])

# --- 第一栏：我的 IP (左侧) ---
with col1:
    st.subheader("我的 IP")
    st.markdown("---")
    # 这里使用 radio 或者 button 模拟左侧菜单
    menu = st.radio("导航", ["IP画像", "记忆库", "创作历史"], label_visibility="collapsed")
    if menu == "记忆库":
        st.info("这里展示你所有的长期记忆列表...")
    elif menu == "创作历史":
        st.info("这里展示你过去生成的所有笔记...")

# --- 第二栏：内容创作工作台 (中间) ---
with col2:
    st.subheader("内容创作工作台")

    # 任务输入框 (还原图中的框)
    task_input = st.text_area(
        "内容任务",
        value="写一个关于实习被拒的小红书笔记，真实一点",
        height=100
    )

    # 生成按钮
    if st.button("生成内容", type="primary"):
        with st.spinner("正在调用大模型并检索记忆..."):
            # 模拟 API 调用耗时
            time.sleep(1.5)

            # 这里放置你之前的 Python 逻辑：评分、召回、调用大模型
            # 下面模拟返回结果
            st.markdown("---")
            st.text_input("标题", value="大二实习被拒，我学到了什么？")
            st.text_area("正文", value="今天收到了拒信，心里挺难受的...\n但是仔细复盘了一下，发现...", height=150)

            # 将“已调用记忆”的状态传递给右栏（通过 session_state）
            st.session_state['generated'] = True

# --- 第三栏：本次调用的记忆 (右侧，还原截图核心) ---
with col3:
    st.subheader("本次调用的记忆")

    if st.session_state.get('generated', False):
        # 记忆 1
        with st.container(border=True):
            st.write("❶ 大二求职被拒")
            st.progress(0.92, text="相关度 92%")

        # 记忆 2
        with st.container(border=True):
            st.write("❷ 拒绝空洞鸡汤")
            st.progress(0.87, text="相关度 87%")

        # 记忆 3
        with st.container(border=True):
            st.write("❸ 过去高赞笔记的开头结构")
            st.progress(0.81, text="相关度 81%")

        st.caption("已调用 3 条长期记忆")

        # 操作按钮
        c1, c2 = st.columns(2)
        with c1:
            st.button("删除这条记忆", use_container_width=True)
        with c2:
            st.button("查看来源", use_container_width=True)
    else:
        st.info("等待生成任务，自动召回相关记忆...")