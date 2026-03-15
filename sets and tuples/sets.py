def rev(s):
    res = {}
    
    for char in s :
        res[char] = res.get(char,0) +1
    return res
print(rev("hello"))