import requests
import base64
import pygame
import os
from dwspark.config import Config
from datetime import datetime


config = Config('3a115b20', '9d1b7a738c3e63a79656df4222d12cef','ZGMyMzA3MGFlM2MzM2UxZWE1YTJhYjgw')
# SDK引入模型
from dwspark.models import ChatModel, Text2Img, ImageUnderstanding, Text2Audio, Audio2Text, EmebddingModel

def process_text(text):
    """
    处理文本，如果文本超过长度限制，则分段处理。
    """
    #使用当前时间戳生成文件名
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    audio_path = f'output_{timestamp}.mp3'
    #audio_path = 'outout2.mp3'

    # 检查文件是否存在
    if os.path.exists(audio_path):
        # 如果文件存在，删除文件
        os.remove(audio_path)

    t2a = Text2Audio(config)
    # # 对生成上锁，预防公有变量出现事务问题，但会降低程序并发性能。
    t2a.gen_audio(text, audio_path)
    play_audio(audio_path)
    #audio_html = f'<audio src="{audio_path}" autoplay="autoplay"></audio>'
    # audio_html = f'''<audio controls autoplay>
    #                     <source src="{audio_path}" type="audio/mpeg">
                        
    #                     您的浏览器不支持 audio 标签。
    #                     </audio>'''

    # return audio_html

def play_audio(file_name):
    # 初始化 pygame 混音器
    pygame.mixer.init()
    # 加载音频文件
    pygame.mixer.music.load(file_name)
    # 播放音频
    pygame.mixer.music.play()
    # 等待音频播放完成
    # while pygame.mixer.music.get_busy():
    #     pygame.time.Clock().tick(5)


if __name__ == '__main__':
    #create_voise('他是谁呀，你认识吗')
    # text = "聪明的一休哥也斗不过阿凡提的毛驴子"
    # #text = "他是谁呀，汤面"
    # process_text(text)
    pass
