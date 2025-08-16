# {key_expr: value_expr for item in iterable if condition}

nums = [1, 2, 3, 4]

square_dicts = {x : x **2 for x in nums }

print(square_dicts) 


# loop element in nums
#and then take each element x and create a key value pair
# where key is x and value is x * 2
