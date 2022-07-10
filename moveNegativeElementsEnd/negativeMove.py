def nMove(A):
    # TODO Code here.
    sortedList = []
    for i in A:
        sorLength = len(sortedList)
        if i < 0:
            sortedList.insert(sorLength, i)
        else:
            sortedList.insert(0, i)
    return sortedList


if __name__ == "__main__":
    arr = [1, -1, -3, -2, 7, 5, 11, 6]
    print(nMove(arr))
