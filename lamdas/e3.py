#lambda

# age = lambda n1 : n1 + 10

# result = age(20)

# print(result)



original_price = [ 10, 20, 30, 40 ]

calcu_price = list(map(lambda param : param - (param * 0.1), original_price))

print(calcu_price)


    