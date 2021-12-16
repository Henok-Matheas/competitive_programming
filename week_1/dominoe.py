
# inpt = input()
# inpt= inpt.split()

# def dominoe( x , y):
#     x,y= int(x), int(y)
#     z = x * y // 2
#     return z


# print(dominoe(inpt[0],inpt[1]))


# def isPalindrome(x):
#         x = str(x)
#         for i in range(len(x)):
#             if x[i] != x[-(i+1)]:
#                 return False
#         return True

# while(True):
#     print(isPalindrome(int(input())))


def romanToInt(s):
    inti=0
    dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if len(s)<2:
        return dict(s)

    for i in range(len(s)-1):
        x=i+1
        if dict[s[i]]<dict[s[i]]:
            inti-=dict[s[i]]
        else:
            inti+=dict[s[i]]
        
    return (inti+dict[s[-1]])

while(True):
    print(romanToInt(input()))