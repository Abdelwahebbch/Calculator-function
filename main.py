import json


def main(context):
    if (context.req.method == 'GET'): 
        return context.res.json({
            "Name":"Abdelwaheb"
        })
    return context.res.send("Aloo Aloo ya migo")