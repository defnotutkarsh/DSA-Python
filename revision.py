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





# def rev(s):
#     res = ""
#     for i in range(len(s)-1,-1,-1):
#         res = res + s[i]
#     return res
# print(rev("utk"))

# def vow(s):
#     count = 0
#     vowel = "aeiou"
#     for char in s:
#         if char in vowel:
#             count+=1
#     return count
# print(vow("utkarsh"))


# def first_unique(s):
#     count = {}
#     for char in s:
#         count[char] = count.get(char,0)+1
#     for char in s:
#         if (count[char]==1):
#             return char
#     return None
# first_unique("aabbcdd") 
# first_unique("hello")  
# first_unique("aabbcc")  
# first_unique("abcd") 


# def is_anagram(s1,s2):
#     d1 = {}
#     d2 = {}
#     for char in s1:
#         d1[char] = d1.get(char,0)+1
#     for char in s2:
#         d2[char] = d2.get(char,0)+1
#     return (d1==d2)

# print(is_anagram("listen", "silent") )
# print(is_anagram("hello", "world") )
# print(is_anagram("aab", "aba") )
# print(is_anagram("aab", "aaa") )



# def compress(s):
#     count = 1
#     res = ""
#     current = s[0]
#     for i in range(1,len(s)):
#         if(s[i]==current):
#             count += 1
#         elif(s[i] != current):
#             res = res +current+ str(count)
#             count =1
#             current = s[i]
            
#     return res +current+ str(count)
# print(compress("aaabbbcc"))


# def rev(lst):
#     res = []
#     for i in range(len(lst)-1,-1,-1):
#         res.append(lst[i])
#     return res
# print(rev([1, 2, 3, 4, 5]))       # [5, 4, 3, 2, 1]
# print(rev([10, 20, 30]))           # [30, 20, 10]
# print(rev([7]))                    # [7]
# print(rev([]))                     # []
# print(rev(["a", "b", "c"]))        # ["c", "b", "a"]

# def find_max(lst):
#     if(len(lst)== 0):
#         return []
    
#     current = lst[0]
#     for i in range(len(lst)):
#         if lst[i] > current :
#             current = lst[i]
#     return current
# print(find_max([3, 7, 2, 9, 1]))        # 9
# print(find_max([10, 20, 30]))            # 30
# print(find_max([-5, -2, -8]))            # -2
# print(find_max([42]))                    # 42
# print(find_max([]))                      # None



# def two_sum(lst,target):
    
#     seen = {}
#     for i in range(len(lst)):
#         need = target - lst[i]
#         if need in seen :
#             return [seen[need],i]
#         else:
#             seen[lst[i]] = i
# print(two_sum([2, 7, 11, 15], 9))       # [0, 1]
# print(two_sum([3, 2, 4], 6))            # [1, 2]
# print(two_sum([1, 5, 3, 7], 8))         # [1, 3]
# print(two_sum([10, 20, 30, 40], 50))    # [1, 2]



# def freq(s):
#     count = {}
#     s=s.split()
#     for word in s :
#         count[word] = count.get(word,0)+1
#     return count
# print(freq("the cat and the dog"))

# def invert(d):
#     res = {}
#     for key,value in d.items():
#         res[value]= key
#     return res
# print(invert({"a": 1, "b": 2, "c": 3}))


# def ana(lst):
#     res ={}
#     for word in lst:
#         key = "".join(sorted(word))
#         if key in res:
#             res[key].append(word)
#         else:
#             res[key] = [word]
#     return list(res.values())


# def charmap(s1,s2):
#     d= {}
#     for i in range(len(s1)):
#         d[s1[i]] = s2[i]
#     return d
# print(charmap("abc", "xyz"))


# def invert(d):
#     res = {}
#     for key,value in d.items():
#         res[value].append(key)
    



# def is_palindrome(s):
#     org = s
#     res = ""
#     for i in range(len(s)-1,-1,-1):
#         res = res + s[i]
#     return res == org
# print(is_palindrome("racecar")      )
# print(is_palindrome("hello")        )
# print(is_palindrome("")              )
# print(is_palindrome("a")             )
# print(is_palindrome("ab")            )
# print(is_palindrome("abba")          )
# print(is_palindrome("abcba")         )
# print(is_palindrome("Racecar")       )


# def count_vowels(s):
#     vowels = "aeiou"
#     count = 0
#     s= s.lower()
#     for char in s:
#         if char in vowels:
#             count+=1
#     return count
# print(count_vowels("hello"))        # 2
# print(count_vowels(""))             # 0
# print(count_vowels("bcdfg"))        # 0
# print(count_vowels("aeiou"))        # 5
# print(count_vowels("AEIOU"))        # 5
# print(count_vowels("HeLLo WoRLd")) # 3
# print(count_vowels("aaa"))          # 3


# def first_non_repeating(s):
#     count = {}
#     for char in s:
#         count[char] = count.get(char,0)+1
#     for char in s:
#         if (count[char] ==1):
#             return char

# print(first_non_repeating("aabbc"))    # c
# print(first_non_repeating("aabb"))     # None
# print(first_non_repeating(""))         # None
# print(first_non_repeating("a"))        # a
# print(first_non_repeating("abcabc"))   # None
# print(first_non_repeating("aabcbd"))   # c
# print(first_non_repeating("xxyz"))     # y

# def is_anagram(s1, s2):
#     d1 = {}
#     d2 = {}
#     for char in s1:
#         d1[char] = d1.get(char,0)+1
#     for char in s2:
#         d2[char] = d2.get(char,0)+1
#     return d1==d2
# print(is_anagram("listen", "silent"))  # True
# print(is_anagram("hello", "world"))    # False
# print(is_anagram("", ""))              # True
# print(is_anagram("a", "a"))            # True
# print(is_anagram("ab", "ba"))          # True
# print(is_anagram("ab", "abc"))         # False
# print(is_anagram("aab", "aba"))        # True
# print(is_anagram("abc", "def"))        # False


# def compress(s):
#     if not s:
#         return ""
#     res = ""
#     count =1
#     current = s[0]
#     if len(res) >= len(s):
#         return s
    
#     for i in range(1,len(s)):
#         if(s[i]==current):
#             count += 1
#         elif s[i] != current:
#             res = res + current+str(count)
#             count = 1
#             current =s[i]
#     return  res + current+str(count)





# print(compress("aabcccccaaa"))  # a2b1c5a3
# print(compress("abc"))          # abc
# print(compress(""))             # 
# print(compress("a"))            # a
# print(compress("aa"))           # a2
# print(compress("aaaaaa"))       # a6
# print(compress("aabb"))         # aabb
# print(compress("aaabbba"))      # a3b3a1



# def reverse_list(lst):
#     res = []
#     for i in range(len(lst)-1,-1,-1):
#         res.append(lst[i])
#     return res
# print(reverse_list([1, 2, 3, 4]))    # [4, 3, 2, 1]
# print(reverse_list([]))               # []
# print(reverse_list([1]))              # [1]
# print(reverse_list([1, 2]))           # [2, 1]
# print(reverse_list(["a", "b", "c"])) # ['c', 'b', 'a']


# def find_max(lst):
#     if not lst:
#      return None
#     cr = lst[0]
#     for i in range(len(lst)):
#         if (lst[i]>cr):
#             cr = lst[i]
#     return cr
# print(find_max([1, 2, 3]))         # 3
# print(find_max([3, 2, 1]))         # 3
# print(find_max([5]))               # 5
# print(find_max([-1, -2, -3]))      # -1
# print(find_max([0, 0, 0]))         # 0
# print(find_max([-5, 10, -3, 7]))   # 10
# print(find_max([]))                # None


# def two_sum(lst,target):
#     seen = {}
#     for i in range(len(lst)):
#         need = target -lst[i]
#         if need in seen :
#             return [seen[need],i] 
#         else:
#             seen[lst[i]] = i
    




# print(two_sum([2, 7, 11, 15], 9))    # [0, 1]
# print(two_sum([3, 2, 4], 6))         # [1, 2]
# print(two_sum([3, 3], 6))            # [0, 1]
# print(two_sum([1, 2, 3, 4], 8))      # None
# print(two_sum([0, 4, 3, 0], 0))      # [0, 3]
# print(two_sum([-1, -2, -3, -4], -6)) # [1, 3]


# def remove_duplicates(lst):
#     seen = {}
#     res = []
#     for num in lst :
#         if num not in seen :
#             res.append(num)
#         seen[num] = True
#     return res


# print(remove_duplicates([1, 2, 3, 2, 1, 4]))        # [1, 2, 3, 4]
# print(remove_duplicates([]))                          # []
# print(remove_duplicates([5]))                         # [5]
# print(remove_duplicates([1, 1, 1, 1]))                # [1]
# print(remove_duplicates(["a", "b", "a", "c", "b"]))  # ['a', 'b', 'c']
# print(remove_duplicates([3, 2, 1]))                   # [3, 2, 1]
# print(remove_duplicates([0, 0, 0, 1, 0, 2, 1]))      # [0, 1, 2]


# def freq(s):
#     seen = {}
#     for word in s.split():
#      seen[word] = seen.get(word,0)+1
#     return seen
# print(freq("the cat and the dog"))
# # {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}

# print(freq("a a a b b"))
# # {'a': 3, 'b': 2}

# print(freq("hello"))
# # {'hello': 1}

# print(freq("one two one two three"))
# # {'one': 2, 'two': 2, 'three': 1}

# def invert(d):
#     res = {}
#     for key,value in d.items():
#         res[value] = key
#     return res
# print(invert({"a": 1, "b": 2, "c": 3}))
# # {1: 'a', 2: 'b', 3: 'c'}

# print(invert({}))
# # {}

# print(invert({"x": 10}))
# # {10: 'x'}

# print(invert({"a": 1, "b": 1}))
# # {1: 'b'}  (last one wins)


# sets and tuples



# def intersec(lst1,lst2):
#     return list(set(lst1)&set(lst2))
# print(intersec([1, 2, 2, 3], [2, 3, 3, 4]))    # [2, 3]
# print(intersec([1, 5, 7], [2, 3, 4]))            # []
# print(intersec([1, 1, 1], [1, 1, 1]))            # [1]
# print(intersec([], [1, 2, 3]))                    # []
# print(intersec([1, 2], [1, 2]))                   # [1, 2]


# def rem(lst):
#     seen = {}
#     res = []
#     for num in lst:
#         if num not in seen:
#             res.append(num)
#             seen[num] = True
#     return res
# print(rem([3, 1, 2, 1, 3, 4, 2]))    # [3, 1, 2, 4]
# print(rem([1, 1, 1]))                 # [1]
# print(rem([5, 4, 3, 2, 1]))           # [5, 4, 3, 2, 1]
# print(rem([]))                         # []
# print(rem([7]))                        # [7]
# print(rem(["a", "b", "a", "c"]))      # ['a', 'b', 'c']

# def cor(lst):
#     d= {}
#     for coordinates,labels in lst:
#         d[coordinates] = labels
#     return d

# print(cor([((1, 2), "A"), ((3, 4), "B"), ((1, 2), "C")]))
# # {(1, 2): 'C', (3, 4): 'B'}

# print(cor([((0, 0), "origin"), ((5, 5), "corner")]))
# # {(0, 0): 'origin', (5, 5): 'corner'}

# print(cor([((1, 1), "X"), ((1, 1), "Y"), ((1, 1), "Z")]))
# # {(1, 1): 'Z'}

# print(cor([]))
# # {}

# print(cor([((9, 9), "solo")]))
# {(9, 9): 'solo'}

# def coun(lst):
#     common = set(lst[0])
#     for s in lst[1:]:
#         common = common&set(s)
#     return len(common)

# print(coun(["hello", "world", "hold"]))    # 2
# print(coun(["abc", "bcd", "cde"]))          # 1
# print(coun(["aaa", "bbb", "ccc"]))          # 0
# print(coun(["abc", "abc", "abc"]))          # 3
# print(coun(["a"]))                           # 1

# def dupl(lst):
#     duplicate = set()
#     seen = set()
#     for num in lst:
#         if num not in seen:
#             seen.add(num)
#         else:
#             duplicate.add(num)
#     return duplicate

# print(dupl([1, 3, 4, 2, 1, 2, 4]))    # {1, 2, 4}
# print(dupl([1, 2, 3]))                  # set()
# print(dupl([5, 5, 5, 5]))              # {5}
# print(dupl([]))                          # set()
# print(dupl([1, 1, 2, 2, 3, 3]))        # {1, 2, 3}
# print(dupl(["a", "b", "a"]))            # {'a'}
# print(dupl([7]))                         # set()


# func
# def find_duplicates(lst):
#     seen = set()
#     dup = set()
#     for num in lst:
#         if num not in seen:
#             seen.add(num)
#         else:
#             dup.add(num)
#     return list(dup)
# print(find_duplicates([1, 3, 2, 3, 5, 1, 6]))

# print(find_duplicates([1, 2, 3]))
# print(find_duplicates([5, 5, 5]))


# def coordinate_labels(pairs):
#     d = {}
#     for x,y,label in pairs:
#         d[x,y] = label
#     return d

# def two_sum(lst,target):
#     seen = {}
#     for i in range(len(lst)):
#         need = target - lst[i]
#         if need in seen:
#             return [seen[need],i]
#         else:
#             seen[lst[i]] = i
# print(two_sum([2, 7, 11, 15], target = 9))

# def sor(lst):
#     return sorted(lst , key = lambda x:x[-1])
# print(sor(["hello", "boa", "zip", "ant"]))
# # ['boa', 'hello', 'zip', 'ant']

# print(sor(["dog", "cat", "bat"]))
# # ['bat', 'cat', 'dog']

# print(sor(["z"]))
# # ['z']

# print(sor(["apple", "be", "arc"]))
# # ['be', 'arc', 'apple']

# def dub(lst):
#     return list(map(lambda x:x*2 , lst))
# print(dub([1, 2, 3]))
# # [2, 4, 6]

# print(dub([-1, 0, 5]))
# # [-2, 0, 10]

# print(dub([]))
# # []

# print(dub([100]))
# # [200]

# def keep_positive(lst):
#     return list(filter(lambda x: x>0 , lst))
# print(keep_positive([1, -2, 3, -4, 5]))
# # [1, 3, 5]

# print(keep_positive([-1, -2, -3]))
# # []

# print(keep_positive([0, 5, -3, 10]))
# # [5, 10]

# print(keep_positive([]))
# # []

# print(keep_positive([7]))
# # [7]

# def factorial(n):
#     if(n==0):
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))    # 120
# print(factorial(0))    # 1
# print(factorial(3))    # 6
# print(factorial(1))    # 1
# print(factorial(10))   # 3628800

# def rec_sum(lst):
#     if(len(lst)==0):
#         return 0
#     return lst[0]+ rec_sum(lst[1:])
    
# print(rec_sum([1, 2, 3, 4]))    # 10
# print(rec_sum([5]))              # 5
# print(rec_sum([]))               # 0
# print(rec_sum([-1, -2, -3]))    # -6
# print(rec_sum([0, 0, 0]))       # 0

def sort_by_frequency(lst):
    d= {}
    for num in lst :
        d[num] = d.get(num,0)+1
    return sorted(lst , key = lambda x:d[x])
print(sort_by_frequency([4, 4, 1, 2, 2, 2]))
# [1, 4, 4, 2, 2, 2]

print(sort_by_frequency([5, 5, 5]))
# [5, 5, 5]

print(sort_by_frequency([3, 1, 3, 1, 2]))
# [2, 3, 1, 3, 1]

print(sort_by_frequency([1]))
# [1]

print(sort_by_frequency([7, 7, 3, 3, 1, 1]))
# [7, 7, 3, 3, 1, 1]