#!/usr/bin/env python3
"""
模型配置文件
使用环境变量保护API密钥
"""

from config import Config, ModelProvider

# 使用安全的配置管理
MODEL_CONFIG = {
    # 当前使用的模型提供商
    "provider": Config.get_current_provider(),
    
    # 百度模型配置（从环境变量读取）
    "baidu": Config.get_baidu_config() if Config.BAIDU_API_KEY else {},
    
    # 讯飞模型配置（从环境变量读取）
    "xunfei": Config.get_xunfei_config() if all([Config.XUNFEI_APP_ID, Config.XUNFEI_API_KEY, Config.XUNFEI_API_SECRET]) else {}
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