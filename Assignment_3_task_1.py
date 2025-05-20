def factorial (n) :
    
    if n <2 :
        return 1
    else :
        return n* (factorial(n-1))
n = int(input("Enter the Number "))

result = factorial(n)
print ("factorial is", result)
factorial(n)
