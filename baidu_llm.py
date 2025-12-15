#!/usr/bin/env python3
"""
百度ERNIE模型封装类
用于替换讯飞模型的文生文功能
"""
import asyncio
from openai import AsyncOpenAI
import json
import re

class BaiduLLM:
    def __init__(self, api_key=None, base_url=None, model="ernie-4.5-turbo-32k"):
        """
        初始化百度ERNIE模型
        
        Args:
            api_key: 百度API密钥
            base_url: 百度API基础URL
            model: 使用的模型名称
        """
        from config import Config
        self.api_key = api_key or Config.BAIDU_API_KEY
        self.base_url = base_url or Config.BAIDU_BASE_URL
        self.model = model
        self.client = AsyncOpenAI(api_key=self.api_key, base_url=self.base_url)
    
    async def generate_async(self, messages, temperature=0.7):
        """异步生成文本"""
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"百度模型调用失败: {e}")
            return "抱歉，模型调用失败，请稍后重试。"
    
    def generate(self, messages, temperature=0.7):
        """同步生成文本（兼容原有接口）"""
        return asyncio.run(self.generate_async(messages, temperature))
    
    def chat(self, content, temperature=0.7):
        """简化的对话接口"""
        messages = [{"role": "user", "content": content}]
        return self.generate(messages, temperature)

# 全局百度模型实例
baidu_model = BaiduLLM()

def promptajust(text, style, sign):
    """生成Flux AI绘画prompt"""
    userinput = text + "," + "风格是：" + style + "," + "签名是：" + sign
    question = f'''
flux是一个AI艺术生成工具，它的prompt规则通常遵循一些基本的指导原则，以确保生成的艺术作品符合用户的期望。以下是一些编写Flux prompt时应该考虑的要点：

主题描述：明确地描述您想要AI创作的主题，比如"向日葵"。

细节特征：提供关于作品细节的具体描述，如花瓣的形态、颜色的深浅、光线的运用等。

风格指定：指出您希望作品模仿的艺术风格或艺术家，例如"梵高风格"。

媒介和技法：说明作品的创作媒介，如"油画"，以及使用的技法，比如"厚涂法"。

构图方式：描述作品的构图，比如"近距离特写"或"全身像"。

情感氛围：传达您希望作品表达的情感，如"充满希望和活力"。

技术参数：如果适用，可以指定渲染技术，如"Flux AI渲染"。

分辨率和质量：对于数字作品，可以指定分辨率，但对于油画等传统媒介，可以强调作品的质量，如"适合艺术打印的高质量"。

连续性：如果prompt需要继续扩展，保持描述的连贯性和一致性。

简洁性：尽管详细很重要，但也要避免过度复杂化，使prompt易于理解和执行。

举例：

Paint a Van Gogh-inspired 'Sunflowers' oil piece: a close-up composition of vibrant yellow sunflowers in a rustic vase, with deep green leaves. Emulate Van Gogh's thick, expressive brushstrokes and rich color palette. Convey the hopeful vitality of the original. Use Flux AI for a high-resolution, fine art-quality rendering.

一个好的prompt在500字以内，包含了艺术作品的关键元素和风格要求，同时指定了使用Flux AI进行高分辨率渲染。且是英文的。

请将下面的内容描述成flux的prompt，符合要求，且是英文。

{userinput}
'''
    
    response = baidu_model.chat(question)
    print(response)
    return response

def bosssay(text):
    """莫奈角色对话"""
    question = f'''
你是莫奈，你是印象派大师，现在你来回答用户的问题：{text}
'''
    response = baidu_model.chat(question)
    print(response)
    return response

def Core_tex(text):
    """提炼插画内容"""
    question = f'''
你是插画大师，你需要能从文本中提炼主题关键词并进行插画的内容描述，下面这段文字是小贝和琪琪博士的对话，他们在谈论一个问题，请你依据他们讨论的问题核心提炼出插画内容。不超过20个字，以用于画画：{text}
'''
    response = baidu_model.chat(question)
    print(response)
    return response

def RAG_LLM(text):
    """儿童百科问答助手"""
    question = f'''
你是作为儿童的虚拟朋友和知识导师，少儿百科问答助手拥有丰富的知识储备和耐心的性格，随时准备回答小朋友们提出的任何问题。它用简单易懂的语言，带领孩子们走进科学的殿堂，激发他们的好奇心与求知欲。该助手的主要任务是准确理解并回答孩子们提出的问题，同时提供相关领域的额外知识点，以丰富孩子的认知世界。在回答问题的过程中，注重引导孩子自主思考，培养其解决问题的能力。请用3-8岁小朋友能理解的语言，进行百科问答的解释，不要做过多的分段和书面用词：{text}
'''
    response = baidu_model.chat(question)
    print(response)
    return response

def Org_tex(text):
    """绘画作品介绍"""
    question = f'''
用户输入的内容是：{text}。你是一个绘画博士，你需要用户的输入，输出相关内容。介绍的内容，可以包括作品介绍、作家介绍，包括相关的流派、作品、生平，不超过2000个字
'''
    response = baidu_model.chat(question)
    print(response)
    return response

def llm_write(text):
    """创作儿童绘画故事"""
    question = f'''
你是一个绘画博士，你需要向中小学生讲述法国绘画风格、艺术和画师的故事，请将下面的内容写成一段故事，以主人公小贝和它的爸爸琪琪博士的对话为主要情景，小贝正在学习法国绘画艺术，用8-12岁小朋友的语言进行描述，将绘画作品的背景、作家的风格、作家表达的意图。不超过1000个字，在解释清楚的同时，还要注意启发孩童思考为主：{text}
'''
    response = baidu_model.chat(question)
    print(response)
    return response

def is_right(inputtext, answer):
    """判断用户输入是否匹配答案"""
    question = f'''
请匹配用户输入的内容和答案之间是否匹配
用户输入： {inputtext} 
答案： {answer}
请给出答案，如果匹配或者接近，请回复为1，如果不匹配，请回复为0.
注意，只要用户输入出现了和答案相近的意思，或者同音的字，都可以视为正确。比如答案是真菌，用户输入了真君，虽然字面意思不一致，但考虑到用户音频翻译有误差，用户可能说的就是真菌，但翻译成了真君，因此也判断为正确。
或者客户说了2个及以上的选项，只要有1个选项满足要求，也可以让其通过。
输出格式如下：
```json
[
    {{
        "answer" : "1",
        "reason": "判断的理由"
    }}
]
```
'''
    
    try:
        response = baidu_model.chat(question)
        print(response)
        
        # 提取JSON部分
        json_match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            # 如果没有找到```json```标记，尝试直接解析
            json_str = response.strip()
        
        data = json.loads(json_str)
        answer_result = data[0]["answer"]
        reason = data[0]["reason"]
        
        print(f"判断结果: {answer_result}")
        print(f"理由: {reason}")
        return answer_result
        
    except Exception as e:
        print(f"解析响应失败: {e}")
        print(f"原始响应: {response}")
        return "0"  # 默认返回不匹配

if __name__ == "__main__":
    # 测试函数
    print("测试百度模型...")
    result = baidu_model.chat("你好，请简单介绍一下自己")
    print(f"测试结果: {result}")