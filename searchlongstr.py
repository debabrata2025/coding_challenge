# str = abbbccccccccc -> return long str -> ccccccccc

def myFun(str1):
    my_counter = {}
    for letter in str1:
        if letter in my_counter:
            my_counter[letter] += 1
        else:
            my_counter[letter] = 1

    print(max(my_counter, key=my_counter.get)*my_counter[max(my_counter, key=my_counter.get)])

myFun("aabbbcccccc")