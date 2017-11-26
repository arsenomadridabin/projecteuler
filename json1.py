import json

json_data={"name":"Abin", "age":"22"}
python_object= json.loads(json_data)
print(python_object["name"])

