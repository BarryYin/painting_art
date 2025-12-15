import streamlit as st
from audiorecorder import audiorecorder
from vocie3 import process_text
from LLM_unified import is_right
from dwspark.models import Audio2Text
from modify_mp3 import modify_mp3_file
from dwspark.config import Config

 # 加载系统环境变量：SPARKAI_APP_ID、SPARKAI_API_KEY、SPARKAI_API_SECRET
from xunfei_config import xunfei_config as config

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