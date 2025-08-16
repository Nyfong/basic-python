#division

#initailize a variable``
a = 10
try:
    print(a/"a")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed." )
except Exception as e:
    print("Error: Division by zero is not allowed Parent.", e)
finally:
    print("Execution completed.")
    
# This code demonstrates exception handling in Python, specifically for division by zero.