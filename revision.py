# def is_palindrome(s):
#     res = ""
#     org = s
#     for i in range(len(s)-1,-1,-1):
#         res += s[i]
#     return res== org
# print(is_palindrome("madam"))
# print(is_palindrome("hello"))
# print(is_palindrome("a"))
# print(is_palindrome(""))

# def count_vowels(s):
#     vow = "aeiou"
#     count = 0
#     s = s.lower()
#     for char in s:
#         if char in vow:
#             count+=1
#     return count
# print(count_vowels("hello)") 
# print(count_vowels("APPLE)") 
# print(count_vowels("xyz)") 
# print(count_vowels("aEiOu)")


# def count_words(s):
#     return len(s.split())
# print(count_words("hello world")) 
# print(count_words("I love Python")) 
# print(count_words("word")) 
# print(count_words(""))

def first_unique(s):
    count = {}
    for char in s:
        count[char] =count.get(char,0)+1
    for char in s:
        if count[char] ==1
        return char
    return None

print(first_unique("aabbcdd")) 
print(first_unique("hello")) 
print(first_unique("aabbcc"))  
print(first_unique("abcd")) 