# Implement your function below.
def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    key = list1[0]
    key_loc = -1
    for i in range(len(list2)):
        if list2[i] == key:
            key_loc = i
            break
    print()
    if key_loc == -1:
        return False
    for i in range(len(list1)):
        j = (key_loc + i) % len(list1)
        if list1[i] != list2[j]:
            return False
    return True

list1 = [1, 2, 3, 4, 5, 6, 7]
list2b = [4, 5, 6, 7, 1, 2, 3]
print(is_rotation(list1, list2b))

