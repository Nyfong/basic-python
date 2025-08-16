#[expression for item in iterable if condition]

list_numbers = [1, 2, 3, 4, 5]

list_comprehension_discount = [x * 0.9 for x in list_numbers]  # apply discount to each number

print(list_comprehension_discount)  