def dequy(data):
    ids = []
    for item in data:
        ids.append(item['id'])
        if 'value' in item and isinstance(item['value'], list):
            ids.extend(dequy(item['value']))
    return ids

lstDemo = [
    {"id": 1, "value": [{"id": 2, "value": [{"id": 3, "value": [{"id": 4, "value": []}]}]}]},
    {"id": 5, "value": []}
]

result =dequy(lstDemo)
print(result)
