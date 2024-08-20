import streamlit as st
from LLM_xunfei2 import llm_write,Core_tex,draw,Org_tex,bosssay
from data_change import query_drawing_data
import pandas as pd
from vocie3 import process_text
from test_web_api import talkwithboss

st.set_page_config(page_title='和大师对话', page_icon=' ', layout='wide')

if "messages" not in st.session_state:
                st.session_state["messages"] = []
# 假设有一个函数用于显示大师的界面
def show_master_page(master_name):
    st.header(f"{master_name}的界面")
    # 这里可以添加更多关于大师的信息和交互

# 使用自定义CSS调整侧边栏宽度
# st.markdown(
#     """
#     <style>
#         .css-1d391kg {
#             width: 300px; /* 调整这个值来改变侧边栏的宽度 */
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# 自定义CSS来设置按钮宽度
st.markdown(
    """
    <style>
        /* 为侧边栏中的所有按钮设置宽度 */
        .stSidebar .stButton>button {
            width: 100% !important; /* 设置按钮宽度为侧边栏宽度的100%，并使用!important提高优先级 */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 创建侧边栏
st.sidebar.title("大师列表")

# 大师名单
masters = ["莫奈", "毕加索", "梵高"]
master_images = {
    "莫奈": "https://sf-maas-uat-prod.oss-cn-shanghai.aliyuncs.com/outputs/f3a57a1e-2305-449a-add7-7e76390729cf_00001_.png",  # 假设图片文件名与大师名字对应
    "毕加索": "https://sf-maas-uat-prod.oss-cn-shanghai.aliyuncs.com/outputs/f3a57a1e-2305-449a-add7-7e76390729cf_00001_.png",
    "梵高": "https://sf-maas-uat-prod.oss-cn-shanghai.aliyuncs.com/outputs/f3a57a1e-2305-449a-add7-7e76390729cf_00001_.png"
}

# 初始化对话状态
if 'current_master' not in st.session_state:
    st.session_state['current_master'] = '莫奈'  # 默认与莫奈对话

# 为每个大师创建按钮，并检测哪个按钮被点击
for master in masters:
    if st.sidebar.button(master):
        st.session_state['current_master'] = master  # 更新当前对话的大师

# 创建一个容器用于对话
with st.container():
    st.markdown("""
    <style>
    .chat-container {
        display: flex;
        flex-direction: row;
        justify-content: start;
        align-items: flex-start;
    }
    .chat-box {
        width: 60%;
    }
    .image-box {
        width: 40%;
        text-align: center;  # 使图片居中显示
    }
    </style>
    <div class="chat-container">
        <div class="chat-box">
            <!-- 在这里使用Python代码动态生成对话内容 -->
        </div>
        <div class="image-box">
            <!-- 在这里插入图片 -->
            <img src="https://sf-maas-uat-prod.oss-cn-shanghai.aliyuncs.com/outputs/f3a57a1e-2305-449a-add7-7e76390729cf_00001_.png" alt="大师照片" style="max-width: 100%; height: auto;">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 动态生成对话内容
    for msg in st.session_state.messages:
        st.markdown(f'<p>{msg["role"]}: {msg["content"]}</p>', unsafe_allow_html=True)

# 注意：这里使用的图片URL需要替换为实际的图片地址。
# 如果图片存储在本地，你可能需要使用Streamlit的静态文件夹或者其他方法来提供图片的URL。
# 根据当前对话的大师显示对应界面
show_master_page(st.session_state['current_master'])
for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
# 原有的聊天逻辑
if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    msg = talkwithboss(st.session_state['current_master'],prompt)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)


# # 使用columns创建两个并排的列
# col1, col2 = st.columns(2)
# # 在col1中显示对话
# with col1:
#     for msg in st.session_state.messages:
#             st.chat_message(msg["role"]).write(msg["content"])
#     # 原有的聊天逻辑
#     if prompt := st.chat_input():
#         st.chat_message("user").write(prompt)
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         msg = talkwithboss(st.session_state['current_master'],prompt)
#         st.session_state.messages.append({"role": "assistant", "content": msg})
#         st.chat_message("assistant").write(msg)


# # 在col2中显示当前大师的照片
# with col2:
#     st.image(master_images[st.session_state['current_master']], caption=st.session_state['current_master'])




# st.header("与莫奈对话")
# st.write("你好，我是莫奈，很高兴能和你对话")
# st.write( "左边是我的生平往事，希望你对我已经了解了")
# if "messages" not in st.session_state:
#                 st.session_state["messages"] = []
# #st.session_state["messages"].append({"role": "assistant", "content": "你好，我是莫奈，很高兴能和你对话"})
# #st.session_state["messages"].append({"role": "assistant", "content": "左边是我的生平往事，希望你对我已经了解了"})
# for msg in st.session_state.messages:
#         st.chat_message(msg["role"]).write(msg["content"])
# #if prompt := st.chat_input():

#                 # if not openai_api_key:
#                 #     st.info("Please add your OpenAI API key to continue.")
#                 #     st.stop()
#                 #openai_api_key = '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'
#                 #client = OpenAI(api_key=openai_api_key)
#                 #st.session_state.messages.append({"role": "user", "content": prompt})
# if prompt := st.chat_input():
#     st.chat_message("user").write(prompt)
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     #response1 = respond2(prompt)
#     #response1 = RAG_LLM(prompt)
#     #response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
#     msg = bosssay(prompt)
#     #msg = response.choices[0].message.content
#     #msg = response.get_result()
#     #msg = prompt + "你在说什么"
#     st.session_state.messages.append({"role": "assistant", "content": msg})
#     st.chat_message("assistant").write(msg)
#     #st.chat_message("assistant").write("你在说什么")

# # else:
# #     st.write("")

