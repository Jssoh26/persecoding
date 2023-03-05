#L2 Question 3
secret_number = int(input())
answer = 50 
lower_answer = 0
higher_answer = 101
number_of_times=[0]
while answer > secret_number:
  answer_before = answer 
  answer = (answer + lower_answer)//2 
  number_of_times.append(1)
  while answer < secret_number:
    lower_answer = answer 
    answer = (answer_before+lower_answer)//2 
    number_of_times.append(1)
while answer < secret_number: #50<71
  answer_before = answer #50
  answer = (answer_before+higher_answer)//2 #75
  number_of_times.append(1)
  while answer > secret_number:
    higher_answer = answer 
    answer = (answer_before + higher_answer)//2 
    number_of_times.append(1)
times_of_input = sum(number_of_times) +1
print(times_of_input)
