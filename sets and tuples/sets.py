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

# def nonrep(s):
#     count = {}
#     for char in s:
#         count[char] = count.get(char,0) + 1
#     for char in s:

#         if (count[char] == 1 ):
#             return char
#     return None
# print(nonrep("aabbcde"))

# def compress(s):
#     current =s[0]
#     count = 0
#     res =""
#     for i in range(1,len(s)):
#         if (len(s)==current):
#             count+=1
#         elif(s[i]!=current):
#             res = res+ current + str(count)_
#             count =1
#             current = s[i]
#     return res + current + str(count)
    