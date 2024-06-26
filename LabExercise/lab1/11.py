#WAP to find square root of all numbers in a list using map tool.
import math
def sqroot(num):
    return math.sqrt(num)
nums = [16,25,9,64]
square_root=list(map(sqroot,nums))

print("original numbers:",nums)
print("Square roots:",square_root)
