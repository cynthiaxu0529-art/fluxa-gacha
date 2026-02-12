import json

def handler(request):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "success": True,
            "data": {
                "status": "ready",
                "agent_id": "7a123ed9-1517-4405-bafb-708b9aeb0577"
            }
        })
    }
