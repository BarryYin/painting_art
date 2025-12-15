#!/usr/bin/env python3
"""
模型配置文件
可以在这里轻松切换使用的AI模型提供商
"""

from enum import Enum

class ModelProvider(Enum):
    BAIDU = "baidu"
    XUNFEI = "xunfei"

# 配置项
MODEL_CONFIG = {
    # 当前使用的模型提供商
    "provider": ModelProvider.BAIDU,  # 改为 ModelProvider.XUNFEI 可切换到讯飞
    
    # 百度模型配置
    "baidu": {
        "api_key": "bce-v3/ALTAK-IlAGWrpPIFAMJ3g8kbD4I/f17c0a909b891c89b0dce53d913448d86a87bad9",
        "base_url": "https://qianfan.baidubce.com/v2",
        "model": "ernie-4.5-turbo-32k",
        "temperature": 0.7
    },
    
    # 讯飞模型配置
    "xunfei": {
        "app_id": "3a115b20",
        "api_key": "9d1b7a738c3e63a79656df4222d12cef",
        "api_secret": "ZGMyMzA3MGFlM2MzM2UxZWE1YTJhYjgw",
        "domain": "generalv3.5"
    }
}

def get_current_provider():
    """获取当前配置的模型提供商"""
    return MODEL_CONFIG["provider"]

def get_provider_config(provider=None):
    """获取指定提供商的配置"""
    if provider is None:
        provider = get_current_provider()
    
    return MODEL_CONFIG.get(provider.value, {})

def switch_provider(provider):
    """切换模型提供商"""
    if isinstance(provider, str):
        provider = ModelProvider(provider)
    
    MODEL_CONFIG["provider"] = provider
    print(f"✅ 已切换到 {provider.value} 模型")

if __name__ == "__main__":
    print(f"当前模型提供商: {get_current_provider().value}")
    print(f"配置信息: {get_provider_config()}")