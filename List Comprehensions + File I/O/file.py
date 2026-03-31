# def sort_by_length(lst):
#     return sorted(lst , key = lambda x:len(x))
# print(sort_by_length(["banana", "pie", "apple", "kiwi"]))
# print(sort_by_length(["a", "bbb", "cc"]))
# print(sort_by_length([]))

# def only_even(lst):
#     return list(filter(lambda x:x%2==0,lst))
# print(only_even([1, 2, 3, 4, 5, 6]))
# print(only_even([7, 9, 11]))
# print(only_even([0, -2, 3, -4]))

def recursive_max(lst):
    if(len(lst)==1):
        return lst[0]
    big = lst[0]
    bigger = recursive_max(lst[1:])
    if(big>bigger):
        return big
    else: 
        return bigger
print(recursive_max([3, 1, 4, 1, 5]))
print(recursive_max([10]))
print(recursive_max([-3, -1, -7]))