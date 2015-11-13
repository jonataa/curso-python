def fib(n, S=[]): 
    if n in (1, 2):
        return 1
    return fib(n-1) + fib(n-2) 
print (fib(7))
#fib(5) = 1 1 2 3 5 8 13 21
