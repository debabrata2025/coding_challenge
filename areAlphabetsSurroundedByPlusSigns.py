#input_str -> +d+=3=+s+ output -> true, input_str -> f++d+ output -> false

def areAlphabetsSurroundedByPlusSigns(str1):
    flag = False
    for i in range(len(str1)):
        if str1[i].isalpha():
            if i == 0 or i == len(str1)-1 or str1[i-1] != '+' or str1[i+1] != '+':
                flag = False
                break
            else:
                flag = True

    return flag


str1 = "+a+b+c+"
print(areAlphabetsSurroundedByPlusSigns(str1))
