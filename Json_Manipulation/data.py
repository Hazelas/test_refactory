import json

with open('Refactory_test/Json_Manipulation/mydata.json','r') as f:
    json_object = json.loads(f.read())

print("01. Item in the meeting room: ")
print(json_object['inventory'][0]['name'])
print(json_object['inventory'][1]['name'])
print("______________________")

print("02. All electronic devices: ")
print(json_object['inventory'][2]['name'])
print(json_object['inventory'][3]['name'])
print("______________________")

print("03. All furniture: ")
print(json_object['inventory'][0]['name'])
print(json_object['inventory'][1]['name'])
print("______________________")

print("04. All item purchase on 16 January 2020: ")
print("______________________")

print("05. All item with brown collor: ")
print(json_object['inventory'][0]['name'])
print(json_object['inventory'][1]['name'])
print("______________________")