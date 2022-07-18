def array_rotation(arr, k, n):
    # TODO Code here.
    idx = n - (k % n)
    for i in range(idx, n):
        print(arr[i], end=' ')
    for i in range(0, idx):
        print(arr[i], end=' ')


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 3
    array_rotation(arr, k, len(arr))
