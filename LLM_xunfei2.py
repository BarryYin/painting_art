from dwspark.config import Config
import json
import requests
import re
 
 # 加载系统环境变量：SPARKAI_APP_ID、SPARKAI_API_KEY、SPARKAI_API_SECRET
from xunfei_config import xunfei_config as config

# SDK引入模型
from dwspark.models import ChatModel, Text2Img, ImageUnderstanding, Text2Audio, Audio2Text, EmebddingModel
# 讯飞消息对象
from sparkai.core.messages import ChatMessage
# 日志
from loguru import logger

def promptajust(text,style,sign):  #这里用智能体会好一些，加油
        userinput = text + "," + "风格是："+style+ "," + "签名是：" + sign
        model = ChatModel(config, stream=False)
        question=f'''
                    flux是一个AI艺术生成工具，它的prompt规则通常遵循一些基本的指导原则，以确保生成的艺术作品符合用户的期望。以下是一些编写Flux prompt时应该考虑的要点：

主题描述：明确地描述您想要AI创作的主题，比如“向日葵”。

细节特征：提供关于作品细节的具体描述，如花瓣的形态、颜色的深浅、光线的运用等。

风格指定：指出您希望作品模仿的艺术风格或艺术家，例如“梵高风格”。

媒介和技法：说明作品的创作媒介，如“油画”，以及使用的技法，比如“厚涂法”。

构图方式：描述作品的构图，比如“近距离特写”或“全身像”。

情感氛围：传达您希望作品表达的情感，如“充满希望和活力”。

技术参数：如果适用，可以指定渲染技术，如“Flux AI渲染”。

分辨率和质量：对于数字作品，可以指定分辨率，但对于油画等传统媒介，可以强调作品的质量，如“适合艺术打印的高质量”。

连续性：如果prompt需要继续扩展，保持描述的连贯性和一致性。

简洁性：尽管详细很重要，但也要避免过度复杂化，使prompt易于理解和执行。

举例：

Paint a Van Gogh-inspired 'Sunflowers' oil piece: a close-up composition of vibrant yellow sunflowers in a rustic vase, with deep green leaves. Emulate Van Gogh's thick, expressive brushstrokes and rich color palette. Convey the hopeful vitality of the original. Use Flux AI for a high-resolution, fine art-quality rendering.

一个好的prompt在500字以内，包含了艺术作品的关键元素和风格要求，同时指定了使用Flux AI进行高分辨率渲染。且是英文的。

请将下面的内容描述成flux的prompt，符合要求，且是英文。

"+ {userinput}
                    '''
        response = model.generate([ChatMessage(role="user", content=question)])
        print(response)
        return response 

def bosssay(text):  #这里用智能体会好一些，加油
        model = ChatModel(config, stream=False)
        question=f'''
                    你是莫奈，你是印象派大师，现在你来回答用户的问题"+ {text}
                    '''
        response = model.generate([ChatMessage(role="user", content=question)])
        print(response)
        return response 

def Core_tex(text):
        model = ChatModel(config, stream=False)
        question=f'''
                    你是插画大师，你需要能从文本中提炼主题关键词并进行插画的内容描述，下面这段文字是小贝和琪琪博士的对话，他们在谈论一个问题，请你依据他们讨论的问题核心提炼出插画内容。不超过20个字，以用于画画"+ {text}
                    '''
        response = model.generate([ChatMessage(role="user", content=question)])
        print(response)
        return response 
def draw(text):
        prompt = text
        file_path = './demo9.jpg'
        t2i = Text2Img(config)
        t2i.gen_image(prompt, file_path)
        return file_path

def RAG_LLM(text):
        model = ChatModel(config, stream=False)
        question=f'''
                    你是作为儿童的虚拟朋友和知识导师，少儿百科问答助手拥有丰富的知识储备和耐心的性格，随时准备回答小朋友们提出的任何问题。它用简单易懂的语言，带领孩子们走进科学的殿堂，激发他们的好奇心与求知欲。该助手的主要任务是准确理解并回答孩子们提出的问题，同时提供相关领域的额外知识点，以丰富孩子的认知世界。在回答问题的过程中，注重引导孩子自主思考，培养其解决问题的能力。请用3-8岁小朋友能理解的语言，进行百科问答的解释，不要做过多的分段和书面用词"+ {text}
                    '''
        response = model.generate([ChatMessage(role="user", content=question)])
        print(response)
        return response 


def Org_tex(text):
        model = ChatModel(config, stream=False)
        question=f'''
                    用户输入的内容是"+ {text} + "你是一个绘画博士，你需要用户的输入，输出相关内容。介绍的内容，可以包括作品介绍、作家介绍，包括相关的流派、作品、生平，不超过2000个字"
                    '''
        response = model.generate([ChatMessage(role="user", content=question)])
        print(response)
        return response 

def llm_write(text):
        model = ChatModel(config, stream=False)
        question=f'''
                    你是一个绘画博士，你需要向中小学生讲述法国绘画风格、艺术和画师的故事，请将下面的内容写成一段故事，以主人公小贝和它的爸爸琪琪博士的对话为主要情景，小贝正在学习法国绘画艺术，用8-12岁小朋友的语言进行描述，将绘画作品的背景、作家的风格、作家表达的意图。不超过1000个字，在解释清楚的同时，还要注意启发孩童思考为主"+ {text}
                    '''
        response = model.generate([ChatMessage(role="user", content=question)])
        print(response)
        return response

def is_right(inputtext,answer):
            
            model = ChatModel(config, stream=False)
            question=f'''
                           请匹配用户输入的内容和答案之间是否匹配\n
                           用户输入： {inputtext} \n
                           答案： {answer}
                           请给出答案，如果匹配或者接近，请回复为1，如果不匹配，请回复为0.
                           注意，只要用户输入出现了和答案相近的意思，或者同音的字，都可以视为正确。比如答案是真菌，用户输入了真君，虽然字面意思不一致，但考虑到用户音频翻译有误差，用户可能说的就是真菌，但翻译成了真君，因此也判断为正确。
                           或者客户说了2个及以上的选项，只要有1个选项满足要求，也可以让其通过。
                           输出格式如下：
                           ‘’‘json
                           [
                                {{
                                    "answer" : "1",
                                    "reason'": "判断的理由"
                                }}
                            ]
                           ’‘’
                           '''
            
            #response = model.generate([ChatMessage(role="user", content=question)])
            response = model.generate([ChatMessage(role="user", content=question)])
            print(response)
            # 移除非JSON的部分
            json_str = response.strip("’‘’json\n").strip("’‘’\n")
            json_str = json_str.strip("```json\n").strip("```\n")
            print(json_str)

            data = json.loads(json_str)
            print(data)
            # 提取"answer"的值
            answer = data[0]["answer"]
            reason = data[0]["reason"]

            print(answer)  # 输出: 1
            print(reason)
            return answer

#promptajust("小桥，洛可可艺术风格，签名为John")
# is_right("the south people","南方的人")

#Org_tex('莫奈介绍')
# llm_write('''
#           奈的《睡莲》系列，共181幅画作，是克劳德·莫奈在1895年至1926年间创作的。莫奈运用细腻的笔触和丰富的色彩，捕捉水面上莲叶的光影变化，呈现出一种和谐宁静的氛围。这些作品不仅展示了莫奈对光线和色彩的敏锐把握，也体现了印象派对自然之美的独特诠释。

# 克劳德·莫奈，法国画家，印象派代表人物和创始人之一，其艺术生涯中，他深受自然界的启发。《睡莲》并非莫奈晚年的突发奇想，而是他长期观察自然、描绘自然所积累的深厚功力的集中爆发。在莫奈的笔下，水面波光粼粼，莲叶与莲花布置得恰到好处，形成了一种和谐宁静的氛围。画面中莲花的色彩丰富多样，彰显了莫奈对光线和色彩的敏锐把握。

# 《睡莲》这个标题，是1909年在迪朗-吕埃尔画廊展出作品时，莫奈自选的标题。这48幅画作于1903年完成，标志着莫奈对这一主题长达十年的深度探索。莫奈以令人叫绝的技法，在垂直的平面上描绘出波光粼粼的水面向远处延伸的视觉效果。这种独特的视角和表现手法，使得《睡莲》成为印象派绘画最具代表性的作品之一。

# 莫奈的《睡莲》系列，不仅是他个人艺术风格的集大成之作，也是整个印象派运动的里程碑。这一系列作品以其独特的视角、细腻的笔触和丰富的色彩，展现了莫奈对自然界的深刻理解和热爱。同时，它们也体现了印象派对光与色彩的独特处理方式，对后世艺术产生了深远影响。

# 莫奈的《睡莲》系列是他在艺术生涯晚期的代表作，也是印象派绘画的杰出典范。这一系列作品以其独特的视角、细腻的笔触和丰富的色彩，展现了莫奈对自然界的深刻理解和热爱。同时，它们也体现了印象派对光与色彩的独特处理方式，对后世艺术产生了深远影响。
#           ''')
# llm_write('梵高的故事')
# llm_write('高更的故事')
# llm_write('莫奈的故事')
#RAG_LLM('月亮为什么会陪着地球')

# Core_tex('''小贝和爸爸琪琪博士晚上散步时，抬头看见闪烁的北斗七星。小贝好奇地问：“爸爸，那些星星为什么叫北斗七星呢？”

# 琪琪博士微笑着说：“你看，它们像不像一个勺子？”小贝点点头，觉得真像。琪琪博士接着说：“但你知道吗？这些星星虽然现在是这样的形状，可是在很久很久以前或者很久以后，它们的样子会改变哦。”

# “真的吗？它们为什么会变呢？”小贝惊讶地问。

# 琪琪博士解释道：“因为每颗星星都在天空中慢慢移动，就像我们走路一样。虽然走得很慢，但时间一长，位置就会有所不同。”

# “那它们会变成什么样子呢？”小贝好奇地追问。''')

# Core_tex(''' 在温暖的夏夜，小贝躺在后院的草地上，望着繁星点点的天空。他好奇地问道：“爸爸，星星是从哪里来的呢？”

# 琪琪博士微笑着说：“好问题，小贝！很多年前，有一个聪明的人叫哈勃先生，他用一个大望远镜看到了很远的地方。”

# “比月亮还远吗？”小贝惊讶地问。

# “对，比月亮还要远得多，”琪琪博士回答，“他发现了很多像我们银河系一样的星星家族，这些家族叫做星系。”

# “哇，那有多少个星系呀？”小贝好奇地继续问。

# “数不清哦，就像沙滩上的沙粒一样多。”琪琪博士解释道，“而且，哈勃先生还发现了一个很重要的东西，就是星系们在慢慢地移动，离我们越来越远。”

# “它们为什么要离开我们？”小贝有些困惑。

# 琪琪博士温柔地说：“不是离开我们，小贝，是宇宙在长大，就像你每天都在长高一样。这个发现帮助我们知道了宇宙是怎么变化的。”

# 小贝想象着宇宙在不断变大，小声说：“那我们的宇宙真的好大啊！”

# “是的，它真的很大，充满了奇迹。”琪琪博士点头，“而我们通过学习和探索，就能了解更多关于它的奇妙故事。”

# 小贝紧紧握着爸爸的手，一起仰望星空，心里充满了对未知世界的憧憬和尊重。''')