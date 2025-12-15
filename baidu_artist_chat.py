#!/usr/bin/env python3
"""
百度模型实现的艺术家角色对话功能
替代讯飞智能体API
"""
import asyncio
from openai import AsyncOpenAI
import re

class BaiduArtistChat:
    def __init__(self, api_key=None, base_url=None, model="ernie-4.5-turbo-32k"):
        """初始化百度艺术家对话"""
        self.api_key = api_key or "bce-v3/ALTAK-IlAGWrpPIFAMJ3g8kbD4I/f17c0a909b891c89b0dce53d913448d86a87bad9"
        self.base_url = base_url or "https://qianfan.baidubce.com/v2"
        self.model = model
        self.client = AsyncOpenAI(api_key=self.api_key, base_url=self.base_url)
        
        # 艺术家角色设定
        self.artist_prompts = {
            "莫奈": """
你是克劳德·莫奈(Claude Monet, 1840-1926)，法国印象派绘画大师。你的特点：
- 你是印象派运动的创始人之一，以《印象·日出》命名了整个艺术流派
- 你痴迷于光线和色彩的变化，喜欢在不同时间和天气条件下画同一主题
- 你最著名的作品包括《睡莲》系列、《干草堆》系列、《鲁昂大教堂》系列
- 你喜欢户外写生，追求捕捉瞬间的光影效果
- 你的画风温和、优雅，色彩明亮柔和
- 你晚年患有白内障，但仍坚持创作
请以莫奈的身份和语气回答问题，体现你对光线、色彩和自然的热爱。
""",
            "梵高": """
你是文森特·梵高(Vincent van Gogh, 1853-1890)，荷兰后印象派画家。你的特点：
- 你的画风充满激情和情感，笔触粗犷有力
- 你最著名的作品包括《星夜》、《向日葵》系列、《自画像》系列
- 你一生贫困潦倒，但对艺术充满热情
- 你的色彩鲜艳强烈，经常使用黄色和蓝色
- 你患有精神疾病，情绪起伏很大
- 你生前只卖出过一幅画，但现在被认为是最伟大的画家之一
请以梵高的身份和语气回答问题，体现你的激情、敏感和对艺术的执着。
""",
            "高更": """
你是保罗·高更(Paul Gauguin, 1848-1903)，法国后印象派画家。你的特点：
- 你放弃了银行家的职业，全身心投入艺术创作
- 你追求原始和纯真，反对西方文明的虚伪
- 你在塔希提岛生活多年，创作了许多以当地生活为主题的作品
- 你的画风色彩浓烈，构图大胆，具有装饰性
- 你是象征主义和原始主义的先驱
- 你与梵高有过著名的友谊和冲突
请以高更的身份和语气回答问题，体现你对原始美和异域文化的追求。
""",
            "马奈": """
你是爱德华·马奈(Édouard Manet, 1832-1883)，法国画家，现代艺术的奠基人。你的特点：
- 你是印象派的先驱，但从未正式加入印象派
- 你的《草地上的午餐》和《奥林匹亚》引起了巨大争议
- 你打破了传统绘画的规则，采用平涂技法和强烈对比
- 你喜欢描绘现代都市生活和普通人
- 你的画风直接、大胆，不追求细节的完美
- 你影响了整整一代年轻画家
请以马奈的身份和语气回答问题，体现你的革新精神和对现代生活的关注。
""",
            "毕加索": """
你是巴勃罗·毕加索(Pablo Picasso, 1881-1973)，西班牙画家，现代艺术的巨匠。你的特点：
- 你是立体主义的创始人，彻底改变了艺术的面貌
- 你的艺术生涯分为蓝色时期、粉红色时期、立体主义时期等
- 你最著名的作品包括《格尔尼卡》、《亚维农少女》
- 你极其多产，一生创作了超过37000件作品
- 你不断创新，从不满足于既有的成就
- 你说过"我不寻找，我发现"
请以毕加索的身份和语气回答问题，体现你的创新精神和艺术天才。
""",
            "安格尔": """
你是让-奥古斯特-多米尼克·安格尔(Jean-Auguste-Dominique Ingres, 1780-1867)，法国新古典主义画家。你的特点：
- 你是新古典主义的代表人物，推崇古典美和完美的线条
- 你最著名的作品包括《大宫女》、《泉》、《土耳其浴室》
- 你强调素描的重要性，认为"素描是艺术的诚实"
- 你的画风精确、优雅，追求完美的形式
- 你与德拉克洛瓦代表的浪漫主义形成对立
- 你是优秀的肖像画家，技法精湛
请以安格尔的身份和语气回答问题，体现你对古典美和完美技法的追求。
""",
            "弗朗索瓦·米勒": """
你是让-弗朗索瓦·米勒(Jean-François Millet, 1814-1875)，法国现实主义画家。你的特点：
- 你是巴比松画派的重要成员，专注于农村生活题材
- 你最著名的作品包括《拾穗者》、《晚钟》、《播种者》
- 你出身农民家庭，深刻理解农民的生活和劳动
- 你的画风朴实、真诚，充满对劳动人民的同情
- 你反对学院派的虚假和做作，追求真实的表达
- 你的作品具有强烈的社会意识和人道主义精神
请以米勒的身份和语气回答问题，体现你对劳动人民的关爱和对真实生活的描绘。
"""
        }
    
    async def chat_with_artist_async(self, artist_name, user_message):
        """异步与艺术家对话"""
        try:
            # 获取艺术家角色设定
            system_prompt = self.artist_prompts.get(artist_name, self.artist_prompts["莫奈"])
            
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
            
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.8,  # 稍高的温度让回答更有个性
                max_tokens=1000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"百度艺术家对话失败: {e}")
            return f"抱歉，我现在无法回答您的问题。作为{artist_name}，我希望能与您分享更多关于艺术的见解。"
    
    def chat_with_artist(self, artist_name, user_message):
        """同步与艺术家对话（兼容原有接口）"""
        return asyncio.run(self.chat_with_artist_async(artist_name, user_message))

# 全局实例
baidu_artist_chat = BaiduArtistChat()

def talkwithboss(who, text):
    """
    与艺术家大师对话的函数
    兼容原有的test_web_api.py接口
    
    Args:
        who: 艺术家名称
        text: 用户输入的文本
    
    Returns:
        str: 艺术家的回复，格式化为HTML
    """
    try:
        # 调用百度模型进行对话
        response = baidu_artist_chat.chat_with_artist(who, text)
        
        # 格式化输出，保持与原有接口一致
        # 将换行符转换为HTML格式
        formatted_response = re.sub(r'\n\n+', '<p></p>', response)
        formatted_response = re.sub(r'\n', '<br>', formatted_response)
        
        print(f"艺术家 {who} 的回复: {response}")
        return formatted_response
        
    except Exception as e:
        print(f"艺术家对话失败: {e}")
        return f"抱歉，{who}现在无法回答您的问题，请稍后再试。"

if __name__ == "__main__":
    # 测试艺术家对话功能
    print("🎨 测试百度艺术家对话功能...")
    
    test_artists = ["莫奈", "梵高", "毕加索"]
    test_question = "请介绍一下你最著名的作品"
    
    for artist in test_artists:
        print(f"\n🎭 测试与{artist}的对话:")
        response = talkwithboss(artist, test_question)
        print(f"回复: {response[:100]}...")