import streamlit as st
from testimage import create_iamge
from data_change import get_images_from_excel
from LLM_xunfei2 import promptajust
from streamlit_pills import pills

if 'prompt_image' not in st.session_state:
        st.session_state['prompt_image'] = ""

st.set_page_config(page_title='向大师学习绘画', page_icon=' ', layout='wide')
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