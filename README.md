# 🎰 FluxA 扭蛋机 MVP

> 基于FluxA Wallet的AI Agent微支付Demo

## 📱 手机适配

✅ **完全响应式设计**:
- 320px - 428px 屏幕完美适配
- 触摸优化
- 流畅动画

## 🚀 部署到Vercel

1. 访问: https://vercel.com/new
2. 导入: `cynthiaxu0529-art/fluxa-gacha`
3. 配置:
   - Framework: Other
   - Build: `echo "No build needed"`
   - Output: `.`
4. Deploy

## 🌐 访问

- Vercel: https://fluxa-gacha.vercel.app
- 自定义域名: `gacha.fluxapay.xyz`

## 💰 支付流程

```
用户 → 扭蛋(0.01 USDC) → FluxA支付 → AI奖品
```

## 📦 文件结构

```
fluxa-gacha/
├── index.html           # ✅ 前端页面 (根目录!)
├── api/
│   ├── status.py
│   ├── create_payment.py
│   └── draw.py
├── vercel.json          # Vercel配置
└── README.md
```

## ⚠️ 注意

- 前端必须放在**根目录** (`index.html`)
- API在 `/api/` 目录
- Vercel会自动处理SPA路由

## 🔗 链接

- GitHub: https://github.com/cynthiaxu0529-art/fluxa-gacha
- FluxA: https://fluxapay.xyz

---

*Built with FluxA Wallet 🦞*
