#!/usr/bin/env python3
"""
安全的配置管理
使用环境变量保护API密钥
"""
import os
from dotenv import load_dotenv
from enum import Enum

# 加载环境变量
load_dotenv()

class ModelProvider(Enum):
    BAIDU = "baidu"
    XUNFEI = "xunfei"

class Config:
    """配置管理类"""
    
    # 百度模型配置
    BAIDU_API_KEY = os.getenv('BAIDU_API_KEY', '')
    BAIDU_BASE_URL = os.getenv('BAIDU_BASE_URL', 'https://qianfan.baidubce.com/v2')
    BAIDU_MODEL = os.getenv('BAIDU_MODEL', 'ernie-4.5-turbo-32k')
    
    # 讯飞模型配置
    XUNFEI_APP_ID = os.getenv('XUNFEI_APP_ID', '')
    XUNFEI_API_KEY = os.getenv('XUNFEI_API_KEY', '')
    XUNFEI_API_SECRET = os.getenv('XUNFEI_API_SECRET', '')
    XUNFEI_DOMAIN = os.getenv('XUNFEI_DOMAIN', 'generalv3.5')
    
    # 默认提供商
    DEFAULT_PROVIDER = ModelProvider(os.getenv('DEFAULT_PROVIDER', 'baidu'))
    
    @classmethod
    def get_baidu_config(cls):
        """获取百度模型配置"""
        if not cls.BAIDU_API_KEY:
            raise ValueError("百度API密钥未配置，请设置BAIDU_API_KEY环境变量")
        
        return {
            "api_key": cls.BAIDU_API_KEY,
            "base_url": cls.BAIDU_BASE_URL,
            "model": cls.BAIDU_MODEL,
            "temperature": 0.7
        }
    
    @classmethod
    def get_xunfei_config(cls):
        """获取讯飞模型配置"""
        if not all([cls.XUNFEI_APP_ID, cls.XUNFEI_API_KEY, cls.XUNFEI_API_SECRET]):
            raise ValueError("讯飞API密钥未完整配置，请设置XUNFEI_APP_ID、XUNFEI_API_KEY、XUNFEI_API_SECRET环境变量")
        
        return {
            "app_id": cls.XUNFEI_APP_ID,
            "api_key": cls.XUNFEI_API_KEY,
            "api_secret": cls.XUNFEI_API_SECRET,
            "domain": cls.XUNFEI_DOMAIN
        }
    
    @classmethod
    def get_current_provider(cls):
        """获取当前配置的模型提供商"""
        return cls.DEFAULT_PROVIDER
    
    @classmethod
    def validate_config(cls):
        """验证配置是否完整"""
        errors = []
        
        # 检查百度配置
        if cls.DEFAULT_PROVIDER == ModelProvider.BAIDU and not cls.BAIDU_API_KEY:
            errors.append("百度API密钥未配置")
        
        # 检查讯飞配置
        if cls.DEFAULT_PROVIDER == ModelProvider.XUNFEI:
            if not cls.XUNFEI_APP_ID:
                errors.append("讯飞APP_ID未配置")
            if not cls.XUNFEI_API_KEY:
                errors.append("讯飞API_KEY未配置")
            if not cls.XUNFEI_API_SECRET:
                errors.append("讯飞API_SECRET未配置")
        
        if errors:
            raise ValueError(f"配置验证失败: {', '.join(errors)}")
        
        return True

if __name__ == "__main__":
    # 测试配置
    try:
        Config.validate_config()
        print("✅ 配置验证通过")
        print(f"当前提供商: {Config.get_current_provider().value}")
    except ValueError as e:
        print(f"❌ 配置错误: {e}")
        print("请参考 .env.example 文件配置环境变量")