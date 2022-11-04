import requests
import json
response = requests.get("https://exo.lgms.nl/?asJson&list=userlevels")


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    file = open("data.json","w")
    file.write(text)

jprint(response.json())
