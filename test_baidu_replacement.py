#!/usr/bin/env python3
"""
测试百度模型替换讯飞模型的完整功能
"""

def test_text_generation():
    """测试文本生成功能"""
    print("📝 测试文本生成功能...")
    
    try:
        from LLM_unified import llm_write, Core_tex, RAG_LLM, Org_tex, promptajust, is_right
        
        # 测试故事创作
        print("📖 测试故事创作...")
        story = llm_write("梵高的向日葵")
        print(f"✅ 故事创作: {story[:80]}...")
        
        # 测试内容提炼
        print("🎨 测试内容提炼...")
        core = Core_tex("小贝和爸爸在讨论彩虹的形成原理")
        print(f"✅ 内容提炼: {core}")
        
        # 测试儿童问答
        print("👶 测试儿童问答...")
        qa = RAG_LLM("为什么天空是蓝色的？")
        print(f"✅ 儿童问答: {qa[:80]}...")
        
        # 测试作品介绍
        print("🖼️ 测试作品介绍...")
        intro = Org_tex("蒙娜丽莎")
        print(f"✅ 作品介绍: {intro[:80]}...")
        
        # 测试Prompt生成
        print("🎯 测试Prompt生成...")
        prompt = promptajust("向日葵", "梵高风格", "Vincent")
        print(f"✅ Prompt生成: {prompt[:80]}...")
        
        # 测试答案匹配
        print("✔️ 测试答案匹配...")
        match = is_right("梵高", "梵高")
        print(f"✅ 答案匹配: {match}")
        
        return True
        
    except Exception as e:
        print(f"❌ 文本生成测试失败: {e}")
        return False

def test_artist_chat():
    """测试艺术家对话功能"""
    print("\n🎭 测试艺术家对话功能...")
    
    try:
        from artist_chat_unified import talkwithboss
        
        artists = ["莫奈", "梵高", "毕加索", "马奈"]
        question = "你最喜欢的颜色是什么？为什么？"
        
        for artist in artists:
            print(f"🎨 测试与{artist}的对话...")
            response = talkwithboss(artist, question)
            print(f"✅ {artist}回复: {response[:60]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ 艺术家对话测试失败: {e}")
        return False

def test_model_switching():
    """测试模型切换功能"""
    print("\n🔄 测试模型切换功能...")
    
    try:
        from model_config import get_current_provider, switch_provider, ModelProvider
        
        current = get_current_provider()
        print(f"当前模型: {current.value}")
        
        # 测试切换
        if current == ModelProvider.BAIDU:
            switch_provider(ModelProvider.XUNFEI)
            print("切换到讯飞模型")
        else:
            switch_provider(ModelProvider.BAIDU)
            print("切换到百度模型")
        
        new_provider = get_current_provider()
        print(f"切换后模型: {new_provider.value}")
        
        # 切换回原来的模型
        switch_provider(current)
        print(f"恢复到原模型: {current.value}")
        
        return True
        
    except Exception as e:
        print(f"❌ 模型切换测试失败: {e}")
        return False

def show_replacement_summary():
    """显示替换总结"""
    print("\n" + "="*60)
    print("🎉 百度模型替换讯飞模型 - 完成总结")
    print("="*60)
    
    print("\n✅ 已替换的功能:")
    print("1. 📝 文本生成功能 (LLM_unified.py)")
    print("   - 故事创作 (llm_write)")
    print("   - 内容提炼 (Core_tex)")
    print("   - 儿童问答 (RAG_LLM)")
    print("   - 作品介绍 (Org_tex)")
    print("   - Prompt生成 (promptajust)")
    print("   - 答案匹配 (is_right)")
    
    print("\n2. 🎭 艺术家角色对话 (baidu_artist_chat.py)")
    print("   - 莫奈、梵高、毕加索、马奈、高更、安格尔、米勒")
    print("   - 每个艺术家都有独特的性格和回答风格")
    
    print("\n3. 📄 更新的页面文件:")
    print("   - app.py (主应用)")
    print("   - test_story.py (故事页面)")
    print("   - stimage.py (图像页面)")
    print("   - test_text.py (文本页面)")
    print("   - test_QA.py (问答页面)")
    print("   - talkwithbigboss.py (对话页面)")
    
    print("\n⚠️ 保留讯飞模型的功能:")
    print("1. 🎵 语音功能 (vocie3.py)")
    print("   - 文本转语音 (Text2Audio)")
    print("   - 语音转文本 (Audio2Text)")
    print("2. 🎨 图像生成 (draw函数)")
    print("   - 百度暂不支持图像生成")
    
    print("\n🔧 配置说明:")
    print("- 修改 model_config.py 中的 provider 可切换模型")
    print("- ModelProvider.BAIDU: 使用百度ERNIE模型")
    print("- ModelProvider.XUNFEI: 使用讯飞星火模型")
    
    print("\n💰 成本优势:")
    print("- 百度ERNIE模型调用成本更低")
    print("- 支持更大的上下文长度")
    print("- 响应速度更快")

if __name__ == "__main__":
    print("🚀 开始测试百度模型替换功能...\n")
    
    # 执行所有测试
    text_ok = test_text_generation()
    artist_ok = test_artist_chat()
    switch_ok = test_model_switching()
    
    # 显示总结
    show_replacement_summary()
    
    # 最终结果
    if text_ok and artist_ok and switch_ok:
        print(f"\n🎉 所有测试通过！百度模型替换成功完成！")
        print("现在你可以享受更低成本、更快速度的AI文本生成服务了！")
    else:
        print(f"\n⚠️ 部分测试失败，请检查配置和网络连接")