# str -> h3ello9-9 total_no 9+9+3 = 21 total_letter = 6, 21/6 ->3.5~4
# one number*1* -> 0 as there is no number with first string
def stringChallenge(str1):
    sum = 0
    count_letter = 0
    for char in str1:
        if char.isdigit():
            sum += int(char)
        else:
            if char == ' ':
                continue
            else:
               count_letter += 1
    res = round(sum/count_letter)
    print(res)

str1 = "one number*1*"
stringChallenge(str1)

