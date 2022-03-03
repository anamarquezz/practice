def allFib(n):
    memo = [1]
    for i in range(n):
        print(i , ":" , fib(i, memo));

def fib(n, memo):
    print('n', n)  
    print('memo', memo)  
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] >= 0:
        return memo[n]

    memo[n] = fib(n -1, memo) + fib(n - 2, memo)
    print(memo)
    return memo[n]

n = 10
allFib(n)