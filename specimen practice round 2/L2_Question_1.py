#L2 Question 1
numbers=input()
integer = list(map(int,numbers.split()))
for i in integer:
  
   if 13 in integer:
    position = integer(13)
    new_list = integer.pop(position)
    new_new_list = integer.pop(position)
    total = sum(new_new_list)
    print(total)
else:
  total = sum(integer)
  print(total)
