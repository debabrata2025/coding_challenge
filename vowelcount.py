#vowel count
def vowelCount(str1):
    s1 = list(str1)
    count = 0
    for char in s1:
        if(char == 'a' or char == 'A' or char == 'e' or
                char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U'):
            count += 1
    print(count)
str1 = "trinanjan"
vowelCount(str1)

# str1 = "trinanjan"
# vowel = "aeiouAEIOU"
#
# count = sum(str1.count(char)for char in vowel)
# print(count)