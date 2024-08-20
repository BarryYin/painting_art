# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline
from streamlit_option_menu import option_menu
import pages as pgs
from vocie3 import process_text
from LLM_xunfei2 import llm_write,Core_tex,draw,Org_tex,bosssay
from data_change import query_drawing_data
import pandas as pd
from vocie3 import process_text
from test_web_api import talkwithboss
from testimage import create_iamge
from data_change import get_images_from_excel
from LLM_xunfei2 import promptajust
from streamlit_pills import pills
from audiorecorder import audiorecorder
from dwspark.models import Audio2Text
from modify_mp3 import modify_mp3_file
from dwspark.config import Config
# 加载系统环境变量：SPARKAI_APP_ID、SPARKAI_API_KEY、SPARKAI_API_SECRET
config = Config('3a115b20', '9d1b7a738c3e63a79656df4222d12cef','ZGMyMzA3MGFlM2MzM2UxZWE1YTJhYjgw')

st.set_page_config(page_title="法国绘画展-瓦力AI解读", layout="wide")

def get_question(n):
    # 假设我们有一个包含问题及其答案的列表
    questions_with_answers = [
        {"question": "法国有一位艺术家，他的作品《草地上的午餐》挑战了当时的社会规范，以其大胆的构图和对光影的处理而闻名，这位艺术家是谁？ 提示：这位艺术家是印象派的先驱之一，他的作品常常描绘户外场景。", "answer": "马奈"},
        {"question": "哪位法国画家以他的《睡莲》系列而闻名，这些作品描绘了自家花园中的睡莲池塘?", "answer": "莫奈"},
        {"question": "法国有一位艺术家，他的作品《阿维尼翁的少女》被认为是立体主义的开端，这位艺术家是谁？提示：这位艺术家的画作打破了传统的透视规则，用几何形状重新组合了画面。", "answer": "毕加索"},
        {"question": "法国有一个著名的艺术时期，艺术家们创作了许多描绘日常生活场景的画作，这个时期被称为什么?提示：这个时期的艺术家们喜欢描绘普通人的日常生活。", "answer": "现实主义"},
        {"question": "法国有一位后印象派画家，以其使用鲜明色彩和厚重笔触而知名，他的作品《星夜》是世界著名的艺术品，这位画家是谁？", "answer": "英国"},
        {"question": "18世纪上半叶，法国居统治地位的是宫廷喜好的冗繁浮华风格，这种风格描绘全裸或半裸的妇女和精美华丽的装饰。追求轻盈纤巧，精致细腻的风格，趣味甜俗，充满胭脂粉气。这种艺术的名字？", "answer": "洛可可"},
       
    ]
    # 根据 `n` 的值返回相应的问题和答案
    # 注意: 这里假设 `n` 的值不会超过问题列表的长度
    return questions_with_answers[n]


def main():

    selected2 = option_menu(None, ["法国绘画作品", "绘画故事", "绘画解读", '绘画风格', '获得证书'], 
    icons=['house', 'cloud-upload', "list-task", 'gear', 'gear'], 
    menu_icon="cast",  orientation="horizontal") #default_index=0,
    #selected2
    
    if selected2 == "法国绘画作品":
        st.session_state.page = '法国绘画作品'
        # 添加居中且加粗的标题
        st.markdown("<h1 style='text-align: center; font-weight: bold;'>法国绘画300年</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; font-weight: normal;'>与AI一起学习法国绘画历史</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; font-weight: normal;'>欣赏名画、趣讲画作故事、与大师对话、模拟名画<br/></h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; font-weight: bold;'></h1>", unsafe_allow_html=True)
        # load data
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
    
    elif selected2 == "绘画故事":
        st.session_state.page = '绘画故事'
        

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
    
    elif selected2 == "绘画解读":
        st.session_state.page = '绘画解读'
        if "messages" not in st.session_state:
                st.session_state["messages"] = []
        # 假设有一个函数用于显示大师的界面
        def show_master_page(master_name):
            st.header(f"{master_name}的界面")
            # 这里可以添加更多关于大师的信息和交互

        
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

    elif selected2 == "绘画风格":
        st.session_state.page = '绘画风格'
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
            generate_button = st.button("生成图片")
            st.session_state['prompt_image']  = promptajust(user_input,pills_options,username_input)
            st.write(st.session_state['prompt_image'])

        # 在右列中显示出图界面
        with col2:
            # 创建一个空的占位符
            placeholder = st.empty()
            placeholder.markdown("""
            <div style="border: 2px solid #4CAF50; border-radius: 5px; height: 200px; display: flex; justify-content: center; align-items: center;">
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
                <div style="border: 2px solid #4CAF50; border-radius: 5px; height: 200px; display: flex; justify-content: center; align-items: center;">
                    <h3>图片生成中，请稍候...</h3>
                </div>
                """, unsafe_allow_html=True)
                image_url = create_iamge(st.session_state['prompt_image'],size_option)  # 生成图片
                # 图片生成完成后，使用placeholder.markdown显示生成的图片
                placeholder.image(image_url, caption="生成的图片")
                    # placeholder.empty()  # 清空占位符中的内容
                    # # 显示生成的图片
                    # st.image(image_url, caption="生成的图片")  # 显示图片


        # 展示画廊
        # image_info_df = get_images_from_excel()
        # if not image_info_df.empty:
        #     st.write("画廊")
        #     for index, row in image_info_df.iterrows():
        #         st.image(row['imageURL'], caption=f"{row['user']} - {row['savetime']}")
                

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
            # 使用Streamlit展示图片
            # for index, row in image_info_df.iterrows():  # 正确迭代DataFrame的每一行
            #     size_str = row["size"]  # 使用行数据
            #     display_width = get_display_width(size_str)
            #     #st.image(row["imageURL"], width=display_width)
            #     # 在图片下方展示用户和保存时间信息
            #     caption = f"{row['user']} - {row['savetime']}"
            #     st.image(row["imageURL"], width=display_width, caption=caption)
            # 计算需要多少行来展示所有图片
            rows = (len(image_info_df) + 2) // 3  # 每行三幅图，计算需要多少行

            for i in range(rows):
                # cols = st.columns(3)  # 创建三列
                # for j in range(3):
                #     # 计算当前行的图片索引
                #     img_index = i * 3 + j
                #     if img_index < len(image_info_df):
                #         row = image_info_df.iloc[img_index]
                #         size_str = row["size"]
                #         display_width = get_display_width(size_str)  # 获取每张图片的显示宽度
                #         caption = f"{row['user']} - {row['savetime']}"  # 在图片下方展示用户和保存时间信息
                #         # 在对应的列中显示图片，并设置宽度
                #         cols[j].image(row["imageURL"], width=display_width, caption=caption)
                #         # 为每个图片组件生成一个唯一的key
                #         # unique_key = f"image_{img_index}"
                #         # # 在对应的列中显示图片，并设置宽度，确保每个图片都有一个唯一的key
                #         # cols[j].image(row["imageURL"], width=display_width, caption=caption, key=unique_key)
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
        st.session_state.page = '获得证书'

        st.markdown("""
            <div style="text-align: center;">
                <h4>一站到底</h4>
            </div>
                    """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1,2,1])  # 调整比例以更好地居中

        # 在中间列显示图像
        with col2:
            #st.image("path/to/your/image.png")  # 替换为您的图像路径
            #st.image("standing.png", caption="",width=350)
            st.write("法国考试")

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
                st.write("你赢的了一站到底英雄的头衔")
            else:
                if st.session_state['n'] < 5:
                    question_and_answer = get_question(st.session_state['n'])
                    question = question_and_answer["question"]
                    answer = question_and_answer["answer"]      
                    print(question)
                    st.markdown(f"""
                        <div style="text-align: center;">
                            <p>{question}</p>
                            <h4>语音答题请点击</h4>
                        </div>
                    """, unsafe_allow_html=True)

                    if st.session_state['voice_triggered']:
                        process_text(question)
                    #answer = "苹果的创办者是乔布斯" 
                    st.session_state['voice_triggered'] = False
                

                    # 使用 Streamlit 的 columns 方法创建三列
                    col1, col2, col3 = st.columns([2,1,2])  # 调整比例以更好地居中

                    # 在中间列添加 audiorecorder 组件
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
                            voice_answer = audio_text
                                    
                            st.write(voice_answer)
                            st.session_state['flag_answer'] = voice_answer
                            
                        if st.button('提交答案'):
                            print(st.session_state['answer'])
                            print(answer)
                            matches = is_right(st.session_state['answer'],answer)
                            if matches == '1':
                                st.write("答对了")
                                process_text("哦，答对了，加油哦，下一题")
                                st.session_state['voice_triggered'] = True
                                st.session_state['n'] += 1  # 答对了，计数器加1
                                if st.session_state['n'] >= 10:
                                    st.session_state['is_win'] = 1
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
                            if st.session_state['n'] >= 10:
                                st.session_state['is_win'] = 1
                            st.rerun()
                        else:
                            st.write("出局")
                            process_text("哦，失败了，就差一点点了")
                            st.session_state['is_win'] = 2
                            st.rerun()

                    
            
        else:
            #col1, col2, col3 = st.columns([1,2,1])  # 调整比例以更好地居中

            # 在中间列显示图像
            #with col2:
            if st.button("开始吧"):
                st.session_state['start'] = 1
                st.rerun()
            else:
                st.markdown("""
                    <div style="text-align: center;">
                        <p>我们将会持续给出10道题目，如果能全部答对，你将获得冠军头衔，准备好了吗？</p>
                    </div>
                """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()