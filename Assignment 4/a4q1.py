# NAME :- SHAH JAINAM DINESHKUMAR
# NSID :- AYQ754
# STUDENT NUMBER :- 11321534
# INSTRUCTOR'S NAME :- Nisha Puthiyedth
# COURSE :- CMPT 141



populationsSK = [ [' Pelican Narrows ', 2703] ,['Saskatoon' , 222035] ,['Moose Jaw' , 33617] ,['La Ronge' , 5905] ]
citiesSK = []
"""
for x in populationsSK :
    if x [1] >= 10000:
        citiesSK.append(x)
print(citiesSK)

"""
#part a=============================================================================================

citiesSK = [x for x in populationsSK if x[1]>=10000]
print("Cities with population more than or equal to 10,000 are :")
print(citiesSK)
print()

#part b============================================================================================

print("Cities with population less than 40,000 are :")
towns  = [i for i in populationsSK if i[1]<40000]
print(towns)
print()

#part C=============================================================================================

names_of_cities = [a[0] for a in populationsSK]
print("The names of cities/towns are :")
print(names_of_cities)
print()

#part D==============================================================================================

len_names = [z[0] for z in populationsSK if  len(z[0]) >8]
print("The  list of all the towns and cities whose names are more than 8 characters is: ")
print(len_names)











