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