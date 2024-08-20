import streamlit as st
# 设置页面配置
st.set_page_config(page_title='向大师学习绘画', page_icon='🎨', layout='wide')


# # 创建两列，第一列宽度较小，作为模拟的侧边栏
# sidebar_col, main_col = st.columns([1, 4])
# 创建三列，中间的列作为分割线
left_col, divider_col, right_col = st.columns([2, 1, 5])


# 在中间的列中添加一条垂直分割线
with divider_col:
    st.markdown('''
        <style>
            .divider {
                border-left: 2px solid #ccc;
                height: 100vh;
            }
        </style>
        <div class="divider"></div>
        ''', unsafe_allow_html=True)

# 在模拟的侧边栏中添加内容
with left_col:
    st.write("模拟侧边栏")
    if st.button("首页"):
        st.session_state['page'] = '首页'
    if st.button("画廊"):
        st.session_state['page'] = '画廊'
    if st.button("关于"):
        st.session_state['page'] = '关于'

# 在主内容区根据条件展示内容
with right_col:
    if st.session_state.get('page') == '首页':
        st.header("欢迎来到首页")
        # 首页内容
    elif st.session_state.get('page') == '画廊':
        st.header("画廊展示")
        # 画廊内容
    elif st.session_state.get('page') == '关于':
        st.header("关于我们")
        # 关于页面内容
# import streamlit as st
# from streamlit_option_menu import option_menu  # 确保已经安装了streamlit-option-menu

# # 设置页面配置
# st.set_page_config(page_title='向大师学习绘画', page_icon='🎨', layout='wide')

# # 在页面顶部创建一个选项菜单作为主导航
# selected = option_menu(None, ["首页", "画廊", "关于"], 
#                         icons=["house", "image", "info"], 
#                         menu_icon="cast", 
#                         default_index=0, 
#                         orientation="horizontal",
#                         styles={
#                             "container": {"padding": "0!important", "background-color": "#fafafa"},
#                             "icon": {"color": "orange", "font-size": "25px"}, 
#                             "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "padding":"10px", "width": "200px"},
#                             "nav-link-selected": {"background-color": "green"},
#                         })

# # 根据选项菜单的选择显示不同的页面内容
# if selected == "首页":
#     st.header("欢迎来到首页")
#     # 首页内容
# elif selected == "画廊":
#     st.header("画廊展示")
#     # 画廊内容
# elif selected == "关于":
#     st.header("关于我们")
#     # 关于页面内容



# # 如果你需要在页面上添加其他导航或信息，可以直接在主页面上添加，而不是使用侧边栏
# # 例如，添加一个额外的信息区域
# st.info("这是一个额外的信息区域，可以放置任何你想要的内容。")

# import streamlit as st
# from streamlit_option_menu import option_menu  # 确保已经安装了streamlit-option-menu

# # 设置页面配置
# st.set_page_config(page_title='向大师学习绘画', page_icon='🎨', layout='wide')

# # 使用侧边栏放置标题和其他可能的侧边栏元素
# with st.sidebar:
#     st.title("大师列表")
#     # 你可以在这里添加更多的侧边栏元素，比如过滤器或者链接等

# # 在页面顶部创建一个选项菜单作为主导航
# selected = option_menu("主导航", ["首页", "画廊", "关于"], icons=["house", "image", "info"], menu_icon="cast", default_index=0, orientation="horizontal")

# # 根据选项菜单的选择显示不同的页面内容
# if selected == "首页":
#     # 创建左右两列
#     col1, col2 = st.columns(2)

#     with col1:
#         user_input = st.text_input("请输入你的绘画创意：")
#         size_option = st.selectbox(
#             "选择图片尺寸",
#             ["1024x576", "1024x1024", "576x1024", "512x768", "768x512"]
#         )
#         # 这里继续你的代码逻辑
# elif selected == "画廊":
#     st.write("这里可以展示画廊内容")
# elif selected == "关于":
#     st.write("这里可以展示关于页面的内容")