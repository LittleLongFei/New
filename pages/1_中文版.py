

import streamlit as st

from PIL import Image

# page Configuration

st.set_page_config(
    page_title="Hui-Zhang",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 导航栏
image = Image.open(r'./Resource/6.png')
st.sidebar.image(image, width=300)

st.sidebar.title("张辉")
st.sidebar.caption("<span style='font-family: Arial; font-size: 18px; color: gray;'>H.Zhang</span>",
                   unsafe_allow_html=True)
st.sidebar.write("<span style='font-family: Times New Roman; font-size: 18px;'>山东大学, 控制科学与工程学院</span>",
                 unsafe_allow_html=True)

# --------------------------------------------------------------------- 导航栏 ---- 位置/邮箱等信息

st.sidebar.write("---")


# ------------------------------------------------------------- 位置

col1, col2 = st.sidebar.columns([1, 8])

image = Image.open(r'./Resource/weizhi-3.png')

col1.image(image, width=30)
col2.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>中国, 济南</span>",
           unsafe_allow_html=True)

# ------------------------------------------------------------- 主页

col1, col2 = st.sidebar.columns([1, 8])

image = Image.open(r'./Resource/lianjie-2.png')

col1.image(image, width=25)
col2.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[个人主页](https://www.streamlit.io/)</span>",
           unsafe_allow_html=True)

col1, col2 = st.sidebar.columns([1, 8])

# ------------------------------------------------------------- 邮箱

image = Image.open(r'./Resource/youxiang-3.png')

col1.image(image, width=25)
col2.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>bigserendipty@gmail.com</span>",
           unsafe_allow_html=True)

col1, col2 = st.sidebar.columns([1, 8])

image = Image.open(r'./Resource/xueshimao.png')

col1.image(image, width=25)
col2.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[谷歌学术档案](https://scholar.google.com/citations?user=cv14-cMAAAAJ&hl=zh-CN)</span>",
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


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 主页内容



col11, col12, col13 = st.columns([3, 17, 3])
with col12:

    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'>张 辉</span>",
             unsafe_allow_html=True)
    
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: black;'> 张辉，男，汉族，1999年12月生，山东沂水人，中共党员，中国自动化学会会员，IEEE student member。2018年考入山东建筑大学信息与电气工程学院物联网工程专业，连续四年学习成绩位列专业第一，曾获得山东建筑大学“十大自强不息优秀学生”、国家奖学金等综合性奖励60余项，担任三个实验室以及信息与电气工程学院创新基地学生负责人。于2022年获得国家“推荐优秀本科毕业生免试攻读硕士研究生”资格，保送至山东大学控制科学与工程学院攻读硕士学位。由于硕士阶段表现优异，科研能力突出，经个人申请、专家推荐、导师同意，获得山东大学“硕博连读”资格，于2024年直接攻读工学博士学位。</span>",
             unsafe_allow_html=True)

    # ------------------------------------------------------------------------------------------------------------------------------------------ 教育经历

    st.write("---")
    
    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'>教育经历</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: black;'>2022年9月——至今: 于山东大学控制科学与工程学院攻读工学博士学位(控制科学与工程,硕博连读), 中国, 山东, 济南;</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: black;'>2018年9月——2022年6月: 于山东建筑大学信息与电气工程学院学院获得工学学士学位(物联网工程), 中国, 山东, 济南;</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: black;'>2015年9月——2018年6月: 高中毕业于沂水县第一中学, 中国, 山东, 沂水;</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: black;'>2015年9月——2012年6月: 初中毕业于黄山铺镇初级中学, 中国, 山东, 沂水;</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: black;'>2012年9月——2006年6月: 小学毕业于黄山铺镇中心小学, 中国, 山东, 沂水;</span>",
             unsafe_allow_html=True)

    # ------------------------------------------------------------------------------------------------------------------------------------------ 论文
    st.write("---")
    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'>论 文</span>",
             unsafe_allow_html=True)
    
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[1] **张辉**, 基于深度模糊系统方法的多变量时间序列预测方法研究及应用, 工学学士学位论文, 指导老师:彭伟, 2022年优秀学士学位论文 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已发表]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[2] **H.Zhang**, W.Peng. Time Series Forecasting Based on Interval Type-2 Fuzzy Logic System with PSO, 2021 China Automation Congress (CAC), Beijing, China, 2021, pp. 3090-3097, doi: 10.1109/CAC53003.2021.9727414. ***EI*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已发表]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[3] **H.Zhang**, B.Sun .et al. Interval Type-2 Fuzzy Logic System Based on Batch Normalization and Uniform Regularization with Application to Time Series Forecasting, 2023 China Automation Congress (CAC), Chongqing, China, 2023. ***EI*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已发表]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[4] **H.Zhang**, B.Sun and W.Peng*. A novel hybrid deep fuzzy model based on gradient descent algorithm with application to time series forecasting, ***Expert Systems with Applications***, 2023, doi:10.1016/j.eswa.2023.121988, ***SCI-Q1***, ***TOP***, ***IF=8.5*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已发表]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[5] LZ.Zhang, **H.Zhang**, F.Li and B.Sun*. Bi-level Optimal Design of Integrated Energy System with Synergy of Renewables, Conversion, Storage and Demand, ***IEEE TRANSACTIONS ON INDUSTRY APPLICATIONS***, ***SCI-Q2***, ***IF=4.4*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[审稿中]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[6] **H.Zhang**, W.Peng*, KV.Gao, GY.Fan. Mini-Batch Forward Automatic Differentiation based on Efficient Adaptive Optimization Algorithm for TSK Fuzzy Systems, ***IEEE TRANSACTIONS ON FUZYY SYSTEMS***, ***SCI-Q1***, ***TOP***, ***IF=11.9*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[审稿中]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[7] H.Ming, **H.Zhang**, N.Cui*. Battery life estimation method based on forward adaptive width learning, ***Energy***, ***SCI-Q1***, ***TOP***, ***IF=9*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[准备提交]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[8] **H.Zhang**, LZ.Zhang, B.Jia, GY.Fan, B.Sun*. Hydrogen-containing integrated energy system architecture search algorithm based on reinforcement learning. ***IEEE TRANSACTIONS ON INDUUSTRIAL INFORMATIONS***, ***SCI-Q1***, ***TOP***, IF=12.3 </span><span style='font-family: Times New Roman; font-size: 19px; color: red;'>[正在写]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[9] **H.Zhang**, L.Zhang, GY.Fan, J.Chen, B.Sun*. Research and application of heating pipe network modeling framework based on physical information network. ***Engineering Applications of Artificial Intelligence***, ***SCI-Q2***, ***TOP***, ***IF=8*** </span><span style='font-family: Times New Roman; font-size: 19px; color: red;'>[正在写]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[10] GY.Fan, **H.Zhang**, B.Sun*. Economic Modeling and Analysis of China's Hydrogen Energy System. ***Nature Communications***, ***SCI-Q1***, ***TOP***, ***IF=16.6*** </span><span style='font-family: Times New Roman; font-size: 19px; color: red;'>[正在写]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[11] **H.Zhang**, JX.Zhang, B.Sun*, XF.Li. Research and application of a physically constrained data-driven modeling method for hydrogen leakage and diffusion in confined spaces. ***NATURE METHODS***, ***SCI-Q1***, ***TOP***, ***IF=48*** </span><span style='font-family: Times New Roman; font-size: 19px; color: green;'>[调试中]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[12] MR.Qi, **H.Zhang**, XY.Li*. Research and application of interpretable prediction framework for diabetes risk based on fuzzy logic. ***International Journal of Nursing Studies***, ***SCI-Q1***, ***TOP***, ***IF=8.1*** </span><span style='font-family: Times New Roman; font-size: 19px; color: green;'>[调试中]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'></span>",
             unsafe_allow_html=True)

    # ------------------------------------------------------------------------------------------------------------------------------------------ 论文
    st.write("---")
    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'>专 利</span>",
             unsafe_allow_html=True)

    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[1] **张辉**, 聂浩, 齐美荣, 侯振华, 一种基于物联网的安防设备, 实用新型专利 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已授权]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[2] **张辉**, 聂浩, 齐美荣, 侯振华, 一种基于物联网的快递收发系统, 实用新型专利 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已授权]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[3] 陶亮, 王锐霖,  **张辉**, 孙佳杰, 张良, 一种手持式智能残留农药检测仪以及检测方法, 国家发明专利 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已公开]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[4] 孙波, **张辉**, 张立志, 一种含氢综合能源系统的全流程一体化设计方法及系统, 国家发明专利 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已受理]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[5] 孙波, **张辉**, 一种氢气泄漏扩散过程建模方法及系统, 国家发明专利 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已受理]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[6] 孙波, 李志龙, **张辉**, 一种基于自适应PINN的综合能源数字孪生建模方法及系统, 国家发明专利 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已受理]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[7] 孙波, 张良, **张辉**,一种基于物理信息神经网络的供热管网建模方法及系统, 国家发明专利 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已受理]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'></span>",
             unsafe_allow_html=True)
    
    # ------------------------------------------------------------------------------------------------------------------------------------------ 软件著作权
    st.write("---")
    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'>软件著作权</span>",
             unsafe_allow_html=True)

    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[1] **张辉**, 彭伟, 侯振华, 计算机软件著作权《基于ID3算法的大学生恋爱软件V1.0》 计算机软件著作权 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已授权]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[2] **张辉**, 计算机软件著作权, 《基于C4.5算法的寻亲软件V1.0》, 计算机软件著作权 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[已授权]</span>",
             unsafe_allow_html=True)
    
    # ------------------------------------------------------------------------------------------------------------------------------------------ 软件著作权
    st.write("---")
    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'>标 准</span>",
             unsafe_allow_html=True)

    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[1] 潘凤文, 孙波, 张立志, 张全军, 刘洋, **张辉**, 吴睿, 杨锋, 王迎波, 秦顺顺, 冯美丽, 含氢分布式综合能源系统运行优化指南, ***地方/行业标准*** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[专家论证中]</span>",
             unsafe_allow_html=True)
    
    # ------------------------------------------------------------------------------------------------------------------------------------------ 软件著作权
    st.write("---")
    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'>项 目</span>",
             unsafe_allow_html=True)

    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[1] **国家电网科技专项**, 多能互补综合能源系统协同优化控制研究, 经费**300万**元, 2021-2023 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[参与,项目骨干,已结题]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[2] **国家重点研发计划项目氢能专项**, 管道氢气在城镇供能领域关键技术研究与规模应用, 经费**5.15亿**元 2022-2026 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[参与,项目骨干,在研]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[3] **国家重点研发计划项目氢能专项**, 氢能多场景深度融合及智慧管控技术研究与示范应用, 经费**2.05亿**元 2023-2027 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[参与,项目骨干,在研]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[4] **国家重点研发计划项目政府间国际科技创新合作重点专项**, 氢能多场景深度融合及智慧管控技术研究与示范应用, 经费**2.05亿**元 2023-2027 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[参与,项目骨干,在研]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[5] **国家级大学生创新创业训练计划项目**, 基于区间二型模糊逻辑的建筑能耗预测平台, 经费**2万**元 2022-2024 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[参与,指导,在研]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[6] **省级大学生创新创业训练计划项目**, 基于实景投影的农药残留检测技术, 经费**1万**元 2020-2021 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[主持,已结题]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[7] **开放性实验项目**, 基于STM32的智能晾衣架控制系统, 经费**1千**元 2019-2020 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[主持,已结题]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[8] **开放性实验项目**, 基于Arduino的创新机器人开发平台, 经费**1千**元 2020-2021 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[主持,已结题]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[9] **开放性实验项目**, 简易无接触温度测量与身份识别防疫装置, 经费**1千**元 2020-2021 </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[主持,已结题]</span>",
             unsafe_allow_html=True)

    # ------------------------------------------------------------------------------------------------------------------------------------------ 软件著作权
    st.write("---")
    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'>奖学金</span>",
             unsafe_allow_html=True)

    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[1] 2022年**山东大学新生入学奖学金** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[¥3000]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[2] 2020-2021学年 **国家奖学金** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[¥8000]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[3] 2019-2020学年 **国家励志奖学金** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[¥5000]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[4] 2021-2022学年 **第二届泉城奖学金** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[¥3000,全校并列第二]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[5] 2020-2021学年 **山发集团创新创业奖学金** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[¥2000]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[6] 2021-2022学年 **山发集团创新创业奖学金** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[¥2000]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[7] 2020年度 **山东建筑大学十大自强不息优秀学生奖学金** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[¥5000,全校第十]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[8] 2019年度 **山东建筑大学校级建业之星学习先进个人** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[¥1200]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[9] 2018-2019学年 **优秀学生二等奖学金** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[¥600]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[10] 2019-2020学年 **优秀学生二等奖学金** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[¥600]</span>",
             unsafe_allow_html=True)
    st.write("<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[11] 2020-2021学年 **优秀学生一等奖学金** </span><span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[¥1200]</span>",
             unsafe_allow_html=True)
             
    # ------------------------------------------------------------------------------------------------------------------------------------------ 软件著作权
    st.write("---")
    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'>其他荣誉</span>",
             unsafe_allow_html=True)

    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[1] 山东建筑大学2022届优秀毕业生</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[2] 2022届优秀学士学位论文(毕业论文以及答辩成绩全学院第一) </span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[3] 山东建筑大学2019寒假社会实践活动优秀个人</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[4] 山东建筑大学2020暑期社会实践活动优秀个人</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[5] 2018-2019年度山东建筑大学“优秀团员”</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[6] 2019-2020年度山东建筑大学“优秀团员”</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[7] 2020-2021年度山东建筑大学“优秀团员”</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[8] 2018-2019年度山东建筑大学“优秀学生”</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[9] 2019-2020年度山东建筑大学“优秀学生”</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[10] 2020-2021年度山东建筑大学“优秀学生”</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[11] 2019-2020年度山东建筑大学“优秀学生干部”</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[12] 2020-2021年度山东建筑大学“优秀学生干部”</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[13] 2019-2020年度山东建筑大学“优秀学生干部标兵”</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[14] 2020-2021年度山东建筑大学“优秀学生干部标兵”</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[15] 2020-2021年度山东建筑大学“优秀学生标兵”</span>",
        unsafe_allow_html=True)
    
    # ------------------------------------------------------------------------------------------------------------------------------------------ 软件著作权
    st.write("---")
    st.write("<span style='font-family: Times New Roman; font-size: 30px; color: black;'>竞赛获奖</span>",
             unsafe_allow_html=True)

    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[1] 第十四届iCAN国际创新创业大赛国家级三等奖, iCAN20201227J69 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[国家级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[2] 2020年TI杯全国大学生电子设计竞赛山东赛区一等奖 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[省级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[3] 第十二届大学生科技节-科技馆展品创意与设计大赛省级一等奖《基于Arduino的激光雕刻机》, SDUC202051-1-0044 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[省级,第二作者]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[4] 第十二届大学生科技节-科技馆展品创意与设计大赛省级一等奖《基于Arduino的智能避障车》, SDUC202051-1-0049 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[省级,第一作者]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[5] “科创青春，未来我行”科普展品征集活动省级一等奖，SU10001468 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[省级,第二作者]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[6] “科创青春，未来我行”科普展品征集活动省级二等奖, SU10001466 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[省级,第一作者]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[7] 第十四届iCAN国际创新创业大赛山东赛区省级二等奖, iCAN2020-SD-18542 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[省级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[8] 第十一届大学生科技节-科技馆展品创意与设计大赛省级三等奖, SDUC201961-3-0032 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[省级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[9] 第七届山东省物联网创造力大赛省级二等奖, SDUC202007-2-0113 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[省级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[10] 第一届中国·山东数字经济优秀项目省级三等奖 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[省级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[11] 第一届中国·山东数字经济优秀项目春苗奖以及奖金, 奖金¥5000 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[省级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[12] 第十四届大学生科技节-科技馆展品创意与设计大赛省级优秀奖《基于STM32的函数信号发生器》 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[省级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[13] 第十四届大学生科技节-科技馆展品创意与设计大赛省级优秀奖《基于STM32的示波器硬件设计与实现》<span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[省级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[14] “华为杯”山东建筑大学第六届单片机大赛校赛一等奖、华为杯三等奖 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[校级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[15] 建行杯第六届山东省“互联网+”山东建筑大学校赛二等奖 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[校级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[16] 山东建筑大学2020年“创青春”创业大赛校级铜奖 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[校级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[17] 第七届山东省大学生科技创新大赛—山东建筑大学校赛三等奖 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[校级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[18] 山东建筑大学第十二届“挑战杯”创业计划赛校级铜奖 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[校级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[19] 建行杯第六届山东省“互联网+”山东建筑大学校赛二等奖<span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[校级,项目负责人]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[20] 山东建筑大学“喜迎七十华诞与祖国同在同行”征文比赛 校级三等奖 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[院级]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[21] 信息与电气工程学院第三届职业生涯规划演讲比赛 院级三等奖 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[院级]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[22] 信息与电气工程学院“铭记一二九，共筑中国梦”征文比赛 院级二等奖 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[院级]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[23] 信息与电气工程学院党史答题活动 院级一等奖 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[院级]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[24] 计算机科学与技术学院“滑翔机竞速大赛” 院级一等奖 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[院级]</span>",unsafe_allow_html=True)
    st.write(
        "<span style='font-family: Times New Roman; font-size: 19px; color: gray;'>[25] 2019年零“艾”活动优秀志愿者 <span style='font-family: Times New Roman; font-size: 19px; color: blue;'>[院级]</span>", unsafe_allow_html=True)
             
    st.write("---")

col21, col22, col23, col24 = st.columns([1, 0.9, 1.3, 1.6])

with col23:
    image = Image.open(r'./Resource/4.png')
    st.image(image, width=130)

col21, col22, col23, col24 = st.columns([1, 0.4, 1.3, 1.6])

with col23:
    st.caption('Copyright @ 2023, Shandong University, Jinan, China')
