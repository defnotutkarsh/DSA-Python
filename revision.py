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

# def first_unique(s):
#     count = {}
#     for char in s:
#         count[char] = count.get(char,0)+1
#     for char in s :
#         if (count[char] == 1) :
#             return char
  

# print(first_unique("aabbcdd")) 
# print(first_unique("hello")) 
# print(first_unique("aabbcc"))  
# print(first_unique("abcd")) 

# def remove_duplicates(s):
#     res = ""
#     seen = {}
#     for char in s:
#         if(char not in seen):
#             res += char
#             seen[char] = True
#     return res
        
        


# print(remove_duplicates("hello")) 
# print(remove_duplicates("aabbcc")) 
# print(remove_duplicates("abcd"))  
# print(remove_duplicates("mississippi")) 

# def is_anagram(s1, s2):
#     d1 = {}
#     d2 = {}
#     for char in s1:
#         d1[char] = d1.get(char,0)+1
#     for char in s2:
#         d2[char] = d2.get(char,0)+1
#     return (d1==d2)


# print(is_anagram("listen", "silent"))
# print(is_anagram("hello", "world"))
# print(is_anagram("aab", "aba"))
# print(is_anagram("aab", "aaa"))


# def substrings(s):
#     res = []
#     for i in range(len((s))):
#         for j in range ((i+1),len(s)+1)
#     res.append(s[i:j])
#     return res

# print(substrings("abc"))
# print(substrings("ab"))
# print(substrings("a"))


# def compress(s):
#     if not s:
#         return ""
#     count = 1
#     current = s[0]
#     res = ""
#     for i in range(1,len(s)):
#         if(s[i]==current):
#             count+=1
#         elif(s[i] != current):
#             res = res + current + str(count)
#             current =s[i]
#             count = 1
#     return res + current + str(count)
# print(compress("aaabbc"))
# print(compress("aaa"))
# print(compress("abc"))
# print(compress(""))

# def reverse_list(lst):
#     lst1 = []
#     for i in range(len(lst)-1,-1,-1):
#         lst1.append(lst[i])
#     return lst1
# print(reverse_list([1, 2, 3, 4, 5]))       # [5, 4, 3, 2, 1]
# print(reverse_list([10, 20, 30]))           # [30, 20, 10]
# print(reverse_list([7]))                    # [7]
# print(reverse_list([]))                     # []
# print(reverse_list(["a", "b", "c"]))        # ["c", "b", "a"]



# def find_max(lst):
#     if (len(lst) == 0):
#         return None
#     no = lst[0]
#     for i in range(1,len(lst)):
#         if(lst[i]> no):
#             no = lst[i]
#     return no

# print(find_max([3, 7, 2, 9, 1]))        # 9
# print(find_max([10, 20, 30]))            # 30
# print(find_max([-5, -2, -8]))            # -2
# print(find_max([42]))                    # 42
# print(find_max([]))                      # None


# def two_sum(lst, target):
#     seen = {}
#     for i in range(len(lst)):
#         need = target - lst[i]
#         if need in seen :
#             return [seen[need],i]
#         seen[lst[i]] = i
#     return[]
# print(two_sum([2, 7, 11, 15], 9))       # [0, 1]
# print(two_sum([3, 2, 4], 6))            # [1, 2]
# print(two_sum([1, 5, 3, 7], 8))         # [1, 3]
# print(two_sum([10, 20, 30, 40], 50))    # [1, 2]

# def second_largest(lst):
#     first = lst[0]
#     second = None
#     for i in range(len(lst)):
#         if(lst[i]>first):
#             second = first
#             first = lst[i]
#         elif first > lst[i] and (second is None or lst[i] > second):
#             second = lst[i]
#     return second
# print(second_largest([3, 7, 2, 9, 1]))        # 7
# print(second_largest([10, 20, 30]))            # 20
# print(second_largest([5, 5, 5]))               # None
# print(second_largest([1]))                     # None
# print(second_largest([4, 1, 8, 8, 3]))         # 4


# def freq(s):
#     s=s.lower().split()
#     count ={}
#     for word in s:
#         count[word] = count.get(word,0)+1
#     return count
# print(freq("the cat and the dog"))

# def invert(d):
    # for key,values in d.items():
        # key,value = value,key
        # 
# def ana(lst):
#     res = {}
#     for word in lst:
#         key = "".join(sorted(word))
#         if (key in res):
#             res[key].append(word)
#         else:
#             res[key] = [word]
#     return list(res.values())
# print(ana(["eat", "tea", "tan", "ate", "nat", "bat"]))


# def charmap(s1,s2):
#     d={}
#     for i in range (len(s1)):
#         d[s1[i]] = s2[i]
#         return 

