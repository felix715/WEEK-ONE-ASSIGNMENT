def is_prime(n):
    if (n<2):
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True
num = int(input("Enter the number: "))
if is_prime(num):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")