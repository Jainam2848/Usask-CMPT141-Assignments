# NAME :- SHAH JAINAM DINESHKUMAR
# NSID :- AYQ754
# STUDENT NUMBER :- 11321534
# INSTRUCTOR'S NAME :- Nisha Puthiyedth
# COURSE :- CMPT 141

# The following is one example of a black-box test for the recentTrend function

from testing_blackbox_recentTrend import recentTrend
# i.e. the recentTrend() function is sitting in a file called "testing_blackbox_recentTrend.py"

test = []
expected = None
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)

# test a list with only 1 element
test = [42]
expected = 42
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)
    
# test a list shorter than 20 elements with the mode at beginning and end
###To DO: add your test case here
    
test = [1,2,3,4,1,5,9,7,16,1]
expected = 1
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)   
    

# test a list of exactly 20 elements, with the mode at beginning and end
###TO DO: add your test case here

test = [20,19,18,17,16,15,14,45,65,89,78,54,12,65,98,45,78,12,5,20]
expected = 20
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)
   
# test a list of more than 20 elements such that mode would change if the extras were included
###TO DO: add your test case here

test = [20,20,19,20,17,16,15,14,45,65,89,78,54,12,65,98,45,78,12,5,20,19,18,100,4]
expected = 45
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)
print()

# test a list with all ties for the mode, with largest value in the middle    
###TO DO: add your test case here
test = [1,1,1,1,2,2,2,2,5,5,5,5,3,3,3,3,4,4,4,4]
expected = 5
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)


print()

# test a list with all ties for the mode, with largest value at the start    
###TO DO: add your test case here
    
test = [5,5,5,5,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
expected = 5
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)
