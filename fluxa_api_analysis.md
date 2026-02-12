# FluxA扭蛋机 - API需求与能力分析

> 分析当前FluxA API能力与扭蛋机MVP的需求对比

---

## ✅ 已有能力 (已验证)

### 1. Agent ID注册
```bash
POST https://agentid.fluxapay.xyz/register
```
- ✅ 邮箱注册
- ✅ Agent名称
- ✅ Client信息
- ✅ 返回: agent_id, token, JWT

### 2. x402支付
```bash
POST https://walletapi.fluxapay.xyz/api/payment/x402V1Payment
```
- ✅ EIP-3009支付
- ✅ USDC支持
- ✅ Base网络
- ✅ Mandate授权

### 3. Mandate创建
```bash
POST https://walletapi.fluxapay.xyz/api/mandates/create-intent
```
- ✅ 自然语言描述
- ✅ 金额限制
- ✅ 时间限制
- ✅ 授权URL

### 4. 支付验证
```bash
GET /api/mandates/agent/{mandateId}
```
- ✅ 查询状态
- ✅ 花费金额
- ✅ 剩余额度

---

## ❌ 待补充能力 (MVP需求)

### 1. 支付链接生成

**现状**: 需要手动构建支付URL

**需求**: 
```python
# 期望的API
payment_link = fluxa.create_payment_link(
    amount=0.01,
    description="扭蛋机-一次惊喜",
    metadata={"gacha": True}
)
# 返回: payment_url, payment_id, qr_code
```

**建议添加**:
```
POST /api/payments/create-link
{
    "amount": "10000",
    "currency": "USDC", 
    "description": "扭蛋机",
    "metadata": {"game": "gacha"},
    "expiresIn": 3600
}
```

---

### 2. Webhook通知

**现状**: 无 webhook支持

**需求**:
```python
# 用户支付完成后，FluxA回调我们的服务器
@router.post("/webhook/fluxa")
async def fluxa_webhook(data: PaymentConfirmed):
    order_id = data.metadata.order_id
    await update_order_status(order_id, "paid")
    await send_prize(order_id)
```

**建议添加**:
```
POST /api/webhooks/register
{
    "url": "https://our-server.com/webhook",
    "events": ["payment.completed", "payment.failed"],
    "secret": "webhook_secret"
}
```

---

### 3. 退款/取消

**现状**: 无退款API

**需求**:
```python
# 如果支付超时或失败，需要退款
refund = await fluxa.refund(
    payment_id="pay_xxx",
    reason="支付超时"
)
```

**建议添加**:
```
POST /api/payments/{paymentId}/refund
{
    "reason": "超时/失败/用户取消"
}
```

---

### 4. 多链USDC

**现状**: 仅支持Base

**需求**:
```python
# 扭蛋机可能需要多链支持
payment = await fluxa.pay(
    amount=0.01,
    chain="arbitrum",  # 或"optimism"
    token="USDC"
)
```

**建议添加**:
```
POST /api/payment/estimate
{
    "amount": "10000",
    "fromChain": "base",
    "toChain": "arbitrum"
}
```

---

### 5. 批量支付

**现状**: 单笔支付

**需求**:
```python
# 运营活动可能需要批量发放奖励
batch = await fluxa.batch_pay([
    {"to": "0x...", "amount": 0.01, "memo": "奖品A"},
    {"to": "0x...", "amount": 0.01, "memo": "奖品B"},
])
```

**建议添加**:
```
POST /api/payments/batch
{
    "payments": [
        {"to": "0x...", "amount": "10000", "memo": "奖品"},
        ...
    ]
}
```

---

## 📊 API能力对比表

| 功能 | 当前状态 | 优先级 | 影响 |
|------|----------|--------|------|
| Agent注册 | ✅ 完整 | 高 | 无 |
| x402支付 | ✅ 完整 | 高 | 无 |
| Mandate | ✅ 完整 | 高 | 无 |
| 支付链接 | ❌ 需手动 | 中 | 开发成本 |
| Webhook | ❌ 无 | 高 | 无法自动发货 |
| 退款 | ❌ 无 | 中 | 风险控制 |
| 多链 | ❌ 仅Base | 低 | 扩展性 |
| 批量支付 | ❌ 无 | 低 | 运营效率 |

---

## 🎯 建议优先级

### P0 (必须)

1. **Webhook通知**
   - 原因: 支付后自动发货
   - 影响: 无法实现完整闭环

### P1 (重要)

2. **支付链接生成**
   - 原因: 前端简化
   - 影响: 开发成本略增

3. **退款API**
   - 原因: 风险控制
   - 影响: 资金安全

### P2 (可选)

4. **多链支持**
5. **批量支付**

---

## 🔧 当前MVP解决方案

### 支付链接 (临时方案)

```python
def create_payment_link(payment_id: str, amount: float) -> str:
    """手动构建支付链接"""
    base_url = "https://wallet.fluxapay.xyz/pay"
    return f"{base_url}/{payment_id}?amount={amount}&token=USDC"
```

### Webhook (临时方案)

```python
# 使用轮询替代webhook
async def wait_for_payment(payment_id: str, timeout: int = 300):
    """轮询检查支付状态"""
    for _ in range(timeout):
        status = await fluxa.get_payment_status(payment_id)
        if status == "completed":
            return True
        await asyncio.sleep(1)
    return False
```

---

## 📈 长期建议

### 1. 完善Webhook体系
- 支付成功/失败
- Mandate签名状态
- 提现状态

### 2. 开发者工具
- 支付链接SDK
- 前端支付组件
- 后端集成库

### 3. 监控与日志
- 支付成功率
- 失败原因分析
- 资金流向追踪

---

## 🎉 结论

**当前FluxA能力已足够实现MVP核心功能**:
- ✅ 支付: x402协议
- ✅ 验证: Mandate查询
- ✅ 收款: Agent接收

**待补充但非阻塞**:
- Webhook (可轮询替代)
- 支付链接 (可手动构建)
- 退款 (可人工处理)

**建议FluxA优先完善**:
1. Webhook通知 (P0)
2. 支付链接生成 (P1)
3. 退款API (P1)

---

*文档生成: 2026-02-12*
