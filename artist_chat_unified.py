#!/usr/bin/env python3
"""
统一的艺术家对话接口
支持百度和讯飞模型切换
"""
from model_config import get_current_provider, ModelProvider

def get_artist_chat_function():
    """根据配置返回对应的艺术家对话函数"""
    current_provider = get_current_provider()
    
    if current_provider == ModelProvider.BAIDU:
        try:
            from baidu_artist_chat import talkwithboss
            print("✅ 使用百度模型进行艺术家对话")
            return talkwithboss
        except ImportError as e:
            print(f"❌ 百度艺术家对话导入失败: {e}")
            print("🔄 回退到讯飞模型")
    
    # 回退到讯飞模型
    try:
        from test_web_api import talkwithboss
        print("✅ 使用讯飞智能体进行艺术家对话")
        return talkwithboss
    except ImportError as e:
        print(f"❌ 讯飞艺术家对话导入失败: {e}")
        raise ImportError("无法导入任何艺术家对话模型")

# 获取当前艺术家对话函数
talkwithboss = get_artist_chat_function()

if __name__ == "__main__":
    # 测试艺术家对话
    print("🎨 测试统一艺术家对话接口...")
    result = talkwithboss("莫奈", "你好，请介绍一下你自己")
    print(f"测试结果: {result[:100]}...")