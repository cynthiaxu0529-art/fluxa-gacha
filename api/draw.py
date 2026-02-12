import json
import random
import time

PRIZES = [
    {"type": "poem", "name": "藏头诗", "emoji": "📝"},
    {"type": "fortune", "name": "运势", "emoji": "🔮"},
    {"type": "joke", "name": "笑话", "emoji": "😂"},
    {"type": "image_prompt", "name": "Prompt", "emoji": "🎨"},
    {"type": "blessing", "name": "祝福", "emoji": "🧧"},
]

def handler(request):
    prize = random.choice(PRIZES)
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "success": True,
            "data": {
                "status": "success",
                "prize": prize,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }
        })
    }
