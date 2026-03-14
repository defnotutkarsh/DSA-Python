# def sum(n):
    # add = 0
    # while(n>0):
        # add = n%10 + add
        # n = n//10
    # return add
# print(sum(123))
# print(sum(456))
# print(sum(0))

# def rev(n):
#     org = n
#     add = 0
#     while(n>0):
#         add = n%10 + add*10
#         n=n//10
#     return (add==org)

# print(rev(121))
# print(rev(123))
# print(rev(1221))

# def gcd(n1,n2):
#     less = min(n1,n2)
#     for i in range (less,0,-1):
#         if(n1%i==0) and (n2%i==0):
#             return i
# print(gcd(12, 8))
# print(gcd(15, 5))
# print(gcd(7, 3))

# def lcm(n1,n2):
#     high = max(n1,n2)
#     while(True):
#         if(high%n1==0) and (high%n2==0):
#             return high
#         else:
#             high += 1
# print(lcm(4, 6))
# print(lcm(3, 5))
# print(lcm(2, 8))

# def factorial(n):
#     sum=1
#     for i in range(2,n+1):
#         sum = sum*i
#     return sum
# print(factorial(5))
# print(factorial(1))
# print(factorial(0))

# def pow(n1,n2):
#     sum = 1
#     while(n2>0):
#         sum=sum*n1
#         n2=n2-1
#     return sum
# print(pow(2, 3))
# print(pow(5, 2))
# print(pow(5, 0))

# def count(n):
#     cou = 0 
#     while(n>0):
#         cou +=1
#         n=n//10
#     return cou
# def armstrong(n):
#     arm = 0
#     org = n
#     no = count(n) 
#     while(n>0):
#         arm = arm + pow(n%10,no)
#         n=n//10
#     return (arm ==org)
# print(armstrong(153))
# print(armstrong(9474))
# print(armstrong(123))


# def reverse(s):
#     str = ""
#     for i in range(len(s)-1,-1,-1):
#         str = str+ s[i]
#     return (str==s)
# print(reverse("madam"))
# print(reverse("hello"))
# print(reverse("a"))
# print(reverse(""))

# def vowel(s):
#     s = s.lower()
#     count = 0
#     vow = "aeiou"
#     for i in range(len(s)):
#         for j in range (len(vow)):
#             if(s[i]==vow[j]):
#                 count+=1
#     return count
# print(vowel("hello"))
# print(vowel("APPLE"))
# print(vowel("xyz"))
# print(vowel("aEiOu"))


