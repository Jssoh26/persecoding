#L2 Question 2
A=1
B=2
C=3
D=4
E=5
F=6
G=7
H=8
I=9
J=10
K=11
L=12
M=13
N=14
O=15
P=16
Q=17
R=18
S=19
T=20
U=21
V=22
W=23
X=24
Y=25
Z=26
words = input()
alphabets = words.split()
smallest_letter = alphabets[0]
greatest_letter = alphabets[0]
for i in alphabets:
  if i < smallest_letter:
    smallest_letter = i
for s in alphabets:
  if s > greatest_letter:
    greatest_letter = s
smallest_number = ord(smallest_letter)
greatest_number = ord(greatest_letter)
number = greatest_number-smallest_number
print(number)
