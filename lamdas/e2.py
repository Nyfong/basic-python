#simple lamdas


list_numbers = [1, 2, 3, 4, 5]

#discount
#------------- function-------iteration
discount = list(map(lambda x : x * 0.9, list_numbers)) # map spacific function and iterable then convert to list reable

#conver map to list for readable
print(discount)  

