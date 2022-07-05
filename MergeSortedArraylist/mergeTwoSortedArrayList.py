arr1 = [3, 5, 6, 10]
arr2 = [1, 2, 7, 8, 11, 12]
i, j = 0, 0
len1 = len(arr1)
len2 = len(arr2)
newList = []
while i<len1 and j < len2:
    if arr1[i] < arr2[j]:
        newList.append(arr1[i])
        i+=1
    else:
        newList.append(arr2[j])
        j+=1
print(newList)
