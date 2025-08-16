#lamda and functions

add = lambda a, b: a + b
print(f"calling anonymous function using lambda: {add(2, 3)}")  # 5

def add_func(a, b):
    return a + b
add_func_result = add_func(2, 3)
print( f"this is result of call function {add_func_result}" )  # 5
