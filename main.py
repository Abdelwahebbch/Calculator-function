import json


def main(context):
    if (context.req.method == 'GET'): 
        return context.res.json({
            "Name":"Abdelwaheb"
        })