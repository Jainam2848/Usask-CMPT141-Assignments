# NAME :- SHAH JAINAM DINESHKUMAR
# NSID :- AYQ754
# STUDENT NUMBER :- 11321534
# INSTRUCTOR'S NAME :- Nisha Puthiyedth
# COURSE :- CMPT 141

encoded_string = input("Enter the encoded string :")
location = int(input("Enter the location of the number in the encoded string :"))

string_before = encoded_string[0: location - 1]
string_after = encoded_string[location:]
k = int(encoded_string[location - 1])

repeat_substring_before_integer = string_before * k

# concatenation
string = repeat_substring_before_integer + string_after

# reverse
decoded_string = string[-1::-1]
# alternately, [string[len(string-1)::-1]], here -1 is decrement from end of string

print("Decoded string : ", decoded_string)

# key character
n = int(len(decoded_string) // 2)

key = decoded_string[n]
print("The Key character of the decoded string is :", key)
