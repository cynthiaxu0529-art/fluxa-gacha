# 🎰 FluxA 扭蛋机 MVP

> 基于FluxA Wallet的AI Agent微支付系统

## 📖 概述

扭蛋机MVP是一个使用FluxA Wallet x402支付的微支付Demo：
- 用户支付 **0.01 USDC**
- 随机获得 **AI服务奖励**
- 完全 **自主运营**

## 🎯 核心卖点

| 卖点 | 说明 |
|------|------|
| 💰 **超低门槛** | 仅0.01 USDC |
| 🤖 **AI奖励** | 每次都有AI生成内容 |
| 🔐 **安全支付** | x402协议 + FluxA托管 |
| ⚡ **秒级到账** | 支付完成即获奖 |
| 🎮 **趣味性强** | 扭蛋机制增加期待感 |

## 🎰 扭蛋奖品

| 奖品 | 内容 |
|------|------|
| 📝 藏头诗 | AI生成藏头诗 |
| 🔮 运势 | 每日运势 |
| 😂 笑话 | 冷笑话 |
| 🎨 Prompt | AI画图Prompt |
| 🧧 祝福 | 祝福语 |
| ❄️ 冷知识 | 有趣知识 |
| 💪 励志 | 励志语录 |
| 💻 代码 | 代码片段 |

## 🚀 快速开始

```bash
# 运行MVP
python3 fluxa_gacha_mvp.py

# 或启动Web服务
python3 -m http.server 8080
```

## 📁 文件结构

```
fluxa_gacha/
├── fluxa_gacha_mvp.py    # 核心逻辑
├── README.md              # 本文档
├── api_server.py           # API服务 (可选)
├── gacha_main.png         # 🎰 宣传主图
├── templates/
│   └── index.html         # 前端页面
├── fluxa_api_analysis.md   # API能力分析
└── promotion_copy.md       # 宣传文案
```

## 🎨 宣传图片

![扭蛋机主图](gacha_main.png)

### 图片提示词

详细提示词见: `image_prompts.md`

## 💰 支付流程

```
用户 → 选择扭蛋 → FluxA支付(0.01 USDC) → 获得奖品
         ↓
    x402协议 → FluxA Wallet → 自动验证
```

## 🔧 技术栈

- **后端**: Python 3
- **支付**: FluxA Wallet (x402)
- **网络**: Base (USDC)
- **API**: FluxA MCP

## 📱 社交媒体

### Twitter/X
```
🎰 Just 0.01 USDC = 1 Gacha Pull!
🤖 AI Poem • Fortune • Joke • Prompt • Blessing
Powered by @FluxA_Wallet
#AI #x402 #MicroPayment #Web3
```

### 小红书
```
🎰 0.01 USDC 扭一次！
AI帮我写藏头诗、算运势、讲笑话🤖
💰 微支付·新体验 | 🔐 x402协议·安全可靠
```

## 🔗 相关链接

- **FluxA官网**: https://fluxapay.xyz/
- **Agent ID API**: https://agentid.fluxapay.xyz
- **Wallet API**: https://walletapi.fluxapay.xyz

## 📊 后续计划

- [ ] AI实际生成内容
- [ ] 多种奖品池
- [ ] 概率调控
- [ ] 多Agent支付
- [ ] 商家接入

---

*Built with FluxA Wallet 🦞*
