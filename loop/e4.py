#difine array

#fruits = ["banana","apple","orage"]

# for el in fruits:
#     print("element: ", el )


dict_list = [
        {
            "name" : "a1",
            "age" : "a2"
        },
        {
            "name" : "a11",
            "age" : "a21"
        }
        ,{
            "name" : "a12",
            "age" : "a22"
        }
]

for el in dict_list:
    
    name, age = el["name"], el["age"]
    print("name: ", name, " age: ", age)
    
