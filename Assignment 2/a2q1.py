# NAME :- SHAH JAINAM DINESHKUMAR
# NSID :- AYQ754
# STUDENT NUMBER :- 11321534
# INSTRUCTOR'S NAME :- Nisha Puthiyedth
# COURSE :- CMPT 141


email = input("Enter your email address :")

username = email[0: email.find('@')]
domain = email[email.find('@') + 1: email.find('.',email.find("@"))]


print("Username :", username)
print("Domain :", domain)
