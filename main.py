import json

def main(context):
    body = json.loads(context.req.body)

    # Get a and b
    a = body.get("a")
    b = body.get("b")

    # Validate input
    if a is None or b is None:
        return context.res.json(
            {"error": "Please provide both a and b"},
            status=400
        )

    # Calculate a + b
    result = a + b

    # Return result
    return context.res.json({
        "a": a,
        "b": b,
        "result": result
    })