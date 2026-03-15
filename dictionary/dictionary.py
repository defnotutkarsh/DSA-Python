# def compres(s):
    # count = {}
    # res = ""
    # for char in s :
        # if (char in count):
            # count[char] = count[char]+1
        # else:
            # count[char] = 1
    # for key in count:
        # res = res + key + str(count[key])
    # return res
# print(compres("aaabbbcc"))

# def compress(s):
#     current = s[0]
#     count = 1
#     res = ""
#     for i in range(1,len(s)):
#         if(s[i]==current):
#             count = count + 1
#         elif(s[i]!=current):
#             res = res + current +str(count)
#             count = 1
#             current = s[i]
#     return res + current + str(count)
# print(compress("aabbaac"))

# def shif(lst):
#     zer = []
#     nonzer = []
#     for i in range (len(lst)):
#         if(lst[i]==0):
#             zer.append(lst[i])
#         else:
#             nonzer.append(lst[i])
#     return nonzer + zer
# print(shif([0, 1, 0, 3, 12]))

# def longest(lst):
    # larg = ""
    # for word in lst:
        # if(len(word)>len(larg)):
            # larg =word
    # return larg
# print(longest(["hi", "hello", "hey"] ))

# def freq(s):
#     count = {}
#     for word in s.split():
#         count[word] = count.get(word,0)+1
#     return count
# print(freq("the cat and the dog"))
# print(freq("a a a b b"))
# print(freq("hello"))


# def freq(s):
#     count = {}
#     for word in s.split():
#         count[word] = count.get(word,0) + 1
#     return count

# print(freq("the cat and the dog"))
# print(freq("a a a b b"))
# print(freq("hello"))

# def freq(s):
#     count = {}
#     s = s.split()

#     for word in s :
#         count[word] = count.get(word,0) + 1
#     return count
# print(freq("the cat and the dog"))
# print(freq("a a a b b"))
# print(freq("hello"))


# def invert(d):
#     res = {}
#     for key,value in d.items():
#         res[value] = key
#     return res
# print(invert({"a": 1, "b": 2, "c": 3}))

# def ana(lst):
#     res = {}
#     for word in lst:
#         key = "".join(sorted(word))
#         if key in res :
#             res[key].append(word)
#         else:
#             res[key] = [word]
#     return list(res.values())
# print(ana(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(ana(["hello", "world"]))

# def ana(lst):
#     res = {}
#     for word in lst :
#         key = "".join(sorted(word))
#         if key in res :
#             res[key].append(word)
#         else:
#             res[key] = [word]
#     return list(res.values())


# print(ana(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(ana(["hello", "world"]))


# def charmap(s1,s2):
#     dic = {}
#     for i in range (len(s1)):
#         dic[s1[i]] = s2[i]
#     return dic
# print(charmap("hello", "world"))
# print(charmap("abc", "xyz"))

# def twosum(lst,target):
#     seen = {}
#     for i in range (len(lst)):
#         need = target - lst[i]
#         if (need in seen):
#             return [seen[need],i]
#         else:
#             seen[lst[i]] = i
# print(twosum([3, 2, 4], target=6))
# print(twosum([2, 7, 11, 15],target=9))


def invertfinalboss(d):
    res  = {}
    for key,value in d.items():
        
        if value in res :
            res[value].append(key)
        else:
            res[value] = [key]
    return res
print(invertfinalboss({"a": 1, "b": 2, "c": 1}))
print(invertfinalboss({"x": 5, "y": 5, "z": 5}))