# NAME :- SHAH JAINAM DINESHKUMAR
# NSID :- AYQ754
# STUDENT NUMBER :- 11321534
# INSTRUCTOR'S NAME :- Nisha Puthiyedth
# COURSE :- CMPT 141

def spaceTime(d):
    """
    Parameter : Distance travelled by the object
    The program will calculate the time required by object using recursion.
    return : The functions will return the time taken by the object to cover the distance d

    """
    if d<=1:
        return 1
    else:
        t = 1+spaceTime(d/2)
        return t
print("Lets go team!")
print(spaceTime(37), "minutes to travel 37 meters to the nearest Poke - Stop")
print(spaceTime(40075000.0),"minutes to travel 40075000.0 meters for a round - trip around the earth")
print(spaceTime(149000000000.0),"minutes to travel 149000000000.0 meters from our earth to our sun")
print(spaceTime(4e16)," minutes to travel 4e+16 meters from our sun to the nearest star")
print(spaceTime(8.8e26)," minutes to travel 4 e +16 meters from our sun to the nearest star")

print("Those were amazing trips!!! ")

