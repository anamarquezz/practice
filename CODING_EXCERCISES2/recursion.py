def run(n):
    if n == 0:
        return

    print(n)
    run(n)

n = 3 
run(n)