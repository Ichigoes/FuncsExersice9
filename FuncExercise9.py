def palindrome(*args):
    word = args[0]
    return f"{word} is a palindrome" if word == word[-1::-1] \
        else f"{word} is not a palindrome"


print(palindrome("abcbabbcba", 0))
print(palindrome("peter", 0))