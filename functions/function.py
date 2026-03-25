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

# def coordinate_labels(pairs):
#     d = {}
#     for x,y,label in pairs:
#         d[x,y] = label
#     return d
# print(coordinate_labels([(0, 0, "origin"), (1, 2, "A"), (3, 4, "B")]))
# print(coordinate_labels([(5, 5, "center")]))
# print(coordinate_labels( []))

# def two_sum(lst, target):
#     d = {}
#     for i in range (len(lst)):
#         need = target -lst[i]
#         if need in d:
#             return (d[need],i)
#         else:
#             d[lst[i]] = i
# print(two_sum( [2, 7, 11, 15], target = 9)) 
# print(two_sum( [3, 2, 4], target = 6))
# print(two_sum([1, 5, 3, 7], target = 8))

# def sor(lst):
#     return sorted(lst,key =lambda x:x[-1])
# print(sor(["hello", "boa", "zip", "ant"]))
# print(sor(["dog", "cat", "bat"]))
# print(sor( ["z"]))

# def dub(lst):
#     return list(map(lambda x: x*2, lst))
# print(dub([1, 2, 3]))
# print(dub([-1, 0, 5]))
# print(dub([]))

# def keep_positive(lst):
#     return list(filter(lambda x: x>0 ,lst))
# print(keep_positive([1, -2, 3, -4, 5]))
# print(keep_positive([-1, -2, -3]))
# print(keep_positive([0, 5, -3, 10]))
    

# Input: [1, -2, 3, -4, 5]
# Output: [1, 3, 5]

# Input: [-1, -2, -3]
# Output: []

# Input: [0, 5, -3, 10]
# Output: [5, 10]

# def factorial(n):
#     if (n==0):
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))
# print(factorial(0))
# print(factorial(3))

def rec_sum(lst):
    if (len(lst)==0):
        return 0
    return lst[0] + rec_sum(lst[1:])
print(rec_sum([1, 2, 3, 4]))
print(rec_sum( [5]))
print(rec_sum([]))