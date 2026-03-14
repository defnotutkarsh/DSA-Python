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

# def second_largest(lst):
    # if(len(lst)<2):
        # return None
    # first = lst[0]
    # second = None
    # for i in range(len(lst)):
        # if(lst[i]>first):
            # second = first
            # first = lst[i]
        # elif (lst[i] != first) and (second is None or lst[i] > second): 
            # second = lst[i]
    # return second
# 
# 
# 
# print(second_largest([3, 7, 2, 9, 1]))        # 7
# print(second_largest([10, 20, 30]))            # 20
# print(second_largest([5, 5, 5]))               # None
# print(second_largest([1]))                     # None
# print(second_largest([4, 1, 8, 8, 3]))         # 4

# def two_sum(lst, target):
    # seen = {}
    # for i in range (len(lst)):
        # need = target - lst[i]
        # if(need in seen):
            # return [seen[need],i]
        # else:
            # seen[lst[i]] = i
        # 
# print(two_sum([2, 7, 11, 15], 9))       # [0, 1]
# print(two_sum([3, 2, 4], 6))            # [1, 2]
# print(two_sum([1, 5, 3, 7], 8))         # [1, 2]
# print(two_sum([10, 20, 30, 40], 50))    # [1, 2]

# def rotate_list(lst, k):
    # return lst[-k:]+lst[:-k]
            # 
# print(rotate_list([1, 2, 3, 4, 5], 2))    # [4, 5, 1, 2, 3]
# print(rotate_list([10, 20, 30], 1))        # [30, 10, 20]
# print(rotate_list([1, 2, 3], 3))           # [1, 2, 3]
# print(rotate_list([], 5))                  # []

# def second_largest(lst):
    # first = lst[0]
    # second = None
    # if(len(lst)<2):
        # return None
    # for i in range (len(lst)):
        # if (lst[i]>first):
            # second = first
            # first = lst[i]
        # elif((lst[i]!=first)and(second is None or lst[i]> second)):
            # second = lst[i]
    # return second
# 
# print(second_largest([3, 7, 2, 9, 1]))        # 7
# print(second_largest([10, 20, 30]))            # 20
# print(second_largest([5, 5, 5]))               # None
# print(second_largest([1]))                     # None
# print(second_largest([4, 1, 8, 8, 3]))         # 4

# def  move_zeroes(lst):
#     zer = []
#     nonzer = []
#     for i in range(len(lst)):
#         if (lst[i]==0):
#             zer.append(lst[i])
#         else:
#             nonzer.append(lst[i])
#     return nonzer + zer




# print(move_zeroes([0, 1, 0, 3, 12]))      # [1, 3, 12, 0, 0]
# print(move_zeroes([1, 2, 3]))              # [1, 2, 3]
# print(move_zeroes([0, 0, 0]))              # [0, 0, 0]
# print(move_zeroes([4, 0, 5, 0, 6]))       # [4, 5, 6, 0, 0]
# print(move_zeroes([]))                     # []

# def count_freq(lst):
    # freq = {}
    # for num in lst :
        # if num in freq :
            # freq[num] += 1
        # else:
            # freq[num] = 1
    # return freq
# 
# 
# print(count_freq([1, 2, 2, 3, 3, 3]))           # {1: 1, 2: 2, 3: 3}
# print(count_freq(["a", "b", "a", "c", "b"]))     # {"a": 2, "b": 2, "c": 1}
# print(count_freq([7]))                            # {7: 1}
# print(count_freq([]))                             # {}


# def merge_sorted(lst1,lst2):
#     mylst = []
#     i = 0
#     j = 0
#     while(i < len(lst1) and j < len(lst2)):
#         if lst1[i]>lst2[j]:
#             mylst.append(lst2[j])
#             j= j+1
#         else:
#             mylst.append(lst1[i])
#             i += 1
#     mylst = mylst + lst1[i:]
#     mylst = mylst + lst2[j:]
#     return mylst
# print(merge_sorted([1, 3, 5], [2, 4, 6]))        # [1, 2, 3, 4, 5, 6]
# print(merge_sorted([1, 2, 3], [4, 5, 6]))        # [1, 2, 3, 4, 5, 6]
# print(merge_sorted([1, 5, 9], [2, 3]))            # [1, 2, 3, 5, 9]
# print(merge_sorted([], [1, 2, 3]))                # [1, 2, 3]
# print(merge_sorted([7], [3, 8]))                  # [3, 7, 8]


# def intersection(lst1, lst2):
#     seen = {}
#     res = []
#     for num in lst1 :
#         if(num in lst1):
#             seen[num] = True
#     for num in lst2:
#         if(num in seen):
#             res.append(num)
#             del seen[num]
#     return res



# print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))          # [3, 4]
# print(intersection([1, 1, 2, 2], [2, 2, 3, 3]))          # [2]
# print(intersection([1, 2, 3], [4, 5, 6]))                # []
# print(intersection([], [1, 2]))                           # []
# print(intersection([5, 5, 5], [5, 5, 5]))                # [5]

# def has_pair(lst, target):
    # seen = {}
    # for i in range (len(lst)):
        # need = target - lst[i]
        # if(need in seen):
            # return True
        # else: seen[lst[i]] = i
    # return False
# print(has_pair([1, 4, 7, 2], 9))         # True (7+2)
# print(has_pair([1, 2, 3, 4], 10))        # False
# print(has_pair([5, 5], 10))              # True
# print(has_pair([3], 6))                  # False
# print(has_pair([], 5))                   # False


def find_missing(lst):
    n = len(lst)
    org = 0
    sum = (n*(n+1))//2
    for i  in range (len(lst)):
        org = org + lst[i]
    if(sum == org):
        return []
    else:
        return sum - org

print(find_missing([3, 0, 1]))            # 2
print(find_missing([0, 1]))               # 2
print(find_missing([9,6,4,2,3,5,7,0,1]))  # 8
print(find_missing([0]))                  # 1