import json

python_obj = {
    "име": "Иван",
    "възраст": 25,
    "град": "София",
    "интереси": ["програмиране", "музика", "пътувания"]
}

json_data = json.dumps(python_obj, ensure_ascii=False)

print(json_data)




