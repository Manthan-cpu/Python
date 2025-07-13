info={
    "key": "value",
    "name" : "Manthan",
    "age" : 19,
    "marks":[1,12,34,43]

}

print(info)#{'key': 'value', 'name': 'Manthan', 'age': 19, 'marks': [1, 12, 34, 43]}


print(type(info))#<class 'dict'>



#dictionaries are unordered, and mutable
#we can not create duplicate keys


print(info["marks"],info["age"],info["name"])#[1, 12, 34, 43] 19 Manthan




info["age"]=20
print(info["age"])#20




info["surname"]="gupta" 
print(info)#{'key': 'value', 'name': 'Manthan', 'age': 20, 'marks': [1, 12, 34, 43], 'surname': 'gupta'}



null={}
print(null)#{}


#nested dictionary
student={
    "name":"Rahul",
    "subjects" : {
        "phy":99,
        "chem":87,
        "math":97
    }
}
print(student)#{'name': 'Rahul', 'subjects': {'phy': 99, 'chem': 87, 'math': 97}}
print(student["subjects"]["chem"])#87




print(info.keys())#dict_keys(['key', 'name', 'age', 'marks', 'surname'])


print(student.keys())#dict_keys(['name', 'subjects'])


print(student["subjects"].keys())#dict_keys(['phy', 'chem', 'math'])

print(len(student))#2 total no. of key-value pairs
print(student.values())#dict_values(['Rahul', {'phy': 99, 'chem': 87, 'math': 97}])


print(list(student.values()))#['Rahul', {'phy': 99, 'chem': 87, 'math': 97}]

print(student.items())#dict_items([('name', 'Rahul'), ('subjects', {'phy': 99, 'chem': 87, 'math': 97})])


print(student["name"])#Rahul
print(student.get("name"))#Rahul



#print(student["name2"])#error
print(student.get("name2"))#None


(student.update(info))
print(student)#{'name': 'Manthan', 'subjects': {'phy': 99, 'chem': 87, 'math': 97}, 'key': 'value', 'age': 20, 'marks': [1, 12, 34, 43], 'surname': 'gupta'}
