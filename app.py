# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline
from streamlit_option_menu import option_menu
import pages as pgs
from vocie3 import process_text
from LLM_unified import llm_write,Core_tex,draw,Org_tex,bosssay,is_right,promptajust
from data_change import query_drawing_data
import pandas as pd
from vocie3 import process_text
from artist_chat_unified import talkwithboss
from testimage import create_iamge
from data_change import get_images_from_excel
from streamlit_pills import pills
from audiorecorder import audiorecorder
from dwspark.models import Audio2Text
from modify_mp3 import modify_mp3_file
from dwspark.config import Config
import base64
from postMaker import postMaker
from datetime import datetime
import time

# 加载系统环境变量：SPARKAI_APP_ID、SPARKAI_API_KEY、SPARKAI_API_SECRET
config = Config('3a115b20', '9d1b7a738c3e63a79656df4222d12cef','ZGMyMzA3MGFlM2MzM2UxZWE1YTJhYjgw')

st.set_page_config(page_title="法国绘画展-瓦力AI解读", layout="wide")

def convert_mp3_to_base64(mp3_file_path):
            with open(mp3_file_path, "rb") as mp3_file:
                # 读取文件内容
                mp3_data = mp3_file.read()
                # 转换为 Base64 编码的字符串
                base64_mp3 = base64.b64encode(mp3_data).decode('utf-8')
                return base64_mp3
            
def get_question(n):
    # 假设我们有一个包含问题及其答案的列表
    questions_with_answers = [
        #{"question": "法国有一位艺术家，他的作品《草地上的午餐》挑战了当时的社会规范，以其大胆的构图和对光影的处理而闻名，这位艺术家是谁？ 提示：这位艺术家是印象派的先驱之一，他的作品常常描绘户外场景。", "pic":"http://lingganjia.com/images/picture/116321.jpg","answer": "马奈"},
        
        {"question": "哪位法国画家以他的《睡莲》系列而闻名，这些作品描绘了自家花园中的睡莲池塘?","pic":"https://file.nbfox.com/wp-content/uploads/2020/03/11/20200311201150-5e694606359e6.jpg", "answer": "莫奈"},
        {"question": "《拉斐尔与弗纳利娜》，是一幅广受赞誉的绘画作品，它不仅展现了画家卓越的技巧，也体现了新古典主义流派的核心美学理念。此画以其精致的细节刻画和和谐的色彩搭配著称。画中的人物形象生动而优雅，构图严谨而富有节奏感，充分展现了画家对人物肖像和情感表达的深刻把握。请问这幅画的作者是谁", "pic":"http://lingganjia.com/images/picture/107566.jpg","answer": "安格尔"},
        {"question": "欧仁·德拉克罗瓦，创作了一幅描绘19世纪法国七月革命场景的画作，画面中心是一位手持国旗的女性形象，她象征着自由与希望，引领着民众前进。请问此画的名字是什么","pic":"https://img.allhistory.com/5ec4c325d7f8a70001faf009.jpg", "answer": "自由引导人民"},
        {"question": "雅克.路易.大卫有一副著名的画作，描绘了一位法国的传奇人物在1800年率领法军穿越阿尔卑斯山的情景。在画面中，该传奇人物骑着马，身披红色斗篷，显得英勇无畏。他的士兵们紧随其后，共同克服困难，成功穿越了险峻的阿尔卑斯山。请问画中这位传奇人物是谁", "pic":"https://tupian.sioe.cn/uploadfile/201410/18/602139791.jpg","answer": "拿破仑"},
        {"question": "法国有一位后印象派画家，以其使用鲜明色彩和厚重笔触而知名，他的作品《星夜》是世界著名的艺术品，这位画家是谁？", "pic":"http://lingganjia.com/images/picture/100320.jpg","answer": "梵高"},
        #{"question": "法国有一位艺术家，他的作品《阿维尼翁的少女》被认为是立体主义的开端，这位艺术家是谁？提示：这位艺术家的画作打破了传统的透视规则，用几何形状重新组合了画面。", "answer": "毕加索"},
        #{"question": "18世纪上半叶，法国居统治地位的是宫廷喜好的冗繁浮华风格，这种风格描绘全裸或半裸的妇女和精美华丽的装饰。追求轻盈纤巧，精致细腻的风格，趣味甜俗，充满胭脂粉气。这种艺术的名字？", "answer": "洛可可"},
        
    ]
    # 根据 `n` 的值返回相应的问题和答案
    # 注意: 这里假设 `n` 的值不会超过问题列表的长度
    return questions_with_answers[n]


def main():

    selected2 = option_menu(None, ["艺术画廊", "画语新编", "大师对话", '绘梦成真', '画师认证'], 
    icons=['house', 'pen', "people-fell", 'image', 'book'], 
      orientation="horizontal") #default_index=0,menu_icon="cast",
    #selected2

    # selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    # icons=['house', 'cloud-upload', "list-task", 'gear'], 
    # menu_icon="cast", default_index=0, orientation="horizontal")


    if selected2 == "艺术画廊":
        st.session_state.page = '艺术画廊'
        # 添加居中且加粗的标题
        # 添加居中且加粗的标题
        st.markdown("<h1 style='text-align: center; font-weight: bold;'>法绘华章 -- 法国三百年绘画展</h1>", unsafe_allow_html=True)
        #st.markdown("<h1 style='text-align: center; font-weight: bold;'>法国三百年绘画经典作品展</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; font-weight: normal;'>第九届上海图书馆开放数据竞赛作品</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; font-weight: normal;'>献礼中法建交60周年</h1>", unsafe_allow_html=True)
        # load data
        # 绘制一条横线
        st.markdown("---")
        with open('example1.json', "r") as f:
            data1 = f.read()

        # render timeline
        timeline(data1, height=800)

        # load data
        with open('example2.json', "r") as f:
            data2 = f.read()

        # render timeline
        timeline(data2, height=800)

        # load data
        with open('example3.json', "r") as f:
            data3 = f.read()

        # render timeline
        timeline(data3, height=800)

        # load data
        with open('example4.json', "r") as f:
            data4 = f.read()

        # render timeline
        timeline(data4, height=800)

        # load data
        with open('example5.json', "r") as f:
            data5 = f.read()

        # render timeline
        timeline(data5, height=800)

        # load data
        with open('example6.json', "r") as f:
            data6 = f.read()

        # render timeline
        timeline(data6, height=800)

        # load data
        with open('example7.json', "r") as f:
            data7 = f.read()

        # render timeline
        timeline(data7, height=800)
    
    elif selected2 == "画语新编":
        st.session_state.page = '画语新编'
        
        st.markdown("<h1 style='text-align: center; font-weight: bold;'>画语新编</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; font-weight: normal;'>法国名画新解读</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; font-weight: normal;'>选择一副名画，进行AI解读创作，形成新的绘本故事</h1>", unsafe_allow_html=True)
        # 绘制一条横线
        st.markdown("---")
        # load data

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

        questions = new_list
        selected_question = st.selectbox("请选择一副名画作品：", questions)


        if 'drawing_url' not in st.session_state:
                st.session_state['drawing_url'] = ""

        if 'Works_analysis' not in st.session_state:
                st.session_state['Works_analysis'] = ""

        if 'story' not in st.session_state:
                st.session_state['story'] = ""

        if 'voicefile' not in st.session_state:
                st.session_state['voicefile'] = ""

        # 遍历DataFrame中的每一行
        for index, row in st.session_state['data_1'].iterrows():
            # 检查'drawing_name'列的值是否与selected_question相匹配
            if row['drawing_name'] == selected_question:
                # 如果匹配，提取所需的其他数据
                st.session_state['drawing_url'] = row['drawing_url']
                st.session_state['Works_analysis'] = row['Works_analysis']
                st.session_state['story'] = row['story']
                st.session_state['voicefile'] = row['voicefile']
                break  # 匹配成功后退出循环

        # 假设你的 MP3 文件的 URL 是 'http://example.com/my_audio.mp3'
        #audio_url = 'output_20240820132046.mp3'
       
        # 将你的 MP3 文件读取为二进制数据
        
            
        

        st.session_state['answer_01'] = True
        st.session_state['question_1'] = selected_question
        if st.session_state['answer_01']:
            col1, col2, col3 = st.columns([3,0.1,3]) 
            with col1:
                st.markdown("""
                <style>
                .container {
                        width: 530px;
                }
                </style>
                """, unsafe_allow_html=True)
                with st.container():
                        st.image(st.session_state['drawing_url'])
                        st.markdown("""
                        <style>
                        .css-1x0zj2k {
                        max-width: 20%;
                        }
                        </style>
                        """, unsafe_allow_html=True)
                        with st.expander("关于这部作品的赏析原文"):
                            st.write(f"{st.session_state['Works_analysis']}")
                                
            with col2:
                st.markdown('''
                <style>
                    .divider {
                        border-left: 2px solid #ccc;
                        height: 100vh;
                    }
                </style>
                <div class="divider"></div>
                ''', unsafe_allow_html=True)
            with col3:
                # 使用 st.markdown 来嵌入 HTML 代码，其中包含一个 audio 标签用于播放 MP3 文件
                audio_url =  st.session_state['voicefile']
                print(audio_url)
                base64_mp3 = convert_mp3_to_base64(audio_url)
                #print(base64_mp3)
                # 生成一个唯一的时间戳
                #timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                st.audio(audio_url, format='audio/mp3')
                # st.markdown(f"""
                # <audio controls>
                #          <source src="data:audio/mp3;base64,{audio_url}" type="audio/mp3">
                #         Your browser does not support the audio element.
                #         <br/>
                # </audio>
                # """, unsafe_allow_html=True)

                st.write(st.session_state['story'])
            st.session_state['answer_01'] = False
    
    elif selected2 == "大师对话":
        st.session_state.page = '大师对话'
        if "messages" not in st.session_state:
                        st.session_state["messages"] = []
        # # 假设有一个函数用于显示大师的界面
        def show_master_page(master_name):
            st.header(f"{master_name}的界面")

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

        # 大师名单
        masters = ["莫奈", "毕加索", "梵高","高更","安格尔","弗朗索瓦·米勒","马奈"]
        master_images = {
            "莫奈": "https://p3.itc.cn/q_70/images03/20220901/26f1a0107f59484e85d599941e78a1fa.jpeg",  # 假设图片文件名与大师名字对应
            "毕加索": "http://p1.img.cctvpic.com/cportal/img/2018/10/24/1540391373232_826_624x856.jpg",
            "梵高": "https://picx.zhimg.com/70/v2-3a81fde094b9c08452758beb28a44fc8_1440w.avis?source=172ae18b&biz_tag=Post",
            "高更": "https://th.bing.com/th/id/R.1e2eea12b33299b55908e79c4c49395c?rik=m2bMNmR7ga%2bwtA&riu=http%3a%2f%2fimg.mp.itc.cn%2fupload%2f20170709%2fb7fe376868ab44788bc394bf0160ce2d_th.jpg&ehk=izEhoMOjImadMc6XgURpXKwMZU%2brL96s%2fFEgNS%2fsXSQ%3d&risl=&pid=ImgRaw&r=0",
            "安格尔": "http://n1.itc.cn/img8/wb/recom/2016/04/13/146052113964591862.JPEG",
            "弗朗索瓦·米勒": "https://th.bing.com/th/id/OIP.cGvWL0l7KEcbdzWRWkFwPAHaJZ?rs=1&pid=ImgDetMain",
            "马奈": "https://www.xiwangchina.com/Uploads/Picture/2018/08/20/s5b7a1eb505858.jpg",
        }

        # 初始化对话状态
        if 'current_master' not in st.session_state:
            st.session_state['current_master'] = '莫奈'  # 默认与莫奈对话
        # 初始化对话状态
        if 'userinput' not in st.session_state:
            st.session_state['userinput'] = 0 # 默认与莫奈对话

        with st.sidebar:
            # 创建侧边栏
            st.sidebar.title("大师列表")
            # 创建侧边栏单选按钮以选择大师
            current_master = st.sidebar.radio("选择一位大师进行对话", masters)
            # 更新 session_state 中的当前大师
            st.session_state['current_master'] = current_master 
            # 显示当前选择的大师的图片
            st.image(master_images[current_master], width=280)

        
        st.subheader("当前对话" + st.session_state['current_master'])
        st.write("你好，我是"+st.session_state['current_master']+"，很高兴能和你对话")
        for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])

        # 原有的聊天逻辑
        if prompt := st.chat_input():
            st.chat_message("user").write(prompt)
            st.session_state['userinput'] = st.session_state['userinput'] + 1
            st.session_state.messages.append({"role": "user", "content": prompt})
            msg = talkwithboss(st.session_state['current_master'],prompt)
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg)

    elif selected2 == "绘梦成真":
        st.session_state.page = '绘梦成真'
        st.markdown("<h1 style='text-align: center; font-weight: bold;'>绘梦成真</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; font-weight: normal;'>向大师学习绘画</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; font-weight: normal;'>选择绘画流派或者大师分风格，使用AI作画</h1>", unsafe_allow_html=True)
        # 绘制一条横线
        st.markdown("---")
        # load data

        # 创建左右两列
        col1, col2 = st.columns(2)

        # 在左列中创建一个输入框
        with col1:
            user_input = st.text_input("请输入你的绘画创意：")
            # 添加尺寸选择框
            size_option = st.selectbox(
                "选择图片尺寸",
                ["1024x576", "1024x1024", "576x1024", "512x768", "768x512"]  # 注意这里最后两个选项是重复的，可能需要修正
            )
            #selected = pills("Label", ["莫奈的故事", "高更的故事", "梵高的绘画风格"], ["🍀", "🎈", "🌈"])

            # 一级选择的选项
            level_1_options = ['绘画风格', '画家风格', '自定义']
            #level_1_choice = st.radio("请选择一个选项：", level_1_options)
            level_1_choice = st.radio("请选择一个选项：", level_1_options, horizontal=True)
            # 根据一级选择，定义二级pills的内容
            if level_1_choice == '绘画风格':
                #pills_options = ['1-药丸A', '1-药丸B', '1-药丸C']
                pills_options = pills("Label", ["古典主义","洛可可艺术" ,"新古典主义","浪漫主义","写实主义", "印象派","后印象派","现代派"], ["🍀", "🎈", "🌈", "🏖", "⛺️", "🎸", "🎤", "🏵"])
            elif level_1_choice == '画家风格':
                #pills_options = ['2-药丸D', '2-药丸E', '2-药丸F']
                pills_options = pills("Label", ["莫奈的风格", "高更的风格", "梵高的风格","马奈的风格","毕加索的风格","弗朗索瓦·米勒的风格","安格尔的风格"], ["🍏", "🍎", "🍊", "🍌", "🍉", "🍇", "🍓"])
            else:  # '选项3'
            # pills_options = ['3-药丸G', '3-药丸H', '3-药丸I']
                #pills_options = pills("Label", ["莫奈的故事", "高更的故事", "梵高的绘画风格"], ["🍀", "🎈", "🌈"])
                pills_options = ""
            username_input = st.text_input("请输入你的签名：")
            # 显示二级pills的内容
            #pills_choice = st.radio("请选择一个药丸：", pills_options)
            st.session_state['prompt_image']  = promptajust(user_input,pills_options,username_input)
            #st.write(st.session_state['prompt_image'])
            with st.expander("自动生成的Prompt"):
            # 在这里，你可以根据用户的输入显示不同的内容
            # 例如，简单地回显用户输入的内容
                st.write(f"{st.session_state['prompt_image']}")
            generate_button = st.button("生成图片")

        # 在右列中显示出图界面
        with col2:
            # 创建一个空的占位符
            placeholder = st.empty()
            placeholder.markdown("""
            <div style="border: 2px solid  #808080; border-radius: 5px; height: 500px; display: flex; justify-content: center; align-items: center;">
                <h3>图像生成区</h3>
            </div>
            """, unsafe_allow_html=True)
            if generate_button:   # 如果用户已经输入了内容
                # 在占位符中显示“在生成中”的消息
                # with placeholder.container():
                #     st.write("图片生成中，请稍候...")
                #     # 调用生成图片的函数
                # 直接使用placeholder.markdown更新内容为“图片生成中，请稍候...”
                
                placeholder.markdown("""
                <div style="border: 2px solid #4CAF50; border-radius: 5px; height: 800px; display: flex; justify-content: center; align-items: center;">
                    <h3>图片生成中，请稍候...</h3>
                </div>
                """, unsafe_allow_html=True)
                image_url = create_iamge(st.session_state['prompt_image'],size_option)  # 生成图片
                # 图片生成完成后，使用placeholder.markdown显示生成的图片
                placeholder.image(image_url, caption="生成的图片")


        # 在上部分和画廊之间加一条分隔线
        st.markdown("---")
        def get_display_width(size_str):
            # 解析尺寸字符串
            width, height = map(int, size_str.split('x'))
            # 根据尺寸比例决定显示宽度
            if width > height:
                return 300  # 宽度大于高度，设置较大的显示宽度
            else:
                return 200  # 宽度小于或等于高度，设置较小的显示宽度
            
        # 展示画廊
        image_info_df = get_images_from_excel()
        if not image_info_df.empty:
            st.write("画廊")

            rows = (len(image_info_df) + 2) // 3  # 每行三幅图，计算需要多少行

            for i in range(rows):

                cols = st.columns([1, 0.1, 1, 0.1, 1])  # 创建三列，并在每两列图片之间添加一个较小的空列作为间隔
                for j in range(3):
                    img_index = i * 3 + j
                    if img_index < len(image_info_df):
                        row = image_info_df.iloc[img_index]
                        size_str = row["size"]
                        display_width = get_display_width(size_str)
                        caption = f"{row['user']} - {row['savetime']}"
                        # 由于添加了空列，实际图片列的索引需要调整
                        cols[j*2].image(row["imageURL"], width=display_width, caption=caption)

    else:
        st.session_state.page = '画师认证-获得证书'

        def get_image_base64(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode()
        if 'show_post' not in st.session_state:
            st.session_state['show_post'] = 0


        st.markdown("<h1 style='text-align: center; font-weight: bold;'>画师认证</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; font-weight: normal;'>回答对5道题，可以获得证书</h1>", unsafe_allow_html=True)
        # 绘制一条横线
        st.markdown("---")
        
        if 'answer' not in st.session_state:
            st.session_state['answer'] = ''
        # 检查 'voice_triggered' 是否在 session_state 中，且为 True
        if 'voice_triggered' not in st.session_state:
            st.session_state['voice_triggered'] = True
        # 在代码的开始部分初始化计数器
        if 'n' not in st.session_state:
            st.session_state['n'] = 0  # 初始化问题计数器
        if 'is_win' not in st.session_state:
            st.session_state['is_win'] = 0  # 初始化是否出局，0代表继续，1代表赢，2代表出局
        if 'start' not in st.session_state:
            st.session_state['start'] = 0
        if 'pic' not in st.session_state:
            st.session_state['pic'] = ""
        if 'audio_text' not in st.session_state:
            st.session_state['audio_text'] = ""
        if 'username' not in st.session_state:
            st.session_state['username'] = ""
        image_path = "testPost3.jpg"
        if st.session_state['start'] == 1:
            if st.session_state['is_win'] == 2:
                st.write("离成功已经很近了，建议再玩一次")
                if st.button('再来一次'):
                    st.session_state['is_win'] = 0
                    st.session_state['n'] = 0
                    st.rerun()
                else:
                    pass
            elif st.session_state['is_win'] == 1:
                st.write("你赢得了小画家的头衔")
                if st.session_state['show_post'] == 1:
                    st.image(image_path, caption="您的海报")

                else:
                    # 创建一个文本输入框，用户可以在其中输入用户名
                    username_input = st.text_input('请输入用户名:', value=st.session_state['username'])

                    # 更新 session_state 中的 'username'
                    st.session_state['username'] = username_input

                    # 显示当前 session_state 中的 'username' 值
                    st.write(f"用户名: {st.session_state['username']}")
                    if st.button('生成海报'):
                        

                        user=st.session_state['username']
                        backImg = "artist.jpg"
                        font = "msyhl.ttc"
                        pMaker = postMaker(backImg=backImg, font= font)
                        userIcon = 'testIcon.jpg'
                        qrImg = '334.png'
                        pMaker.create(
                            userIcon=userIcon,
                            userName=user,
                            qrImg=qrImg,
                            textColor={'R':0,'G':0,'B':0})
                    

                        time.sleep(5)
                        # 检查图片是否存在，最多等待10秒
                        max_wait_time = 10
                        wait_time = 0
                       
                        st.session_state['show_post'] = 1
                        print('cuo')
                        print(st.session_state['show_post'])
                        st.write('恭喜！您的海报已生成。')
                              
                        st.rerun()
                    else:
                        # 用户存在但is_win不为1
                        st.write('点击生成您的专属海报')




            else:
                # 使用 Streamlit 的 columns 方法创建三列
                
                
                if st.session_state['n'] < 5:
                    question_and_answer = get_question(st.session_state['n'])
                    question = question_and_answer["question"]
                    answer = question_and_answer["answer"]
                    pic =  question_and_answer["pic"]     
                    # # 获取图片的 Base64 编码字符串
                    # image_base64 = get_image_base64(pic)

                    # # col1, col2, col3 = st.columns([1,2,1])  # 调整比例以更好地居中
                    # # with col2:

                    # st.markdown(f"""
                    #     <div style="text-align: center;">
                    #         <img src="data:image/jpeg;base64,{image_base64}" alt="图片" style="width: 600px;">
                    #         <br />
                    #         <br />
                    # </div>
                    #         """, unsafe_allow_html=True)
                    #st.image(pic, width=400)
                    st.markdown(f"""
                <div style="text-align: center;">
                    <img src="{pic}" alt="图片" style="width: 600px;">
                    <br />
                    <br />
            </div>
                    """, unsafe_allow_html=True)

                    col1, col2= st.columns([1,1])  # 调整比例以更好地居中
                    with col1:
                        print(question)
                        st.markdown(f"""
                            <div >
                                <p>{question}</p>
                                
                            </div>
                        """, unsafe_allow_html=True)
                        if st.session_state['voice_triggered']:
                            audio_path = process_text(question)
                            # 使用 st.audio 来播放音频文件
                            st.audio(audio_path, format='audio/mp3')
                        #answer = "苹果的创办者是乔布斯" 
                        st.session_state['voice_triggered'] = False

                    # 在中间列添加 audiorecorder 组件
                    with col2:
                        st.markdown(f"""
                            <div style="text-align: center;">
                                <h4>语音答题请点击</h4>
                            </div>
                        """, unsafe_allow_html=True)
                        with st.container():
                        # 使用 columns 方法在容器内创建两列
                            col1, col2 = st.columns([1, 2])  # 第一列的宽度为1，第二列的宽度为2
                            with col2:
                                audio = audiorecorder("开始答题", "结束答题")
                                if len(audio) > 0:
                                    # To play audio in frontend:
                                    st.audio(audio.export().read())
                                    audio.export("output_audio.mp3", format="mp3")
                                    filename = "output_audio.mp3"
                                    new_filename = modify_mp3_file(filename)
                                    a2t = Audio2Text(config)
                                    # 对生成上锁，预防公有变量出现事务问题，但会降低程序并发性能。
                                    audio_text = a2t.gen_text(new_filename)
                                    #logger.info(audio_text)
                                    print(audio_text)
                                    st.session_state['audio_text'] = audio_text
                                    #voice_answer = audio_text
                                            
                                    st.write(st.session_state['audio_text'])
                                    st.session_state['flag_answer'] = audio_text
                                    
                                if st.button('提交答案'):
                                    print(st.session_state['answer'])
                                    print(answer)
                                    matches = is_right(st.session_state['answer'],answer)
                                    if matches == '1':
                                        st.write("答对了")
                                        process_text("哦，答对了，加油哦，下一题")
                                        st.session_state['voice_triggered'] = True
                                        st.session_state['n'] += 1  # 答对了，计数器加1
                                        if st.session_state['n'] == 4:
                                            st.session_state['is_win'] = 1
                                        
                                        st.session_state['audio_text'] = ''
                                        st.rerun()
                                    else:
                                        st.write("出局")
                                        process_text("哦，失败了，就差一点点了")
                                        st.session_state['is_win'] = 2
                                        st.rerun()

                    if input := st.chat_input("你也可以输入答案"):
                        st.session_state['answer'] = input
                        print(st.session_state['answer'])
                        print(answer)
                        #matches = difflib.get_close_matches(st.session_state['answer'], answer, n=1, cutoff=0.6)
                        matches = is_right(st.session_state['answer'],answer)
                        if matches == '1':
                            st.write("答对了")
                            process_text("哦，答对了，加油哦，下一题")
                            st.session_state['voice_triggered'] = True
                            st.session_state['n'] += 1  # 答对了，计数器加1
                            if st.session_state['n'] >= 5:
                                st.session_state['is_win'] = 1
                            st.rerun()
                        else:
                            st.write("出局")
                            process_text("哦，失败了，就差一点点了")
                            st.session_state['is_win'] = 2
                            st.rerun()

                    
        else:
            if 'clicked' not in st.session_state:
                st.session_state.clicked = False

            # 获取图片的 Base64 编码字符串
            image_base64 = get_image_base64("artist.jpg")

            # col1, col2, col3 = st.columns([1,2,1])  # 调整比例以更好地居中
            # with col2:

            st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{image_base64}" alt="图片" style="width: 600px;">
                    <br />
                    <br />
            </div>
                    """, unsafe_allow_html=True)
            def click_button():
                st.session_state.clicked = True
            with st.container():
                col1, col2, col3 = st.columns([3,1,3])  # 调整比例以更好地居中
                with col2:
                    st.button('开始', on_click=click_button)

            if not st.session_state.clicked:
                st.markdown("""
                        <div style="text-align: center;">
                            <p>我们将会持续给出10道题目，如果能全部答对，你将获得冠军头衔，准备好了吗？</p>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.session_state['start'] = 1
                st.rerun()

if __name__ == '__main__':
    main()