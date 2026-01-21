import json

def main(context):
    return context.res.json({
        "message": "Hello from Appwrite Python Function 🚀",
        "method": context.req.method,
        "body": context.req.body
    })
