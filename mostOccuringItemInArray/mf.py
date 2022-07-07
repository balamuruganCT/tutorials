def most_frequent(given_list):
    max_count = -1
    max_item = None
    count = {}
    for i in given_list:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    return max_item


list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
most_frequent(list5)