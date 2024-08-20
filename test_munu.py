import pages as pgs
import csv
import streamlit as st
import os
import json
import pandas as pd
from streamlit_option_menu import option_menu


st.set_page_config(page_title='十万个为什么', page_icon=' ', layout='wide')
# 创建侧边栏菜单
#menu = st.sidebar.radio("菜单", ('首页', '页面1', '页面2'))

# 根据选择的菜单项显示内容
# if menu == '首页':
#     st.write("欢迎来到首页！")
# elif menu == '页面1':
#     st.write("这是页面1。")
# elif menu == '页面2':
#     st.write("这是页面2。")




# with st.sidebar:
#     page = option_menu(
#         menu_title='企业集成平台',
#         options=['首页', '业务应用', '财务应用', '报表应用', '系统管理'],
#         default_index=0,
#         menu_icon='windows',
#         icons=['house', 'people', 'piggy-bank', 'clipboard-data', 'gear']
#     )

# functions = {
#     '首页': pgs.home,
#     '业务应用': pgs.business_app,
#     '财务应用': pgs.financial_app,
#     '报表应用': pgs.report_app,
#     '系统管理': pgs.system_management
# }

# go_to = functions.get(page)

# if go_to:
#     go_to()

selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2

selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)

if st.session_state.get('switch_button', False):
    st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) + 1) % 4
    manual_select = st.session_state['menu_option']
else:
    manual_select = None
    
selected4 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    orientation="horizontal", manual_select=manual_select, key='menu_4')
st.button(f"Move to Next {st.session_state.get('menu_option', 1)}", key='switch_button')
selected4

def on_change(key):
    selection = st.session_state[key]
    st.write(f"Selection changed to {selection}")
    
selected5 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
                        icons=['house', 'cloud-upload', "list-task", 'gear'],
                        on_change=on_change, key='menu_5', orientation="horizontal")
selected5