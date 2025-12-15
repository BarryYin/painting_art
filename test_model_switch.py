#!/usr/bin/env python3
"""
测试模型切换功能
"""

def test_baidu_model():
    """测试百度模型"""
    print("🧪 测试百度模型...")
    
    try:
        from LLM_unified import RAG_LLM, llm_write, is_right
        
        # 测试儿童问答
        print("📚 测试儿童问答功能...")
        result1 = RAG_LLM("什么是彩虹？")
        print(f"✅ 儿童问答: {result1[:50]}...")
        
        # 测试故事创作
        print("📖 测试故事创作功能...")
        result2 = llm_write("莫奈的睡莲")
        print(f"✅ 故事创作: {result2[:50]}...")
        
        # 测试答案匹配
        print("🎯 测试答案匹配功能...")
        result3 = is_right("莫奈", "莫奈")
        print(f"✅ 答案匹配: {result3}")
        
        return True
        
    except Exception as e:
        print(f"❌ 百度模型测试失败: {e}")
        return False

def test_model_switch():
    """测试模型切换"""
    print("🔄 测试模型切换功能...")
    
    try:
        from model_config import switch_provider, ModelProvider, get_current_provider
        
        print(f"当前模型: {get_current_provider().value}")
        
        # 切换到讯飞模型（如果当前是百度）
        current = get_current_provider()
        if current == ModelProvider.BAIDU:
            print("切换到讯飞模型...")
            switch_provider(ModelProvider.XUNFEI)
        else:
            print("切换到百度模型...")
            switch_provider(ModelProvider.BAIDU)
            
        print(f"切换后模型: {get_current_provider().value}")
        return True
        
    except Exception as e:
        print(f"❌ 模型切换测试失败: {e}")
        return False

if __name__ == "__main__":
    print("🚀 开始测试模型替换功能...\n")
    
    # 测试百度模型
    baidu_ok = test_baidu_model()
    print()
    
    # 测试模型切换
    switch_ok = test_model_switch()
    print()
    
    if baidu_ok and switch_ok:
        print("🎉 所有测试通过！百度模型替换成功！")
        print("\n📋 使用说明:")
        print("1. 默认使用百度ERNIE模型进行文本生成")
        print("2. 如需切换回讯飞模型，修改 model_config.py 中的 provider 配置")
        print("3. 绘图功能仍使用讯飞模型（百度暂不支持）")
        print("4. 语音功能仍使用讯飞模型")
    else:
        print("⚠️ 部分测试失败，请检查配置")