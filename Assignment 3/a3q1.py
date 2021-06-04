# NAME :- SHAH JAINAM DINESHKUMAR
# NSID :- AYQ754
# STUDENT NUMBER :- 11321534
# INSTRUCTOR'S NAME :- Nisha Puthiyedth
# COURSE :- CMPT 141

import random as r
import string as s

N = input("Enter the First name of student :")
Name = N.capitalize()
random_char = r.choice(s.ascii_uppercase)

print(random_char, "is the random character")

if random_char!=Name[0]:
    print("The student ,", Name, "is not chosen for background research group")
    
if random_char==Name[0]:
    print(Name," is choosen for background research team")


else:
    if Name[0]=="A" or Name[0]=="B" or Name[0]=="C" or Name[0]=="D":
        print(Name, "is assigned to Group One")
        
    elif Name[0]=="E" or Name[0]=="F" or Name[0]=="G" or Name[0]=="H" or Name[0]=="I":
        print(Name, " is assigned to Group Two")
   
    elif Name[0]=="J" or Name[0]=="K" or Name[0]=="L" or Name[0]=="M" or Name[0]=="N" or Name[0]=="O" or Name[0]=="P" or Name[0]=="Q" or Name[0]=="R":
        print(Name ,"is assigned to Group Three")    
    
    else:
        print(Name, "is assigned to group Four")





