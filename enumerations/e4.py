list = ['A', 'B', 'C', 'D', 'E']
# num = 0 
# for i in list:
#     print(f'index={num} value={i}')
#     num +=1

for index, element in enumerate(list, start=100):
    print(f'id={index} student_name={element}')