def multiply(f1,f2):
    if f2 == 1:
        return f1
    else:
        return multiply(f1,f2-1) + f1

#print(multiply(7,3))
#Write a **recursive** function named multiply that takes two positive integers as
# parameters and returns the product of those two numbers (the result from multiplying
# them together).  Your program should not use multiplication - it should find the
# result by using addition.  You CANNOT use loops.


