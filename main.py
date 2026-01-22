import json


def main(context):
    try:
        # Read body safely
        body_raw = context.req.body or "{}"
        body = json.loads(body_raw)

        a = body.get("a")
        b = body.get("b")

        # Validate input
        if a is None or b is None:
            return context.res.json(
                {"error": "Please provide both a and b"},
                status=400
            )

        # Convert to numbers (VERY IMPORTANT)
        a = float(a)
        b = float(b)

        result = a + b

        return context.res.json({
            "a": a,
            "b": b,
            "result": result
        })

    except Exception as e:
        # Always return error details for debugging
        return context.res.json(
            {"error": str(e)},
            status=500
        )