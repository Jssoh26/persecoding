#L2 Question 1
numbers=input()
integer = list(map(int,numbers.split()))
if 13 in integer:
  position = integer.index(13)  
  numbers_for_substraction = integer[position] + integer[position+1]
  total_int=sum(integer)
  total= total_int - numbers_for_substraction
  print(total)
else:
  total = sum(integer)
  print(total)
