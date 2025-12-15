# 🎨 法国绘画艺术教育平台

一个基于AI的互动式法国绘画艺术教育平台，专为儿童设计，通过与艺术大师对话、故事创作、语音互动等方式，让孩子们轻松学习法国绘画艺术。

## ✨ 主要功能

### 🎭 与艺术大师对话
- **7位法国艺术大师**：莫奈、梵高、毕加索、马奈、高更、安格尔、弗朗索瓦·米勒
- **角色扮演对话**：每位艺术家都有独特的性格和回答风格
- **实时互动**：支持文字和语音输入，获得艺术家的个性化回复

### 📚 智能故事创作
- **艺术故事生成**：基于艺术作品创作适合8-12岁儿童的教育故事
- **角色设定**：以小贝和琪琪博士的对话形式展现
- **寓教于乐**：在故事中学习绘画技法、艺术历史和创作背景

### 🎵 语音互动功能
- **语音问答**：支持语音提问，AI语音回答
- **音频播放**：自动生成和播放教育内容的音频版本
- **语音识别**：智能识别儿童语音输入

### 🎨 AI绘画助手
- **Prompt生成**：将中文描述转换为专业的AI绘画提示词
- **风格指导**：支持不同艺术风格的绘画指导
- **作品解析**：详细介绍艺术作品的创作背景和技法

### 👶 儿童百科问答
- **年龄适配**：专为3-8岁儿童设计的问答系统
- **简单易懂**：用儿童能理解的语言解释复杂概念
- **启发思考**：引导孩子主动思考和探索

## 🚀 快速开始

### 环境要求
- Python 3.10+
- Conda (推荐) 或 pip

### 安装步骤

1. **创建虚拟环境**
```bash
conda create -n art python=3.10
conda activate art
```

2. **克隆项目**
```bash
git clone https://github.com/BarryYin/painting_art.git
cd painting_art
```

3. **安装依赖**
```bash
pip install -r requirement.txt
```

4. **配置API密钥**
```bash
# 复制环境变量模板
cp .env.example .env

# 编辑.env文件，填入你的API密钥
nano .env
```

5. **启动应用**
```bash
streamlit run app.py
```

6. **访问应用**
打开浏览器访问：`http://localhost:8501`

## 🔧 配置说明

### 🔐 安全配置

项目使用环境变量保护API密钥，请参考 [安全配置指南](SECURITY.md) 进行配置。

### 环境变量配置

在`.env`文件中配置以下变量：

```bash
# 百度ERNIE模型配置
BAIDU_API_KEY=你的百度API密钥
BAIDU_BASE_URL=https://qianfan.baidubce.com/v2
BAIDU_MODEL=ernie-4.5-turbo-32k

# 讯飞星火模型配置
XUNFEI_APP_ID=你的讯飞APP_ID
XUNFEI_API_KEY=你的讯飞API_KEY
XUNFEI_API_SECRET=你的讯飞API_SECRET
XUNFEI_DOMAIN=generalv3.5

# 默认模型提供商
DEFAULT_PROVIDER=baidu
```

### 验证配置
```bash
python config.py
```

## 📁 项目结构

```
painting_art/
├── app.py                      # 主应用入口
├── model_config.py             # AI模型配置
├── LLM_unified.py             # 统一LLM接口
├── baidu_llm.py               # 百度模型封装
├── baidu_artist_chat.py       # 百度艺术家对话
├── artist_chat_unified.py     # 统一艺术家对话接口
├── LLM_xunfei2.py            # 讯飞模型功能
├── test_web_api.py           # 讯飞艺术家对话
├── vocie3.py                 # 语音处理功能
├── data_change.py            # 数据处理
├── testimage.py              # 图像处理
├── modify_mp3.py             # 音频处理
├── pages/                    # 页面组件
├── test_*.py                 # 各功能测试页面
└── requirement.txt           # 项目依赖
```

## 🎯 功能模块

### 文本生成模块
- **llm_write**: 创作儿童艺术教育故事
- **Core_tex**: 从对话中提炼插画关键词
- **RAG_LLM**: 儿童百科问答助手
- **Org_tex**: 艺术作品和画家介绍
- **promptajust**: AI绘画提示词生成
- **is_right**: 语音识别结果验证

### 语音交互模块
- **process_text**: 文本转语音处理
- **Audio2Text**: 语音转文本识别
- **modify_mp3**: 音频文件处理

### 艺术家对话模块
- **talkwithboss**: 与7位艺术大师对话
- 支持个性化角色扮演
- 智能上下文理解

## 🧪 测试功能

项目提供了完整的测试套件：

```bash
# 测试百度模型功能
python test_baidu_replacement.py

# 测试模型切换
python test_model_switch.py

# 测试艺术家对话
python baidu_artist_chat.py

# 测试统一接口
python LLM_unified.py
```

## 📊 支持的艺术家

| 艺术家 | 时期 | 代表作品 | 艺术风格 |
|--------|------|----------|----------|
| 莫奈 | 1840-1926 | 《睡莲》《印象·日出》 | 印象派 |
| 梵高 | 1853-1890 | 《星夜》《向日葵》 | 后印象派 |
| 毕加索 | 1881-1973 | 《格尔尼卡》《亚维农少女》 | 立体主义 |
| 马奈 | 1832-1883 | 《草地上的午餐》《奥林匹亚》 | 现实主义 |
| 高更 | 1848-1903 | 《塔希提岛系列》 | 后印象派 |
| 安格尔 | 1780-1867 | 《大宫女》《泉》 | 新古典主义 |
| 米勒 | 1814-1875 | 《拾穗者》《晚钟》 | 现实主义 |

## 💡 使用技巧

### 与艺术家对话
- 可以询问艺术家的生平、创作理念、代表作品
- 每位艺术家都有独特的回答风格和语气
- 支持深度的艺术讨论和技法交流

### 故事创作
- 输入艺术家名字或作品名称
- 系统会生成适合儿童的教育故事
- 故事以小贝和琪琪博士对话形式呈现

### 语音功能
- 点击录音按钮进行语音输入
- 系统会自动识别并生成语音回复
- 支持音频文件的播放和下载

## 🔄 模型切换

项目支持灵活的模型切换：

1. **百度ERNIE模型**（推荐）
   - 成本更低
   - 响应更快
   - 中文理解能力强
   - 支持32K上下文

2. **讯飞星火模型**
   - 支持语音功能
   - 支持图像生成
   - 专业艺术智能体

## 🛠️ 开发指南

### 添加新的艺术家
1. 在 `baidu_artist_chat.py` 中添加艺术家角色设定
2. 在 `test_web_api.py` 中添加对应的智能体ID
3. 更新艺术家列表和测试用例

### 扩展功能模块
1. 在对应的LLM文件中添加新函数
2. 在 `LLM_unified.py` 中注册新功能
3. 更新页面文件调用新功能

### 自定义模型
1. 创建新的模型封装文件
2. 在 `model_config.py` 中添加配置
3. 在统一接口中添加支持

## 📝 更新日志

### v2.0.0 (2024-12-15)
- ✨ 集成百度ERNIE模型
- 🎭 重构艺术家对话系统
- 🔧 添加灵活的模型切换机制
- 📊 优化成本和性能
- 🧪 完善测试套件

### v1.0.0 (2024-08-01)
- 🎨 基础艺术教育功能
- 🎵 语音交互系统
- 📚 故事创作功能
- 👶 儿童问答助手

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- 感谢百度智能云提供ERNIE模型支持
- 感谢讯飞开放平台提供语音和图像生成能力
- 感谢Streamlit提供优秀的Web应用框架

## 📞 联系方式

- 项目地址：[https://github.com/BarryYin/painting_art](https://github.com/BarryYin/painting_art)
- 问题反馈：[Issues](https://github.com/BarryYin/painting_art/issues)

---

**让艺术教育更有趣，让孩子们在与大师的对话中感受艺术的魅力！** 🎨✨