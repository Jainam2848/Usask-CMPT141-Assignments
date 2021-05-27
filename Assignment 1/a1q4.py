# NAME :- SHAH JAINAM DINESHKUMAR
# NSID :- AYQ754
# STUDENT NUMBER :- 11321534
# INSTRUCTOR'S NAME :- Nisha Puthiyedth
# COURSE :- CMPT 141

weight = float(input("Enter your weight in kg :"))
height = float(input("Eter your height in meters  :"))


def bmi(weight, height):
    """ This function will calculate the body's bmi
        This function will take weight and height as parameters
        and will return the value of bmi with respect to input taken
    """
    b = weight / (height)**2
    return b


print("Your BMI is : ",bmi(weight, height), "kg/m^2")
