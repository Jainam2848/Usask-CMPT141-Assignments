# NAME :- SHAH JAINAM DINESHKUMAR
# NSID :- AYQ754
# STUDENT NUMBER :- 11321534
# INSTRUCTOR'S NAME :- Nisha Puthiyedth
# COURSE :- CMPT 141

def median3(num1, num2, num3):
    """
    Parameters: num1,num2,num3
    
    The function median3 will calculated and return
    median value of parameters.
    
    Returns: median(central value) of parameters
    
    """    
    if num2 <= num1 <= num3 or num3 <= num1 <= num2:
        return num1
    elif num1 <= num2 <= num3 or num3 <= num2 <= num1:
        return num2
    else:
        return num3
    
################################# T E S T   F O R  M E D I A N   F U N C T I O N ###################################0#

# TEST 1-------------------CHECKING IF STATEMENT
test = (2,1,3)
expected = 2
result = median3(2,1,3)
if result != expected:
    print("Testing median3() with", test, "   Expected:", expected, " Got: ", result)

# TEST 2 ------------------CHECKING IF STATEMENT FOR NEGATIVE NUMBERS
test = (7.0,9,-2.2)
expected = 7.0
result = median3(7,9,-2)
if result != expected:
    print("Testing median3() with", test, "   Expected:", expected, " Got: ", result)
    
# TEST 3 ------------------CHECKING ELSE STATEMENT
test = (2,5,9)
expected = 5
result = median3(2,5,9)
if result != expected:
    print("Testing median3() with", test, "   Expected:", expected, " Got: ", result)

# TEST 4 ------------------CHECKING ELSE STATEMENT FOR NEGATIVE NUMBERS
test = (26.0,25.5,-45)
expected = 25.5
result = median3(26.0,25.5,-45)
if result != expected:
    print("Testing median3() with", test, "   Expected:", expected, " Got: ", result)
    
# TEST 5 ------------------CHECKING ELIF STATEMENT
test = (1034, 102, 900)
expected = 900
result = median3(1034, 102, 900)
if result != expected:
    print("Testing median3() with", test, "   Expected:", expected, " Got: ", result)

# TEST 6 ------------------CHECKING ELIF STATEMENT FOR NEGATIVE NUMBERS
test = (3,-2,1)
expected = 1
result = median3(3,-2,1)
if result != expected:
    print("Testing median3() with", test, "   Expected:", expected, " Got: ", result)

# TEST 7-------------------CHCECKING FOR STRINGS IN INPUT
test = ("A",-2,1)
expected = TypeError
result = median3("A",-2,1)
if result != expected:
    print("Testing median3() with", test, "   Expected:", expected, " Got: ", result)


def majority(num_list):
    
    """
    Parameter : The function will take list of numbers as parameters
    The function will check for number of  positive integers and will return True or false based on condition
    The function will return false for empty list or if string is present in list
    return: The function returns True if at least half of the numbers in the input list are positive
    
    """
    positive = 0
  
    
    if len(num_list)==0:
        return False
    else:
        for i in num_list:
            if  i>0:
                    positive+=1
            
    if positive>=(len(num_list))/2:
        return True
    else:
        return False
    

################################### T E S T  F O R  M A J O R I T Y  F U N C T I O N ##########################"""
# TEST 1
num_list = [3,-2,1]
expected = True
result = majority(num_list)
if result != expected:
    print("Testing majority() with", num_list, "   Expected:", expected, " Got: ", result)

# TEST 2
num_list = [3,-2,1,2,3,4,-2,-4,-24]
expected = True
result = majority(num_list)
if result != expected:
    print("Testing majority() with", num_list, "   Expected:", expected, " Got: ", result)

# TEST 3--------------passing empty list
num_list = []
expected = False
result = majority(num_list)
if result != expected:
    print("Testing majority() with", num_list, "   Expected:", expected, " Got: ", result)

# TEST 4
num_list = [-2,-4,0,0,0,-5]
expected = False
result = majority(num_list)
if result != expected:
    print("Testing majority() with", num_list, "   Expected:", expected, " Got: ", result)

# TEST 5---------------PASSING ONLY NEGATIVE NUMBERS
num_list = [-1,-2,-3,-4,-5]
expected = False
result = majority(num_list)
if result != expected:
    print("Testing majority() with", num_list, "   Expected:", expected, " Got: ", result)

# TEST 6---------------PASSING ZEROS
num_list = [0,0,0,0,0,0,0]
expected = False
result = majority(num_list)
if result != expected:
    print("Testing majority() with", num_list, "   Expected:", expected, " Got: ", result)

# TEST 7---------------PASSING STRINGS   (Fault!!!)

num_list = ["a", 1,2,3]
expected = TypeError
result = majority(num_list)
if result != expected:
    print("Testing majority() with", num_list, "   Expected:", expected, " Got: ", result)