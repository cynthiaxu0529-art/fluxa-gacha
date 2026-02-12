# 🎰 FluxA 扭蛋机 MVP

> 基于FluxA Wallet的AI Agent微支付Demo

## 📱 手机适配

✅ **完全响应式设计**:
- 320px - 428px 屏幕完美适配
- 触摸优化 (tap-highlight-color: transparent)
- 大按钮 (44px+ 触摸区域)
- 流畅动画 (transform: scale)

## 🚀 部署到Vercel

### 方式1: GitHub自动部署 (推荐)

1. 访问: https://vercel.com/new
2. 点击: "Import Git Repository"
3. 选择: `cynthiaxu0529-art/fluxa-gacha`
4. 配置:
   - Framework Preset: **Other**
   - Build Command: `echo "No build needed"`
   - Output Directory: `.`
5. 点击: **Deploy**

### 方式2: Vercel CLI

```bash
npm i -g vercel
vercel --yes
```

### 方式3: Cloudflare Pages (免费替代)

1. 访问: https://dash.cloudflare.com
2. Pages → Connect GitHub
3. 选择仓库: `fluxa-gacha`
4. 部署

## 🌐 部署后

### 访问地址
- Vercel: `https://fluxa-gacha.vercel.app`
- 自定义: `gacha.fluxapay.xyz` → Vercel项目

### API端点
- `/api/status` - 状态检查
- `/api/create_payment` - 创建支付
- `/api/draw` - 抽奖

## 🎯 核心卖点

| 卖点 | 说明 |
|------|------|
| 💰 **超低门槛** | 仅0.01 USDC |
| 📱 **手机适配** | 完美移动端体验 |
| 🔐 **安全支付** | x402协议 |
| ⚡ **秒级体验** | 快速响应 |

## 📱 前端特点

- 响应式设计 (320px-428px)
- 触摸优化
- 流畅动画
- 轻量级 (9KB)

## 💰 支付流程

```
用户 → 点击扭蛋 → FluxA支付(0.01 USDC) → 获得奖品
         ↓
    x402协议 → FluxA Wallet → 自动验证
```

## 🎁 奖品类型

| 奖品 | 内容 |
|------|------|
| 📝 藏头诗 | AI定制藏头诗 |
| 🔮 运势 | 今日运势 |
| 😂 笑话 | 冷笑话 |
| 🎨 Prompt | AI画图Prompt |
| 🧧 祝福 | 祝福语 |

## 📦 文件结构

```
fluxa-gacha/
├── index.html           # 主页 (手机适配)
├── api/
│   ├── status.py       # 状态API
│   ├── create_payment.py  # 支付API
│   └── draw.py         # 抽奖API
├── templates/
│   └── index.html     # 前端页面
├── vercel.json         # Vercel配置
├── deploy.sh           # 部署脚本
└── README.md           # 本文档
```

## 🔗 链接

- **仓库**: https://github.com/cynthiaxu0529-art/fluxa-gacha
- **演示**: https://fluxa-gacha.vercel.app (部署后)
- **FluxA**: https://fluxapay.xyz

## ⚠️ Mandate授权

首次使用需要授权:
```
https://agentwallet.fluxapay.xyz/onboard/intent?oid=oi_MZThuSoaxV057wA6SdGb4rz6
```

---

*Built with FluxA Wallet 🦞*
