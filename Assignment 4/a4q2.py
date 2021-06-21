# NAME :- SHAH JAINAM DINESHKUMAR
# NSID :- AYQ754
# STUDENT NUMBER :- 11321534
# INSTRUCTOR'S NAME :- Nisha Puthiyedth
# COURSE :- CMPT 141

import numpy as np

# opening file
a = open("a4q2.txt", 'r')

# creating a empty list and declaring variables
lst = []
x = 0
o = 0

# iterating each line of file and removing newline char
B = np.loadtxt("a4q2.txt", 'r')
for line in a.readlines():
    l = [x for x in line.split()]
    lst.append(l)
    a.close()
print(B)
# converting lst to array
board = np.array(lst)
print(board)
print()

# counting number of x and 0 using nested loops
for i in board:
    for j in i:
        if j == "x":
            x += 1
        if j == "o":
            o += 1

# checking if game is legal or not
print("x = ", x)
print("o = ", o)
if x == o or x - o == 1:
    print("Game is legal")
else:
    # x can be greater than o by 1.. bcoz the x will play the move first
    if o + 1 > x:
        print("There are too many x")
        print("Game is illegal")

    elif o > x:
        print("There are too many o")
        print("Game is illegal")
