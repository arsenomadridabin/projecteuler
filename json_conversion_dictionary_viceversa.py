import json
dictionary={
    "name":"Abin",
    "Surname":"Shakya",
    "age":"15",
    "education":{
        "school":"AVM",
        "college":"St.xavier's",
        "University":"IOE,Pulchowk"
    }
}
json_data=json.dumps(dictionary)
dictionary2=json.loads(json_data)
print(dictionary2)
