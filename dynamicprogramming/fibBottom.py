def fibBottom(n):
    bottomUp = [None] * (n + 1)
    if n == 1 or n == 2:
        return 1
    bottomUp[1] = 1
    bottomUp[2] = 1
    for i in range(3, n + 1):
        bottomUp[i] = bottomUp[i - 1] + bottomUp[i - 2]
    return bottomUp[n]


if __name__ == "__main__":
    n = 10000
    print(fibBottom(n))
