#!/usr/bin/env python3
"""
统一的LLM接口，支持百度和讯飞模型切换
"""
import os
from model_config import get_current_provider, ModelProvider

# 获取当前配置的模型提供商
CURRENT_PROVIDER = get_current_provider()

def get_llm_functions():
    """根据配置返回对应的LLM函数"""
    global CURRENT_PROVIDER
    
    if CURRENT_PROVIDER == ModelProvider.BAIDU:
        try:
            from baidu_llm import (
                promptajust, bosssay, Core_tex, RAG_LLM, 
                Org_tex, llm_write, is_right
            )
            print("✅ 使用百度ERNIE模型")
            return {
                'promptajust': promptajust,
                'bosssay': bosssay,
                'Core_tex': Core_tex,
                'RAG_LLM': RAG_LLM,
                'Org_tex': Org_tex,
                'llm_write': llm_write,
                'is_right': is_right
            }
        except ImportError as e:
            print(f"❌ 百度模型导入失败: {e}")
            print("🔄 回退到讯飞模型")
            CURRENT_PROVIDER = ModelProvider.XUNFEI
    
    if CURRENT_PROVIDER == ModelProvider.XUNFEI:
        try:
            from LLM_xunfei2 import (
                promptajust, bosssay, Core_tex, RAG_LLM, 
                Org_tex, llm_write, is_right
            )
            print("✅ 使用讯飞星火模型")
            return {
                'promptajust': promptajust,
                'bosssay': bosssay,
                'Core_tex': Core_tex,
                'RAG_LLM': RAG_LLM,
                'Org_tex': Org_tex,
                'llm_write': llm_write,
                'is_right': is_right
            }
        except ImportError as e:
            print(f"❌ 讯飞模型导入失败: {e}")
            raise ImportError("无法导入任何LLM模型")

# 获取当前LLM函数
llm_funcs = get_llm_functions()

# 导出函数
promptajust = llm_funcs['promptajust']
bosssay = llm_funcs['bosssay']
Core_tex = llm_funcs['Core_tex']
RAG_LLM = llm_funcs['RAG_LLM']
Org_tex = llm_funcs['Org_tex']
llm_write = llm_funcs['llm_write']
is_right = llm_funcs['is_right']

# 保留讯飞的绘图功能（百度暂不支持）
try:
    from LLM_xunfei2 import draw
except ImportError:
    def draw(text):
        print("⚠️ 绘图功能需要讯飞模型支持")
        return None

if __name__ == "__main__":
    print(f"当前使用的模型提供商: {CURRENT_PROVIDER.value}")
    
    # 测试文本生成
    test_result = RAG_LLM("什么是彩虹？")
    print(f"测试结果: {test_result[:100]}...")