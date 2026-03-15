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

def ana(lst):
    res = {}
    for word in lst :
        key = "".join(sorted(word))
        if key in res :
            res[key].append(word)
        else:
            res[key] = [word]
    return list(res.values())


print(ana(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(ana(["hello", "world"]))
