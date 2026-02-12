import json
import time

def handler(request):
    data = json.loads(request.get('body', '{}'))
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "success": True,
            "data": {
                "payment_id": f"gacha_{int(time.time())}",
                "amount": "10000",
                "currency": "USDC",
                "description": "扭蛋机 - 一次惊喜"
            }
        })
    }
