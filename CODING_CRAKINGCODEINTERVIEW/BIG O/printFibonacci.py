def allFib(n):
    memo = [] 
    for i in range(n):
        print(i , ":" , fib(i, memo));

def fib(n, memo):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif memo >= 0:
        return memo[n]

    memo[n] = fib(n -1, memo) + fib(n - 2, memo)
    print('memo',memo)
    return memo[n]

n = 10
allFib(n)