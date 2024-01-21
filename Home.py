




import streamlit as st

from PIL import Image

# page Configuration

st.set_page_config(
    page_title="Hui-Zhang",
    page_icon="🏡",
    layout="wide",
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 导航栏
image = Image.open(r'./Resource/6.png')
st.sidebar.image(image, width=300)

st.sidebar.title("Hui Zhang")
st.sidebar.caption("<span style='font-family: Arial; font-size: 18px; color: gray;'>H-Zhang</span>",
                   unsafe_allow_html=True)
st.sidebar.write("<span style='font-family: Times New Roman; font-size: 18px;'>School of Control Science and Engineering, Shandong University</span>",
         unsafe_allow_html=True)

# --------------------------------------------------------------------- 导航栏 ---- 位置/邮箱等信息

st.sidebar.write("---")


col1, col2 = st.sidebar.columns([1, 8])

image = Image.open(r'./Resource/weizhi-3.png')

col1.image(image, width=30)
col2.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>Jinan, China</span>",
                     unsafe_allow_html=True)

col1, col2 = st.sidebar.columns([1, 8])

image = Image.open(r'./Resource/lianjie-2.png')

col1.image(image, width=25)
col2.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[website](https://www.streamlit.io/)</span>",
           unsafe_allow_html=True)

col1, col2 = st.sidebar.columns([1, 8])

image = Image.open(r'./Resource/youxiang-3.png')

col1.image(image, width=25)
col2.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>bigserendipty@gmail.com</span>",
           unsafe_allow_html=True)

col1, col2 = st.sidebar.columns([1, 8])

image = Image.open(r'./Resource/xueshimao.png')

col1.image(image, width=25)
col2.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[Google Scholar](https://scholar.google.com/citations?user=cv14-cMAAAAJ&hl=zh-CN)</span>",
           unsafe_allow_html=True)

col1, col2 = st.sidebar.columns([1, 8])

image = Image.open(r'./Resource/github.png')

col1.image(image, width=25)
col2.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[GitHub](https://github.com/LittleLongFei)</span>",
           unsafe_allow_html=True)

col1, col2 = st.sidebar.columns([1, 8])

image = Image.open(r'./Resource/orcid.png')

col1.image(image, width=25)
col2.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[ORCID](https://orcid.org/my-orcid?orcid=0009-0007-1200-5801)</span>",
           unsafe_allow_html=True)

col1, col2 = st.sidebar.columns([1, 8])

image = Image.open(r'./Resource/csdn.png')

col1.image(image, width=25)
col2.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[CSDN](https://blog.csdn.net/qq_45676483?spm=1010.2135.3001.5343)</span>",
           unsafe_allow_html=True)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 主页内容



col11, col12, col13 = st.columns([3, 17, 3])
with col12:
    
    # ------------------------------------------------------------------------------------------------------------------------------------------ 简介
    
    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'><i>H-Zhang</i></span>",
               unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: black;'>Hui Zhang, male, Han nationality, born in December 1999 in Yishui, Shandong Province, is a member of the Communist Party of China, a member of the Chinese Society of Automation, and an IEEE student member. He graduated from Shandong Jianzhu University with a bachelor's degree. He ranked first in his major in academic performance for four consecutive years and won more than 60 comprehensive awards. He served as the student leader of three laboratories and the Innovation Base of the School of Information and Electrical Engineering, and later won the national Recommended Excellent Award Undergraduate graduates are eligible to study for a master's degree without taking the examination and are recommended to study for a master's degree at the School of Control Science and Engineering of Shandong University. Due to his excellent performance and outstanding scientific research ability during the master's degree, after personal application, expert recommendation, and tutor's consent, he was qualified for the Master and Doctoral Program and could directly study for a doctoral degree in the second year of the master's degree.</span>",
               unsafe_allow_html=True)
    st.write("---")
    
    # ------------------------------------------------------------------------------------------------------------------------------------------ 教育经历
    
    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'>Education</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: black;'>Sept.2022——Now: B.Sc in Physics</span>",
             unsafe_allow_html=True)
    
    # ------------------------------------------------------------------------------------------------------------------------------------------ 论文
    st.write("---")
    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'><i>Article</i></span>",
               unsafe_allow_html=True)
    
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[1] **H.Zhang**, W.Peng. Time Series Forecasting Based on Interval Type-2 Fuzzy Logic System with PSO, 2021 China Automation Congress (CAC), Beijing, China, 2021, pp. 3090-3097, doi: 10.1109/CAC53003.2021.9727414. ***EI*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[Accept]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[2] **H.Zhang**, B.Sun .et al. Interval Type-2 Fuzzy Logic System Based on Batch Normalization and Uniform Regularization with Application to Time Series Forecasting, 2023 China Automation Congress (CAC), Chongqing, China, 2023. ***EI*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[Accept]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[3] **H.Zhang**, B.Sun and W.Peng*. A novel hybrid deep fuzzy model based on gradient descent algorithm with application to time series forecasting, ***Expert Systems with Applications***, 2023, doi:10.1016/j.eswa.2023.121988, ***SCI-Q1***, ***TOP***, ***IF=8.5*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[Accept]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[4] L.Zhang, **H.Zhang**, F.Li and B.Sun*. Bi-level Optimal Design of Integrated Energy System with Synergy of Renewables, Conversion, Storage and Demand, ***IEEE TRANSACTIONS ON INDUSTRY APPLICATIONS***, ***SCI-Q2***, ***IF=4.4*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[Under review]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[5] **H.Zhang**, KV.Gao, W.Peng*. Mini-Batch Forward Automatic Differentiation based on Efficient Adaptive Optimization Algorithm for TSK Fuzzy Systems, ***IEEE TRANSACTIONS ON FUZYY SYSTEMS***, ***SCI-Q1***, ***TOP***, ***IF=11.9*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[Draft]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[6] H.Ming, **H.Zhang**, N.Cui*. Battery life estimation method based on forward adaptive width learning, ***Energy***, ***SCI-Q1***, ***TOP***, ***IF=9*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[Draft]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[7] **H.Zhang**, L.Zhang, B.Sun*. Research and application of heating pipe network modeling framework based on physical information network. ***Engineering Applications Of Artificial Intelligence***, ***SCI-Q2***, ***TOP***, ***IF=8*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[Writing]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[8] **H.Zhang**, LZ.Zhang, GY.Fan, B.Jia, B.Sun*. Hydrogen-containing integrated energy system architecture search algorithm based on reinforcement learning. ***IEEE Transactions on Industrial Informatics***, ***SCI-Q1***, ***TOP***, IF=12.3 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[Writing]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[9] MR.Qi, **H.Zhang**, XY.Li*. Research and application of interpretable prediction framework for diabetes risk based on fuzzy logic. ***International Journal of Nursing Studies***, ***SCI-Q1***, ***TOP***, ***IF=8.1*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[Writing]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[10] **H.Zhang**, B.Sun*, XF.Li. Research and application of a physically constrained data-driven modeling method for hydrogen leakage and diffusion in confined spaces. ***NATURE METHODS***, ***SCI-Q1***, ***TOP***, ***IF=48*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[Writing]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[11] JW.Zhu, **H.Zhang** .et al. Food safety detection method based on deep fuzzy system. ***LWT***, ***SCI-Q1***, ***TOP***, ***IF=6*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[Writing]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[12] GY.Fan, **H.Zhang** .et al. Food safety detection method based on deep fuzzy system. ***NATURE COMUNACATIONS***, ***SCI-Q1***, ***TOP***, ***IF=17.646*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[Writing]</span>",
             unsafe_allow_html=True)
    
    # ------------------------------------------------------------------------------------------------------------------------------------------ 论文
    st.write("---")
    
    
col21, col22, col23, col24 = st.columns([1, 0.9, 1.3, 1.6])

with col23:
    image = Image.open(r'./Resource/4.png')
    st.image(image, width=130)

col21, col22, col23, col24 = st.columns([1, 0.4, 1.3, 1.6])

with col23:
    st.caption('Copyright @ 2023, Shandong University, Jinan, China')
