# code.tamil

def maxSumIncreasingSubarray(A, n):

    # TODO Concept here.
    max_sum = A[0]
    current_sum = A[0]
    for i in range(1, n):
        if A[i-1] <= A[i]:
            current_sum += A[i]
            max_sum = max(max_sum, current_sum)
        else:
            max_sum = max(max_sum, current_sum)
            current_sum = A[i]
    return max(current_sum, max_sum)

if __name__ == "__main__":
    A = [1, 2, 2, 4]
    print(maxSumIncreasingSubarray(A, len(A)))
