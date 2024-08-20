import streamlit as st
from LLM_xunfei2 import llm_write,Core_tex,draw

# 创建一个文本输入框，让用户输入一些文本
user_input = st.text_input("请输入一些内容：")

if 'question_1' not in st.session_state:
        st.session_state['question_1'] = ""

if 'answer_01' not in st.session_state:
        st.session_state['answer_01'] = True

# 使用expander创建一个可展开的区域
with st.expander("点击这里展开详细信息"):
    # 在这里，你可以根据用户的输入显示不同的内容
    # 例如，简单地回显用户输入的内容
    st.write(f"你输入的内容是：{user_input}")

    # 你也可以在这里添加更多的Streamlit组件来显示更多的信息
    # 例如，使用st.markdown显示格式化的文本
    st.markdown("""
    这里可以展示更多的详细信息，比如：
    - 用户指南
    - 详细的说明文档
    - 相关链接
    - 等等...
    """)


# 在expander下方增加一个下拉框，让用户从一批问题中选择
questions = ["问题1", "问题2", "问题3", "问题4"]
selected_question = st.selectbox("请选择你感兴趣的问题：", questions)

# 根据用户选择的问题显示相应的回答或信息
if selected_question == "问题1":
    st.write("这里是问题1的答案...")
elif selected_question == "问题2":
    st.write("这里是问题2的答案...")
elif selected_question == "问题3":
    st.write("这里是问题3的答案...")
elif selected_question == "问题4":
    st.write("这里是问题4的答案...")


example_prompts = [
    "You gain life and enemy loses life",
    "Vampires cards with flying ability",
    "Blue and green colored sorcery cards",
    "White card with protection from black",
    "The famous 'Black Lotus' card",
    "Wizard card with Vigiliance ability",
]

example_prompts_help = [
    "Look for a specific card effect",
    "Search for card type: 'Vampires', card color: 'black', and ability: 'flying'",
    "Color cards and card type",
    "Specifc card effect to another mana color",
    "Search for card names",
    "Search for card types with specific abilities",
]

button_cols = st.columns(3)
button_cols_2 = st.columns(3)

button_pressed = ""

if button_cols[0].button(example_prompts[0], help=example_prompts_help[0]):
    button_pressed = example_prompts[0]
elif button_cols[1].button(example_prompts[1], help=example_prompts_help[1]):
    button_pressed = example_prompts[1]
elif button_cols[2].button(example_prompts[2], help=example_prompts_help[2]):
    button_pressed = example_prompts[2]

elif button_cols_2[0].button(example_prompts[3], help=example_prompts_help[3]):
    button_pressed = example_prompts[3]
elif button_cols_2[1].button(example_prompts[4], help=example_prompts_help[4]):
    button_pressed = example_prompts[4]
elif button_cols_2[2].button(example_prompts[5], help=example_prompts_help[5]):
    button_pressed = example_prompts[5]

from streamlit_pills import pills
selected = pills("Label", ["莫奈的故事", "高更的故事", "梵高的绘画风格"], ["🍀", "🎈", "🌈"])
st.write(selected)
st.session_state['answer_01'] = True
st.session_state['question_1'] = selected
if st.session_state['answer_01']:
    st.write(llm_write(selected))
    st.session_state['answer_01'] = False

