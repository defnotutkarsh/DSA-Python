# def rev(lst):
#     lost = []
#     for i in range(len(lst)-1,-1,-1):
#         lost.append(lst[i])
#     return lost
# print(rev([1, 2, 3, 4, 5]))       # [5, 4, 3, 2, 1]
# print(rev([10, 20, 30]))           # [30, 20, 10]
# print(rev([7]))                    # [7]
# print(rev([]))                     # []
# print(rev(["a", "b", "c"]))        # ["c", "b", "a"]

# def find_max(lst):
    # if(len(lst)==0):
        # return None
    # no = lst[0]
    # for i in range(len(lst)):
        # if(lst[i]>no):
            # no = lst[i]
    # return no
# print(find_max([3, 7, 2, 9, 1]))        # 9
# print(find_max([10, 20, 30]))            # 30
# print(find_max([-5, -2, -8]))            # -2
# print(find_max([42]))                    # 42
# print(find_max([]))                      # None

# def remove_dupes(lst):
    # seen = {}
    # res = []
    # for num in lst:
        # if(num not in seen):
            # res.append(num)
            # seen[num] = True
    # return res
# 
# print(remove_dupes([1, 2, 2, 3, 4, 4, 5]))       # [1, 2, 3, 4, 5]
# print(remove_dupes([1, 1, 1, 1]))                  # [1]
# print(remove_dupes([5, 3, 5, 3, 5, 3]))            # [5, 3]
# print(remove_dupes([]))                             # []
# print(remove_dupes(["a", "b", "a", "c", "b"]))     # ["a", "b", "c"]

# def two_sum(lst, target):
    # seen = {}
    # need = 0
    # for i in range(len(lst)):
        # if(target -lst[i]):
            # 
# 



# def find_max(lst):
    # if(len(lst)==0):
        # return None
    # no = lst[0]
    # for i in range (len(lst)):
        # if(lst[i]>no):
            # no = lst[i]
    # return no
# print(find_max([3, 7, 2, 9, 1]))        # 9
# print(find_max([10, 20, 30]))            # 30
# print(find_max([-5, -2, -8]))            # -2
# print(find_max([42]))                    # 42
# print(find_max([]))                      # None

# def remove_dupes(lst):
#     res =[]
#     seen = {}
#     for num in lst:
#         if(num not in seen):
#             res.append(num)
#         seen[num] = True
#     return res
# print(remove_dupes([1, 2, 2, 3, 4, 4, 5]))       # [1, 2, 3, 4, 5]
# print(remove_dupes([1, 1, 1, 1]))                  # [1]
# print(remove_dupes([5, 3, 5, 3, 5, 3]))            # [5, 3]
# print(remove_dupes([]))                             # []
# print(remove_dupes(["a", "b", "a", "c", "b"]))     # ["a", "b", "c"]

# def two_sum(lst, target):
    # need = 0
    # seen = {}
    # 
    # for i in range(len(lst)):
        # need = target - lst[i]
        # if(need in seen):
            # return [seen[need],i]
        # else:
            # seen[lst[i]] = i
# print(two_sum([2, 7, 11, 15], 9))       # [0, 1]
# print(two_sum([3, 2, 4], 6))            # [1, 2]
# print(two_sum([1, 5, 3, 7], 8))# [1, 3]
# print(two_sum([10, 20, 30, 40], 50))    # [1, 2]


# def two_sum(lst, target):
#     seen = {}
#     for i in range(len(lst)):
#         need = target - lst[i]
#         if(need in seen):
#             return [seen[need],i]
#         else:
#             seen[lst[i]] = i
# print(two_sum([2, 7, 11, 15], 9))       # [0, 1]
# print(two_sum([3, 2, 4], 6))            # [1, 2]
# print(two_sum([1, 5, 3, 7], 8))         # [1, 3]
# print(two_sum([10, 20, 30, 40], 50))    # [1, 2]

# def rotate_list(lst, k):
    # lst1 = []
    # if(len(lst)==0):
        # return []
    # lst1 = lst[-k:]+lst[:-k]
    # return lst1
    # 
# print(rotate_list([1, 2, 3, 4, 5], 2))    # [4, 5, 1, 2, 3]
# print(rotate_list([10, 20, 30], 1))        # [30, 10, 20]
# print(rotate_list([1, 2, 3], 3))           # [1, 2, 3]
# print(rotate_list([], 5))                  # []

def second_largest(lst):
    if(len(lst)<2):
        return None
    first = lst[0]
    second = None
    for i in range(len(lst)):
        if(lst[i]>first):
            second = first
            first = lst[i]
        elif (lst[i] != first) and (second is None or lst[i] > second): 
            second = lst[i]
    return second



print(second_largest([3, 7, 2, 9, 1]))        # 7
print(second_largest([10, 20, 30]))            # 20
print(second_largest([5, 5, 5]))               # None
print(second_largest([1]))                     # None
print(second_largest([4, 1, 8, 8, 3]))         # 4