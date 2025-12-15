import requests
import base64
import pygame
import os
from dwspark.config import Config
from datetime import datetime


from xunfei_config import xunfei_config as config
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
    return audio_path
    #play_audio(audio_path)
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
    text = '''
 小贝正坐在画室里，手中拿着调色板，眉头紧锁。琪琪博士走了进来，看到小贝困惑的样子，便问：“小贝，怎么了？有什么让你迷惑的吗？”

小贝抬起头说：“爸爸，我在学习法国绘画艺术时，遇到了一幅名叫《奥尔南的葬礼》的画作。它很大，而且画中的人物看起来都很悲伤。我想知道更多关于它的故事。”

琪琪博士坐下来，微笑着说：“那幅画是居斯塔夫·库尔贝的作品，他是19世纪的法国画家，以现实主义风格著称。现实主义就是艺术家们尝试真实地描绘世界，不过分美化或夸张。”

“库尔贝先生为什么要画一场葬礼呢？”小贝好奇地问。

琪琪博士解释说：“因为库尔贝先生想展示普通人的生活。在那个时代，很多画都是关于贵族和英雄的，但他认为农民和普通人民的生活同样重要。《奥尔南的葬礼》展示了他家乡的一次葬礼，那些参加葬礼的人表情严肃、衣着简朴，他们就像是我们身边真实的人。”

“那么，他是怎么画出这些细节的呢，爸爸？”小贝又问。

“好问题，小贝。库尔贝先生会去观察真实的场景，然后直接在画布上作画。他不会凭空想象，而是尽可能地让画作看起来像真的一样。你看，即使是葬礼这样沉重的主题，他也用细致的笔触表达了每个人不同的情感。”琪琪博士指着画册上的图片说。

“我明白了，他就像是用画笔拍照，把现实记录下来。”小贝点头说。

“没错，”琪琪博士笑着说，“而且库尔贝先生不仅是画家，他还是一个有自己想法的人。他相信艺术应该反映现实，而不只是美化它。所以，他的画作有时候会让人感到不舒服，因为它们太真实了。”

“爸爸，我觉得我开始懂了，艺术可以是多面的，它不仅可以是美丽的，还可以让我们思考。”小贝认真地说。

琪琪博士点点头：“对，小贝，艺术可以教会我们很多东西。库尔贝先生的画作就是一个例子，它让我们看到了另一个时代的人们的生活，也让我们思考什么是真正的艺术。”

小贝再次看向那幅《奥尔南的葬礼》，眼中充满了新的理解和尊重。他知道，每次他观察这幅画时，都能看到不同的故事，感受到不同的情感，这正是艺术的魔力。

    '''
    #process_text(text)
    pass

