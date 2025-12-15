# 🔐 安全配置指南

本项目使用环境变量来保护API密钥和其他敏感信息，确保这些信息不会被意外提交到版本控制系统中。

## 📋 配置步骤

### 1. 复制环境变量模板
```bash
cp .env.example .env
```

### 2. 编辑.env文件
在项目根目录的`.env`文件中填入你的真实API密钥：

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

# 默认使用的模型提供商
DEFAULT_PROVIDER=baidu
```

### 3. 验证配置
运行配置验证脚本：
```bash
python config.py
```

如果配置正确，会显示：
```
✅ 配置验证通过
当前提供商: baidu
```

## 🔑 获取API密钥

### 百度ERNIE模型
1. 访问 [百度智能云千帆大模型平台](https://qianfan.baidubce.com/)
2. 注册并登录账号
3. 创建应用获取API Key
4. 将API Key填入`.env`文件的`BAIDU_API_KEY`

### 讯飞星火模型
1. 访问 [讯飞开放平台](https://console.xfyun.cn/)
2. 注册并登录账号
3. 创建星火认知大模型应用
4. 获取APPID、APIKey、APISecret
5. 分别填入`.env`文件对应字段

## ⚠️ 安全注意事项

### 重要提醒
- **绝不要**将`.env`文件提交到Git仓库
- **绝不要**在代码中硬编码API密钥
- **绝不要**在公开场合分享你的API密钥
- **定期轮换**你的API密钥

### 文件保护
项目已配置`.gitignore`来防止敏感文件被提交：
```
.env
.env.local
.env.production
.env.staging
*.key
*.pem
config_local.py
```

### 环境隔离
建议为不同环境使用不同的API密钥：
- 开发环境：使用测试密钥
- 生产环境：使用正式密钥
- 演示环境：使用受限密钥

## 🚨 泄露应急处理

如果不小心泄露了API密钥：

1. **立即撤销**泄露的密钥
2. **生成新的**API密钥
3. **更新配置**文件中的密钥
4. **检查日志**是否有异常调用
5. **通知团队**成员更新本地配置

## 🔧 故障排除

### 常见错误

**错误1**: `ValueError: 百度API密钥未配置`
- 解决：检查`.env`文件中的`BAIDU_API_KEY`是否正确设置

**错误2**: `ValueError: 讯飞API密钥未完整配置`
- 解决：确保`XUNFEI_APP_ID`、`XUNFEI_API_KEY`、`XUNFEI_API_SECRET`都已设置

**错误3**: 模型调用失败
- 解决：验证API密钥是否有效，检查网络连接

### 调试模式
设置环境变量启用调试模式：
```bash
export DEBUG=true
python config.py
```

## 📞 技术支持

如果遇到配置问题：
1. 查看 [项目文档](README.md)
2. 提交 [Issue](https://github.com/BarryYin/painting_art/issues)
3. 联系项目维护者

---

**记住：安全是每个人的责任！** 🛡️