# NAME :- SHAH JAINAM DINESHKUMAR
# NSID :- AYQ754
# STUDENT NUMBER :- 11321534
# INSTRUCTOR'S NAME :- Nisha Puthiyedth
# COURSE :- CMPT 141

countries = input("Enter the country you want to go :")

expand_list = input("Would you like to enter any other country(y/n) ?:")

Bucket_list = [countries]

#loop will allow user to enter multiple countries in bucket list 
while True:
    if expand_list == "y":
        expand_list = input("Which new country you want to add to the list ? : ")
        Bucket_list.append(expand_list)
        expand_list = input("Would you like to enter any other country(y/n) ?:")
    if expand_list=="n":
        break

print("Long term Bucket list is ", Bucket_list)
gap_year = []

gap_year_country = input("Which country from Bucket list you want to add in gap year list ? :")

gap_year.append(gap_year_country)
Bucket_list.remove(gap_year_country)

expand_gap_year = input("Would you like to add more countries to your gap year list ?")

#loop will allow user to enter multiple countries in gap year list 

while True:
    if expand_gap_year=="y":
        gap_year_country = input("Which another country from Bucket list you want to add in gap year list ? :")
        gap_year.append(gap_year_country)
        Bucket_list.remove(gap_year_country)
        expand_gap_year = input("Would you like to add more countries to your gap year list ?")
        if expand_gap_year=="n":
            break
    if expand_gap_year=="n":
        break

print("Countries visiting in gap year :",gap_year)
print("Countries remaining in Bucket List is/are :" , Bucket_list)
