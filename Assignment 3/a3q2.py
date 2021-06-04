# NAME :- SHAH JAINAM DINESHKUMAR
# NSID :- AYQ754
# STUDENT NUMBER :- 11321534
# INSTRUCTOR'S NAME :- Nisha Puthiyedth
# COURSE :- CMPT 141


import math as m

#initial mass
initial_m = int(input("Enter initial mass (in grams) :"))

while initial_m <= 0:
    initial_m = int(input("Error! Kindly input positive number :"))

#half life
h = float(input("Enter half life of the material :"))

while h <= 0:
    h = float(input("Kindly enter positive half life of the material :"))

t = 0

#remaining mass of material
remaining_m = initial_m * (0.5)**(t / h)

while remaining_m > (1 / 100) * initial_m:

    remaining_m = initial_m * (0.5)**(t / h)
    print("After ", t, "days there are", remaining_m, " grams remaining")

    t += 1
