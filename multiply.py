def multiply(f1,f2):
    if f2 == 1:
        return f1
    else:
        return multiply(f1,f2-1) + f1

print(multiply(7,4))