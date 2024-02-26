def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
print (palindrome(
"1414884937242655719669145562427394884141"))