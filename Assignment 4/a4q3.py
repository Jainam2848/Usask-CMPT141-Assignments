def is_prime(N):
    """
    Determines whether a given positive integer is prime or not
    input: N, any positive integer.
    returns: True if N is prime, False otherwise.
    """
    # special cases:
    if N == 1:
        return False

    # the biggest divisor we're going to try
    divisor = N // 2
    while divisor > 1:
        if N % divisor == 0:
            # we found a number that is a factor of N            
            return False
        divisor = divisor - 1
        
    return True

dic = {}
#print(is_prime(1))
def read(file_name):
    """
    parameter :The function will only take the name of file
    Function will "open the file and read the values" and will call is_prime() function to check if the number is prime,
    return: updated key,value pairs for the dictionary
    
       
    """
    file = open(file_name, 'r')
    
    for i in file.readlines():
        num = int(i.rstrip("\n"))
        results= is_prime(num)
        
        dic.update({num:results})
    return dic
    #print(dic)
    file.close()

print(read("a4q3.txt"))
    