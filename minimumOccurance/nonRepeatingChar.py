# code. tamil
def nr(input_string):
    # TODO Code here
    dict = {}
    for i in input_string:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1

    print(min(dict, key=dict.get))




if __name__ == "__main__":
    inputString = "aabbc"
    nr(inputString)