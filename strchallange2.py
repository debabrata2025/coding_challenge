#input_str -> +d+=3=+s+ output -> true, input_str -> f++d+ output -> false

def stringChallenge(str1):
    for i in range(len(str1)):
        if str1[i].isalpha():
            if i == 0 or i == len(str1)-1 or str1[i-1] != '+' or str1[i+1] != '+':
                return False
            else:
                return True


str1 = "+a++"
print(stringChallenge(str1))