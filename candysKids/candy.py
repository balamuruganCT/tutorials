if __name__ == '__main__':
    num_testCases = int(input())
    for i in range(num_testCases):
        numBags, numStudents = input().split()
        candys = list(map(int, input().split()))
        print(f'Case #{i+1}: {sum(candys)%int(numStudents)}')