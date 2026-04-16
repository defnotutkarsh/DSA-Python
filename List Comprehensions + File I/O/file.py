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

# def recursive_max(lst):
#     if(len(lst)==1):
#         return lst[0]
#     big = lst[0]
#     bigger = recursive_max(lst[1:])
#     if(big>bigger):
#         return big
#     else: 
#         return bigger
# print(recursive_max([3, 1, 4, 1, 5]))
# print(recursive_max([10]))
# print(recursive_max([-3, -1, -7]))



# def sort_by_length(lst):
#     return sorted(lst,key = lambda x:len(x))
# print(sort_by_length(["banana", "pie", "apple", "kiwi"]))
# print(sort_by_length(["a", "bbb", "cc"]))
# print(sort_by_length([]))


# def only_even(lst):
#     return list(filter(lambda x:x%2==0,lst))
# print(only_even([1, 2, 3, 4, 5, 6]))
# print(only_even([7, 9, 11]))
# print(only_even([0, -2, 3, -4]))

# def squares(lst):
#     sq = [x**2 for x in lst ]
#     return sq
# print(squares( [1, 2, 3, 4]))
# print(squares( [-2, 0, 3]))
# print(squares( []))

# def long_words(lst,n):
#     wor = [x for x in lst if len(x)>n]
#     return wor
# print(long_words(["hello", "hi", "world", "go"], 2))
# print(long_words(["a", "bb", "ccc"], 1))
# print(long_words(["test"], 5))


# def flatten(lst):
#     flat = [x for row in lst for x in row ]
#     return(flat)
# print(flatten( [[1, 2], [3, 4], [5, 6]]))
# print(flatten([["a", "b"], ["c"]]))
# print(flatten([[], [1], []]))


# def word_lengths(s):
#     s= s.split()
#     length = [len(word) for word in s]
#     return length
# print(word_lengths("hello world foo"))
# print(word_lengths("I am here"))
# print(word_lengths("python"))

# def even_squares(lst):

#     return [x**2 for x in lst if x%2==0]
# print(even_squares([1, 2, 3, 4, 5, 6]))
# print(even_squares([7, 9, 11]))
# print(even_squares([0, -2, 3]))


with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())