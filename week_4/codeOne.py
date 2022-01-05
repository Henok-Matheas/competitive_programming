import math

def recur(n):
    if n == 1 or n == 0:
        return n
    cOne = recur(math.floor(n / 2))
    return str(cOne) + str(n % 2) + str(cOne)

def codeOne(n,l,r):
    return recur(n)[l  - 1: r].count("1")
    
 
inpt = input()
inpt= inpt.split()
inpt = list(map(int, inpt))
print(codeOne(inpt[0], inpt[1], inpt[2]))