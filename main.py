def main(context):
    name = context.req.query.get("name", "World")

    return context.res.json({
        "message": f"Hello {name}!",
        "method": context.req.method,
        "headers": context.req.headers
    })
