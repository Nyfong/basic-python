''' 
work with range
'''


# start from B and then index start from 10
list_ach = ['A', 'B', 'C', 'D', 'E'] 

# slice from index 2 to 5 (so 'C', 'D', 'E')
for i, ach in enumerate(list_ach[2:5], start=10):
    print(f"index:{i} -> value :{ach}")
