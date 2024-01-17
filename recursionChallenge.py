#recusion challenge :: find factorial of any number then add it with token a2c4dtyx then replace every 3rd
#charecter with X

def changemixToken(mixstr):
    newstr = ""
    i = 0
    while(i<len(mixstr)):
        if(i+1)%3 == 0:
            newstr = newstr + 'X'
        else:
            newstr = newstr + mixstr[i]
        i = i+1
    return newstr

def tokenizeNum(res):
    token = "a2c4dtyx"
    mixtoken = str(res) + token
    return mixtoken

def numFactorial(num):
    # base case
    if num == 1 or num < 0:
        return 1
    return num * numFactorial(num - 1)

res = numFactorial(5)
mix_token = tokenizeNum(res)
print("original mix string: "+mix_token+"\n")
print("changed mix tokwn:  "+ changemixToken(mix_token))
