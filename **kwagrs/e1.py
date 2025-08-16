# **kwargs → captures keyword arguments as a dict
def my_fun(**kwargs):
    print(kwargs)

key="val"
my_fun(key="val", key2="val2")  # it will print as a dictionary based on the function we return print

#if  my_fun(key, key2="val2")  is error cuz the first argument is not a keyword argument
# the first augument is a value so error will be occur
