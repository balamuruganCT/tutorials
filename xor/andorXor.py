def xor(arr, n):
    arr.sort()

    if len(arr) < 2:
        return None

    minimum = arr[0] ^ arr[1]
    for i in range(1, n-1):
        c = arr[i] ^ arr[i+1]
        if c < minimum:
            minimum = c
    print(minimum)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    xor(arr, len(arr))