# code.tamil

def commonElements(arr1, arr2):
    # TODO Code here.
    p1 = 0
    p2 = 0
    newList = []
    while p1 < len(arr1) and p2 < len(arr2):

        if arr1[p1] == arr2[p2]:
            newList.append(arr1[p1])
            p1 +=1
            p2 +=1
        elif arr1[p1] > arr1[p2]:
            p2 +=1
        else:
            p1 +=1
                
    return newList

if __name__ == "__main__":
    
    arr1 = [1, 3, 4, 6, 7, 9]
    arr2 = [1, 2, 4, 5, 9, 10]
    
    print(commonElements(arr1, arr2))
