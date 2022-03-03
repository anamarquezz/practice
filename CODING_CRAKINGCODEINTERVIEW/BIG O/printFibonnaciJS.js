function allFib(n) {
     memo = new Array[n + 1];
    for (let i= 0; i < n; i++) {
    System.out.println(i + ": "+ fib(i, memo));
    }
    }
function fib(n, memo) {
    if (n <= 0) return 0;
     else if (n == 1) return 1;
     else if (memo[n] > 0) return memo[n];
    
     memo[n] = fib(n - 1, memo)+ fib(n - 2, memo);
     return memo[n];
}

allFib(100)