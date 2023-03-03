#L1 Question 2
word = input()
letters = len(word)
guess = int(input())
if letters == guess:
  print('MATCH')
elif letters > guess:
  print('MORE')
else:
  print('FEWER')
