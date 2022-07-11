n = 10
tmp = None
for i in range(n):
    if i == 0:
        tmp = str(i)
        print(n*" ", tmp, n*" ")
    else:
        tmp = str(i) + tmp + str(i)
        print(n*" ", tmp, n*" ")
    n = n - 1



