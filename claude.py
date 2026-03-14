# print("tell me ur name ")
# name = input()
# print("tell me ur age")
# age = int(input())

# birth_year = 2026 - age
# print("ur birth year is", birth_year)
# old_age = 50 - age
# print("ull get 50 after",old_age,"years")
# old_year = 2026 + old_age
# print("ull turn 50 in ",old_year)

# print("enter a no.")
# number = int(input())
# if(number%2==0):
#     print("even")
# else :
#     print("odd")

# number = int(input("enter a no."))
# sum =0 ;
# for i in range(1,number+1):
#     sum+=i
# print(sum)
# n = int(input("enter a no."))    
# count = 1
# while count <=n:
#     print(count)
#     count+= 1

# mylist[1:4] includes index 1 up to (but not including) index 4
# numbers = [10,20,30,40,50]
# for num in numbers :
#     print(num)
# def function_oddeven(num):
#     if(num%2==0):
#         return "even"
        

    
#     else :
#         return "odd"
#  python claude.py

# number =int(input("enter the no."))
# print(function_oddeven(number))
# def function_birthyear(num):
#     return (2026-num)
# year = int(input("enter the no."))
# print(function_birthyear(year))
# def function_oddevencheck(num):
#     if(num%2==0):
#         return "even"
#     else:
#         return "odd"
# check = int(input("enter the no."))
# print(function_oddevencheck(check))
#  python claude.py
# def function_addsum(n):
#     sum = 0 
#     for i in range (1,n+1):
#         sum +=i
#     return sum 
# check = int(input("no."))
# print(function_addsum(check))
# def function_printlist(lst):
#     for i in lst:
#         print(i)

    
# mylist = [1,2,3,4,5]
# print(function_printlist(mylist))
# def function_listsum(lst):
#     sum = 0

#     for i in lst:
#         if(i%2==0):
#             sum+=i
#     return sum
# mylist = [1,2,3,4,5,6]
# print(function_listsum(mylist))

# def function_maxm(n):
#     new = n[0]
#     for i in n :
#         if(i>new):
#             new = i 
#     return new
# print(function_maxm([3, 7, 2, 9, 5]))
# print(function_maxm([-5, -2, -8]))
            
# def function_minm(lst):
#     new = lst[0]
#     for i in lst:
#         if(i<new):
#             new = i
#     return new

# def function_count(lst,target):
#     count = 0
#     for i in lst:
#         if(i==target):
#             count+=1
#     return count

# print(function_count([1, 2, 3, 2, 2, 4], 2))
#  python claude.py

# def function_reverse(lst):
#     mylist = []
#     for i in range(len(lst)-1,-1,-1):
#         mylist.append(lst[i])
#     return mylist 

# range(len(lst)-1, -1, -1) for a list of 5 items:

# len(lst)-1 = 4 (last index)
# -1 = stop before -1 (so stop at 0)
# -1 = go backwards by 1
# python claude.py
# def function_maxm(lst):
#     min_val = lst[0]
#     for i in lst:
#         if(min_val>i):
#             min_val = i
#     return min_val
# mylist1 = [5, 2, 8, 1, 9]
# print(function_maxm(mylist1))
# def function_countocc(lst,target):
#     count =0
#     for i in lst:
#         if(i==target):
#             count += 1
#     return count
# print(function_countocc([1, 2, 3, 2, 2, 4], 2))

# def function_primeornot(num):
#     if(num<2):
#         return False
#     for i in range(2,num-1):
#         if(num%i==0):
#             return False
#     else:
#         return True
# print(function_primeornot(2))

# Python ranges exclude the end value.
 
# def function_fibonacci(n):
#     a,b =1,1
#     for i in range(n-1):
#         a,b=b,a+b
#     return a
# print(function_fibonacci(7))

# def function_reverse(lst):
#     mylist = []
#     for i in lst:
#         mylist.insert(0,i)
#     return mylist



# def function_rev(str):
#     str1 = ""
#     for i in str:
#         str1 = i + str1
#     return str1
# print(function_rev("hello"))


# def function_reverselist(lst):
#     mylist = []
#     for i in lst:
#         mylist.insert(0,i)
#     return mylist

# def function_primeornot(n):
#     if(n<=1):
#         return False
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#     return True


# def function_fibonacci(n):
    # a,b = 1,1
    # for i in range(n-1):
        # a,b = b,b+a
    # return a
# # 
# def function_sumofdig(n):
#     new_dig = 0
#     while(n>0):
#         new_dig = (n%10)+new_dig
#         n= n//10
    
#     return new_dig

# print(function_sumofdig(123))
# print(function_sumofdig(456))
# print(function_sumofdig(0))

# def function_countno(n):
#     count = 0
#     if(n==0):
#         return 1
#     while(n>0):
        
#         n= n//10
#         count += 1
    
#     return count

# print(function_countno(123))
# print(function_countno(7))
# print(function_countno(10000))
# print(function_countno(0))

# def function_reverseno(n):
#     rev = 0 
#     while(n>0):
#         rev= (n%10)+ rev*10
#         n=n//10
#     return rev
# print(function_reverseno(123))
# print(function_reverseno(500))
# print(function_reverseno(7))
# print(function_reverseno(0))

# def function_palindrome(n):
#     rev = 0 
#     original = n
#     while(n>0):
#         rev= (n%10)+ rev*10
#         n=n//10
#     return (original==rev)
        
# print(function_palindrome(121))
# print(function_palindrome(123))
# print(function_palindrome(1))
# print(function_palindrome(1221))

# def function_gcd(n1,n2):
#     while(n1!= 0,n2 !=0):
#         if(n1>n2):
#             n1=n1%n2
#         else:
#             n2=n2%n1
#         if(n2==0):
#             return n1
#         return n2


# def function_gcd(n1,n2):
    
#     for i in range (min(n1,n2),0,-1):
#         if(n1%i==0 and n2%i ==0):
#            return i

# print(function_gcd(12, 8))
# print(function_gcd(15, 5))
# print(function_gcd(7, 3))

# def function_lcm(n1,n2):
#     great = max(n1,n2)
#     while(True):
#         if(great%n1 == 0 and great%n2 == 0):
#             return great
#         great+=1
# print(function_lcm(4, 6))
# print(function_lcm(3, 5))
# print(function_lcm(2, 8))
    

# def function_gcd(n1,n2):
#     for i in range (min(n1,n2),0,-1):
#         if(n1%i==0 and n2%i==0):
#             return i
# print(function_gcd(12, 8))
# print(function_gcd(15, 5))
# print(function_gcd(7, 3))

# def function_lcm(n1,n2):
#     greatest = max(n1,n2)
#     while(True):
#         if(greatest%n1==0 and greatest%n2==0):
#             return greatest
#         greatest += 1
# print(function_lcm(4, 6))
# print(function_lcm(3, 5))
# print(function_lcm(2, 8))

# def function_factorial(n):
#     fact = 1
#     for i in range (1,n+1):
#         fact = fact*i
#     return fact
# print(function_factorial(5))
# print(function_factorial(1))
# print(function_factorial(0))

# def function_power(n1,n2):
#     pow =1
#     while(n2>0):
#         pow = pow*n1
#         n2= n2-1
#     return pow
# print(function_power(2, 3))
# print(function_power(5, 2))
# print(function_power(3, 0))



# def function_lcm(n1,n2):
#     great = max(n1,n2)
#     while(True):
#         if(great % n1 ==0 and great%n2 == 0):
#             return great
#         great+=1
    

# def function_factorial(n):
#     fact = 1
#     for i  in range(1,n+1):
#         fact = fact*i
#     return fact

# def function_power(n1,n2):
#     no = 1
#     while(n2>0):
#         no = no*n1
#         n2 = n2-1
#     return no

# def function_armstrong(n):
#     no = 0    
#     org = n
#     killme = n
#     count = 0
#     while(n>0):
#         count +=1
#         n=n//10
#     while(org>0):
#         no = no+ pow(org%10,count)
#         org= org//10
#     if(no==killme):
#         return True
#     else:
#         return False

# print(function_armstrong(153))
# print(function_armstrong(9474))
# print(function_armstrong(123))

# def function_power(n1,n2):
#     pow = 1 
#     while(n2>0):
#         pow = pow*n1
#         n2-=1
#     return pow
# print(function_power(2, 3))
# print(function_power(5, 2))
# print(function_power(3, 0))

# def function_armstrong(n):
#   count =0
#   no=0
#   org = n
#   final = n
#   while(n>0):
#     count+=1
#     n=n//10
#   while(org>0):
#     no = no+ pow(org%10,count)
#     org=org//10
#   if(no==final):
#     return True
#   else:
#    return False
# print(function_armstrong(153))
# print(function_armstrong(9474))
# print(function_armstrong(123))

# def function_perfect(n):
    
#     sum = 0
#     for i in range(1,n):
#         if(n%i==0):
#             sum+=i
#     return(sum==n)
# print(function_perfect(6))
# print(function_perfect(28))
# print(function_perfect(12))
# def factorial(n):
#     no = 1
#     for i in range (1,n+1):
#         no = no*i
#     return no

# def function_strong(n):
#     sum = n
#     dig = 0
#     while(n>0):
#         dig = dig+ factorial(n%10)
#         n=n//10
#     return(sum==dig)
# print(function_strong(145))
# print(function_strong(123))

# def neon(n):
#     sum = pow(n,2)
#     dig =0
#     while(sum>0):
#         dig = dig + sum%10
#         sum=sum//10
#     return(n==dig)
# print(neon(9))
# print(neon(7))
# print(neon(1))
# def count(n):
#     cou = 0
#     while(n>0):
#         cou+=1
#         n=n//10
#     return cou
# def automorph(n):
#     sum = pow(n,2)
#     dig = sum%(10**count(n))
#     return (n==dig)
# print(automorph(5))
# print(automorph(25))
# print(automorph(7))
# print(automorph(376))

# def extract(n):
#     dig = 0 
    
#     while(n>0):
#         dig = dig + n%10
#         n=n//10
#     return dig
# def harshad(n):
#     sum = n
#     return(sum%extract(n)==0)
# print(harshad(18))
# print(harshad(21))
# print(harshad(14))
# def count(n):
#     cou = 0
#     while(n>0):
#         cou+=1
#         n=n//10
#     return cou
# def disarium(n):
#     dig = 0
#     org = n
#     while(n>0):
#         dig = dig + pow(n%10,count(n))
#         n=n//10
#     return(dig==org)
# print(disarium(135))
# print(disarium(89))
# print(disarium(123))

2