def arr(array):
    # TODO Concept Here.
    finalList = []

    for i in range(len(array)):
        count = 0
        for j in range(i, len(array)):
            if array[i] < array[j]:
                count += 1
        finalList.append(count)

    print(finalList)


if __name__ == "__main__":
    inputArr = [1, 2, 3, 5, 1, 3, 4]
    arr(inputArr)
