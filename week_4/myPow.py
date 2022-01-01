
x = "1" + "0" *(99999)
print(x)
# class Solution:
#     def pow(self, x, n):
#         if n == 1:
#             return x
#         val = x * x
#         rem = x if n % 2 == 1 else 1
#         return self.myPow(val, n // 2) * rem
    
#     def myPow(self, x: float, n: int) -> float:
#         if x == 0 or x == 1:
#             return x
#         elif n < 0:
#             return 1 / (self.pow(x, abs(n)))
#         elif n > 0:
#             return self.pow(x, n)
#         else:
#             return 1
        
        
                