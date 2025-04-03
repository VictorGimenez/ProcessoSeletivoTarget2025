import json

with open("dados.json") as json_data:
    file = json.loads(json_data)
    json_data.close()
    print(file)