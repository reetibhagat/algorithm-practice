import json

with open('sample-json-file.json','r') as file:
    json_data = json.load(file)

print(type(json_data))
print(json_data)
for key, value in json_data['Address'].items():
    print( key ,":" ,value)

with open('sample.json','w') as f:
    json.dump(json_data,f)





