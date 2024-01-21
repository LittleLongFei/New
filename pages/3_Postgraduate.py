

import streamlit as st

from PIL import Image

# page Configuration

st.set_page_config(
    page_title="Hui-Zhang",
    page_icon="🏡",
    layout="wide",
)

# 在侧边栏添加导航栏元素
st.sidebar.title("导航栏标题")
st.sidebar.write("导航栏说明文本")

# 添加导航栏链接
page = st.sidebar.radio("导航栏选项", ["主页", "页面1", "页面2"])

# 根据导航栏选项显示不同的内容
if page == "主页":
    st.title("欢迎访问主页")
    # 添加主页内容
if page == "主页1":
    st.title("页面1")
    # 添加页面1的内容
if page == "主页2":
    st.title("页面2")
    # 添加页面2的内容


