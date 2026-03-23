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
    
#  list

# def rev(lst):
#     lst1 = []
#     for i in range(len(lst)-1,-1,-1):
#         lst1.append(lst[i])
#     return lst1
# print(rev([1, 2, 3, 4, 5]))       # [5, 4, 3, 2, 1]
# print(rev([10, 20, 30]))           # [30, 20, 10]
# print(rev([7]))                    # [7]
# print(rev([]))                     # []
# print(rev(["a", "b", "c"]))        # ["c", "b", "a"]

# def remove_dupes(lst):
#     seen = {}
#     res = []
#     for num in lst:
#         if num not in seen:
#             res.append(num)
#         seen[num] = True
#     return res

# print(remove_dupes([1, 2, 2, 3, 4, 4, 5]))       # [1, 2, 3, 4, 5]
# print(remove_dupes([1, 1, 1, 1]))                  # [1]
# print(remove_dupes([5, 3, 5, 3, 5, 3]))            # [5, 3]
# print(remove_dupes([]))                             # []
# print(remove_dupes(["a", "b", "a", "c", "b"]))     # ["a", "b", "c"]

# def two_sum(lst, target):
#     seen = {}
#     for i in range(0,len(lst)):
#         need = target - lst[i]
#         if need in seen :
#             return [seen[need] , i]
#         else:
#             seen[lst[i]] = i
# print(two_sum([2, 7, 11, 15], 9))       # [0, 1]
# print(two_sum([3, 2, 4], 6))            # [1, 2]
# print(two_sum([1, 5, 3, 7], 8))         # [1, 3]
# print(two_sum([10, 20, 30, 40], 50))    # [1, 2]

# def rotate_list(lst,k):

    
#     return lst[-k:]+lst[:-k]
# print(rotate_list([1, 2, 3, 4, 5], 2))    # [4, 5, 1, 2, 3]
# print(rotate_list([10, 20, 30], 1))        # [30, 10, 20]
# print(rotate_list([1, 2, 3], 3))           # [1, 2, 3]
# print(rotate_list([], 5))                  # []

# def second_largest(lst):
#     first =lst[0]
#     second = None
#     for i in range(1,len(lst)):
#         if(lst[i]>first):
#             second = first
#             first =lst[i]
#         elif lst[i] != first and (second is None or second < lst[i] ):
#             second = lst[i]

#     return second
# print(second_largest([3, 7, 2, 9, 1]))        # 7
# print(second_largest([10, 20, 30]))            # 20
# print(second_largest([5, 5, 5]))               # None
# print(second_largest([1]))                     # None
# print(second_largest([4, 1, 8, 8, 3]))         # 4
# def merge_sorted(lst1,lst2):
#     finalst = []
#     i,j =0,0
#     while i < len(lst1) and j < len(lst2):
#         if lst1[i]<lst2[j] :
#             finalst.append(lst1[i])
#             i+=1
#         else:
#             finalst.append(lst2[j])
#             j+=1
#     finalst+= lst1[i:]
#     finalst+= lst2[j:]
#     return finalst
# print(merge_sorted([1, 3, 5], [2, 4, 6]))        # [1, 2, 3, 4, 5, 6]
# print(merge_sorted([1, 2, 3], [4, 5, 6]))        # [1, 2, 3, 4, 5, 6]
# print(merge_sorted([1, 5, 9], [2, 3]))            # [1, 2, 3, 5, 9]
# print(merge_sorted([], [1, 2, 3]))                # [1, 2, 3]
# print(merge_sorted([7], [3, 8]))                  # [3, 7, 8]

# def intersection(lst1, lst2):
#     seen = {}
#     res = []
#     for num in lst1:
#         seen[num] = True
#     for num in lst2:
#         if num in seen:
#             res.append(num)
#             del seen[num]
#     return res
# print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))          # [3, 4]
# print(intersection([1, 1, 2, 2], [2, 2, 3, 3]))          # [2]
# print(intersection([1, 2, 3], [4, 5, 6]))                # []
# print(intersection([], [1, 2]))                           # []
# print(intersection([5, 5, 5], [5, 5, 5]))                # [5]

#dictionary
# def freq(s):
#     seen = {}
#     for word in s.split():
#         seen = seen.get(word,0)+1
#     return seen



# def ana(lst):
    # seen = {}
    # 
    # for word in lst:
        # key = ".join(sorted(word))"
        # if key in word:
            # seen[key].append(word)
        # else:
            # seen[key] = word
    # return list[res.values()]

# def inv(d):
#     res = {}
#     for key,value in d.items():
#         res[value] = key
#     return res

# def map(s1,s2):
    # seen = {}
    # for i in range(len(s1)):
        # seen[s1[i]] = s2[i]
        # 

# def twosum(lst,target):
    # seen = {}
    # for i in range(len(lst)):
        # need = target - lst[i]
        # for num in lst :
            # if need in seen:
                # return [seen[need],i]
            # else:
                # seen[lst[i]] = i
# 


# def inv(d):
#     res={}
#     for value,key in d.items():
#         if value in res:
#             res[value].append(key)

# def idk(s):
#     seen = {}
#     for char in s:
#         seen[char] = seen.get(char,0)+1
#     return seen

def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Test
lst1 = [1, 2, 2, 3]
lst2 = [2, 3, 3, 4]

result = common_elements(lst1, lst2)
print(result)