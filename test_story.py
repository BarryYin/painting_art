import streamlit as st
from LLM_xunfei2 import llm_write,Core_tex,draw,Org_tex
from data_change import query_drawing_data
import pandas as pd
from vocie3 import process_text

# 设置页面为宽屏模式
st.set_page_config(layout="wide")

if 'question_1' not in st.session_state:
        st.session_state['question_1'] = ""
if 'data_1' not in st.session_state:
        st.session_state['data_1'] = pd.DataFrame()
if 'answer_01' not in st.session_state:
        st.session_state['answer_01'] = True

st.session_state['data_1'] = query_drawing_data()
new_list = []
#使用循环将drawing_names中的每个值添加到新列表中
for name in st.session_state['data_1']['drawing_name']:
    new_list.append(name)
# 在expander下方增加一个下拉框，让用户从一批问题中选择
# questions = ["莫奈的故事", "高更的故事", "梵高的绘画风格", "法国浪漫主义绘画"]
# selected_question = st.selectbox("请选择你感兴趣的问题：", questions)
        
#questions = ["《自由引导人民》的艺术赏析", "莫奈《睡莲》的艺术赏析", "梵高《向日葵》的故事", "让·安东尼·华多《小丑》的故事"]
questions = new_list
selected_question = st.selectbox("请选择你感兴趣的问题：", questions)

drawing_url = ''
Works_analysis = ''
story = ''

if 'drawing_url' not in st.session_state:
        st.session_state['drawing_url'] = ""

if 'Works_analysis' not in st.session_state:
        st.session_state['Works_analysis'] = ""

if 'story' not in st.session_state:
        st.session_state['story'] = ""

# 遍历DataFrame中的每一行
for index, row in st.session_state['data_1'].iterrows():
    # 检查'drawing_name'列的值是否与selected_question相匹配
    if row['drawing_name'] == selected_question:
        # 如果匹配，提取所需的其他数据
        st.session_state['drawing_url'] = row['drawing_url']
        st.session_state['Works_analysis'] = row['Works_analysis']
        st.session_state['story'] = row['story']
        break  # 匹配成功后退出循环

st.session_state['answer_01'] = True
st.session_state['question_1'] = selected_question
if st.session_state['answer_01']:

    with st.expander("关于这部作品的赏析原文"):
    # 在这里，你可以根据用户的输入显示不同的内容
    # 例如，简单地回显用户输入的内容
        st.write(f"你输入的内容是：{st.session_state['Works_analysis']}")
    col1, col2 = st.columns([1,1]) 
    with col1:
        st.image(st.session_state['drawing_url'], width=500)
    with col2:
        st.write(st.session_state['story'])
        #process_text(st.session_state['story'])
        #st.write(Org_tex(st.session_state['question_1']))
        #st.write(llm_write(st.session_state['question_1']))
    st.session_state['answer_01'] = False

