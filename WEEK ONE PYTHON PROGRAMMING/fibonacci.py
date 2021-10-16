# implementation of a fibonacci series(fib function) using a for loop
# def fib(n):
#     a,b,=0,1
#     for i in range(2,n):
#         # next_term=b+a
#         # a=b
#         # b=next_term
#         a,b=b,a+b
#     return b
# print(fib(12))

#TAIL RECURSION METHOD

def fib(n,value=1,a=0):
    if n==0:
        return value
    return fib(n-1,value+a,value)
print(fib(70))
