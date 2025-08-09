#loop object

details = [
    {"name":"sokha", "age": 25, "city": "Phnom Penh"},
    {"name":"sokha", "age": 30, "city": "Siem Reap"},
    {"name":"sokha", "age": 28, "city": "Battambang"},
    {"name":"sokha", "age": 22, "city": "Kampot"},
]

#loop through the list of dictionaries
for detail in details:
    print(f"Name: {detail['name']}, Age: {detail['age']}, City: {detail['city']}")