def checkTrue(string):
    mid = len(string) // 2

    leftString = string[:mid]
    rightString = string[mid + 1:]

    leftSum = 0
    rightSum = 0
    for i in leftString:
        leftSum += int(i)
    for i in rightString:
        rightSum += int(i)

    if leftSum == rightSum:
        return True
    else:
        return False


if __name__ == "__main__":
    string = "44023"
    print(checkTrue(string))
