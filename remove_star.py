# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".


def starRemoval(s):
    i = 0
    newstr = []
    while(i<len(s)):
        if s[i] == '*':
            if i > 0:
                newstr.pop()
            i += 1
        else:
            newstr.append(s[i])
            i += 1
    finalstr = ''.join(newstr)
    print(finalstr)

s = "abc***"
starRemoval(s)