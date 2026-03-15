# def sumofdig(n):
#     sum = 0
#     while(n>0):
#         sum = sum + n%10
#         n=n//10
#     return sum
# print(sumofdig(123))
# print(sumofdig(456))

# def reverseno(n):
#     rev = 0
#     original = n
#     while(n>0):
#         rev = rev*10 + n%10
#         n=n//10
#     return (rev==original)
# print(reverseno(121))
# print(reverseno(123))
# print(reverseno(1221))

# def gcd(n1,n2):
#     no = max(n1,n2)
#     for i in range (no,0,-1):
#         if(n1%i==0 and n2%i==0):
#          return i
# print(gcd(12, 8))
# print(gcd(15, 5))
# print(gcd(7, 3))

# def lcm(n1,n2):
#     no = max(n1,n2)
#     while(True):
#         if(no%n1 == 0 and no%n2 == 0):
#             return no
#         no = no+1
# print(lcm(4, 6))
# print(lcm(3, 5))
# print(lcm(2, 8))

# def fact(n):
#     fax =1
#     for i in range (n,1,-1):
#         fax = fax*i
#     return fax
# print(fact(5))
# print(fact(1))
# print(fact(0))

# def power(n1,n2):
#     pow = 1
#     for i  in range (n2):
#         pow = pow*n1
#     return pow
# print(power(2, 3))
# print(power(5, 2))
# print(power(5, 0))
# def count(n):
    
#     cou = 0
#     while(n>0):
#         cou = cou +1
#         n = n//10
#     return cou

# def armstrong(n):
#     org = n
#     sum = 0
#     digit = count(n)
#     while(n>0):
#         sum = sum + pow(n%10,digit)
#         n=n//10
#     return (sum==org)
# print(armstrong(153))
# print(armstrong(9474))
# print(armstrong(123))


# s = "hello"
# print(s[0])      # first character
# print(s[-1])     # last character
# print(len(s))    # length

# def reverse_string(str):
#     start,end = 0,len(str)
#     while(start<end):
#         s[start],s[end] = s[end],s[start]
#         start+=1
#         end-=1
#     return 


# def rev(s):
    # str = ""
    # for i in range(len(s)-1,-1,-1):
        # str = str + s[i]
    # return str
# print(rev("h""e""l""l""o"))



# def is_palindrome(s):
    # str = ""
    # org = s
    # for i in range(len(s)-1,-1,-1):
        # str = str + s[i]
    # return (str==s)
# print(is_palindrome("madam"))
# print(is_palindrome("hello"))
# print(is_palindrome("a"))
# print(is_palindrome(""))

# def vowel(s):
#     s = s.lower()
#     vow = "aeiou"
#     count = 0
#     for i in range(len(s)):
#         for j in range(len(vow)):
#             if(s[i]==vow[j]):
#                 count +=1
#     return count
# print(vowel("hello"))
# print(vowel("APPLE"))
# print(vowel("xyz"))
# print(vowel("aEiOu"))

# def word(s):
#     return len(s.split())
#     # spa =" "
#     # count = 1
#     # for i in range(len(s)):
#     #     for j in range(len(spa)):
#     #         if(s[i]==spa[j]):
#     #             count+=1
#     # return count
# print(word("hello world"))
# print(word("I love Python")) 
# print(word("word")) 
# print(word("")) 
# def words(s):
    # return  len(s.split())
    #  





# def unique(s):
#     counts = {}
#     for char in s :
#         if char in counts:
#             count[char]= counts[char]+1
#         else:
#             counts[char] = 1

# def unique(s):
#     count = {}
#     for char in s :
#         if(char in count):
#             count[char] = count[char] + 1
#         else:
#             count[char] = 1
#     for char in s :
#         if(count[char] == 1):
#             return char
#     return ""
# print(unique("aabbcdd"))
# print(unique("hello"))
# print(unique("aabbcc"))
# print(unique("abcd"))

# def reverse(s):
    # tr = ""
    # for i in range (len(s)-1,-1,-1):
        # tr = tr + s[i]
    # return tr
# print(reverse("hello"))
# print(reverse("Python"))

# def reverse(s):
    # tri = ""
    # for i in range(len(s)-1,-1,-1):
        # tri = tri + s[i]
    # return tri
# def unique(s):
#     count = {}
#     for char in s :
#         if (char in count):
#             count[char] = count[char]+1
#         else:
#             count[char]= 1
#     for char in s:
#         if(count[char]==1):
#             return char
#     return " "
# print(unique("aabbcdd"))
# print(unique("hello"))
# print(unique("aabbcc"))
# print(unique("abcd"))



# def remove(s):
#     count= {}
#     fin = ""
#     for char in s:
#         if(char in count):
#             count[char] = count[char]+1
#         else:
#             count[char] = 1
#     for char in s :
#         if(count[char]==1):
#             fin = fin + char
#     return fin
# print(remove("hello")) 
# print(remove("aabbcc")) 
# print(remove("abcd")) 
# print(remove("mississippi")) 


# def remove(s):
#     dic = {}
#     tri = ""
#     for char in s:
#         if (char not in dic):
#             tri = tri +char
#             dic[char] = True
#     return tri
# print(remove("hello")) 
# print(remove("aabbcc")) 
# print(remove("abcd")) 
# print(remove("mississippi"))

# def ana(s1,s2):
#     dic1 ={}
#     dic2 = {}
#     for char in s1 :
#         if(char in dic1):
#             dic1[char]= dic1[char]+1
#         else:
#             dic1[char] = 1
#     for char in s2 :
#         if(char in dic2):
#             dic2[char]= dic2[char]+1
#         else:
#             dic2[char] = 1
#     return (dic1 == dic2)
# print(ana("listen", "silent"))
# print(ana("hello", "world"))
# print(ana("aab", "aba"))
# print(ana("aab", "aaa"))

# def rev(s):
#     res = ""
#     for i in range(len(s)-1,-1,-1):
#         res = res + s[i]
#     return res
# print(rev("hello"))
# print(rev("Python"))

# def vowel(s):
#     s = s.lower()
#     vow = "aeiou"
#     count = 0
#     for i in range (len(s)) : 
#         for j in range (len(vow)):
#             if (s[i]== vow[j]):
#                 count+=1
#     return count
# print(vowel("hello")) 
# print(vowel("APPLE")) 
# print(vowel("xyz")) 
# print(vowel("aEiOu")) 

# def word(s):
    # return  len(s.split())
# print(word("hello world"))
# print(word("I love Python"))
# print(word("word"))
# print(word(""))
    # 
# def unique(s):
    # count ={}
    # for char in s :
        # if(char in count ):
            # count[char] = count[char]+1
        # else:
            # count[char] = 1
    # for char in s:
        # if(count[char]==1):
            # return char
    # return ""
        # 
# print(unique("aabbcdd"))
# print(unique("hello")) 
# print(unique("aabbcc")) 
# print(unique("abcd"))

# def remove(s):
#     seen = {}
#     res = ""
#     for char in s :
#         if(char not in seen):
#             res = res + char
#             seen[char] = True
#     return res
# print(remove("hello"))
# print(remove("aabbcc"))
# print(remove("abcd"))
# print(remove("mississippi"))
# 
# def ana(s1,s2):
    # dic ={}
    # dic2 = {}
    # for char in s1 :
        # if (char in dic):
            # dic[char] = dic[char]+1 
        # else:
            # dic[char]= 1
    # for char in s2 :
        # if (char in dic2):
            # dic2[char] = dic2[char]+1 
        # else:
            # dic2[char]= 1
    # return (dic == dic2)
# print(ana("listen", "silent"))
# print(ana("hello", "world"))
# print(ana("aab", "aba"))
# print(ana("aab", "aaa"))
    # 

# def sub(s):
    # res = []
    # for i in range (len(s)) :
        # for j in range (i+1,len(s)+1):
            # res.append(s[i:j])
    # return res
# print(sub("abc"))
# print(sub("ab"))
# 

# def compress(s):
#     count = {}
#     for char in s :
#         if (char in count):
#             count[char] = count[char]+1
#         else:
#             count[char] = 1
#     result = ""
#     for key in count:
        # result = result + key +str(count[key])
#     return result
# print(compress("aaabbc")) 
# print(compress("aaa")) 
# print(compress("abc")) 
# print(compress("")) 

# def longg(s):
#     s = s.split()
#     longest = ""
#     for word in s:
#         if (len(word)>len(longest)):
#             longest = word
#     return longest
# print(longg("I love Python")) 
# print(longg("hello world")) 
# print(longg("a bb ccc")) 
# print(longg("cat")) 
# 

# def sub(s):
    # res =[]
    # for i in range (0,len(s)):
        # for j in range (i+1,len(s)+1):\
            # res.append(s[i:j])
    # return res
# print(sub("abc"))
# print(sub("ab"))

# def compress(s):
    # count = {}
    # for char in s:
        # if(char in count):
            # count[char] = count[char]+1
        # else:
            # count[char] = 1
    # res = ""
    # for key in count :
        # res = res + key + str(count[key])
    # return res
# print(compress("aaabbc")) 
# print(compress("aaa")) 
# print(compress("abc")) 
# print(compress("")) 
        # 

def longg(s):
    s = s.split()
    longest = ""
    for word in s :
        if(len(word)>len(longest)):
            longest = word
    return longest
print(longg("I love Python"))
print(longg("hello world"))
print(longg("a bb ccc"))
print(longg("cat"))
