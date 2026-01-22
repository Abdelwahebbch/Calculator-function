import json


def main(context):
    if (context.req.method == 'GET'): 
        return json.decoder({
            "Name":"Abdelwaheb"
        })