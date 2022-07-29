def fib(n, mem):
    if mem[n] != None:
        return mem[n]

    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1, mem) + fib(n - 2, mem)
    mem[n] = result
    return result


if __name__ == "__main__":
    n = 1000
    mem = [None] * (n + 1)
    print(fib(n, mem))
