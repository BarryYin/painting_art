#!/usr/bin/env python3
"""
讯飞模型安全配置
使用环境变量保护API密钥
"""
from config import Config
from dwspark.config import Config as DwsparkConfig

def get_xunfei_config():
    """获取讯飞模型配置"""
    try:
        xunfei_config = Config.get_xunfei_config()
        return DwsparkConfig(
            xunfei_config['app_id'],
            xunfei_config['api_key'],
            xunfei_config['api_secret']
        )
    except ValueError as e:
        print(f"⚠️ 讯飞配置错误: {e}")
        print("请在.env文件中配置XUNFEI_APP_ID、XUNFEI_API_KEY、XUNFEI_API_SECRET")
        return None

# 导出配置实例
xunfei_config = get_xunfei_config()

if __name__ == "__main__":
    if xunfei_config:
        print("✅ 讯飞配置加载成功")
    else:
        print("❌ 讯飞配置加载失败")