import pandas as pd
from datetime import datetime

def query_drawing_data():
    # 读取Excel文件
    df = pd.read_excel('France_works.xlsx', engine='openpyxl')

    # 打印DataFrame的内容来查看数据
    #print(df)

    # 如果你想访问特定列的数据，可以像这样做：
    #print(df['drawing_name'][0])  # 打印所有的drawing_name列的值

    # 提取drawing_name列的值
    #drawing_names = df['drawing_name']

    # 打印drawing_name列的所有值
    #print(drawing_names)

    # 创建一个新的空列表
    #new_list = []

    # 使用循环将drawing_names中的每个值添加到新列表中
    # for name in drawing_names:
    #     new_list.append(name)

    # 打印新列表以验证结果
    #print(new_list)
    return df



def save_image_info_to_excel(image_url,user,size):
    # 尝试读取现有的Excel文件，如果不存在则创建一个新的DataFrame
    try:
        df = pd.read_excel('images_info.xlsx', engine='openpyxl')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['imageURL', 'user', 'savetime','size'])
    
    # 创建一个包含新数据的DataFrame
    new_data_df = pd.DataFrame([{'imageURL': image_url, 'user': user, 'savetime': datetime.now(),'size': size}])
    
    # 使用concat而不是append合并DataFrame
    df = pd.concat([df, new_data_df], ignore_index=True)
    
    # 保存DataFrame到Excel文件
    df.to_excel('images_info.xlsx', index=False, engine='openpyxl')


def get_images_from_excel():
    # 读取Excel文件
    df = pd.read_excel('images_info.xlsx', engine='openpyxl')
    return df



