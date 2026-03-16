# def rev(s):
#     res = {}
    
#     for char in s :
#         res[char] = res.get(char,0) +1
#     return res
# print(rev("hello"))

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

def nonrep(s):
    count = {}
    for char in s:
        count[char] = count.get(char,0) + 1
    for char in s:

        if (count[char] == 1 ):
            return char
    return None
print(nonrep("aabbcde"))