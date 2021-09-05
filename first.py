# print("hello, world")

nums = [1,2,3,4,5]
dict = {1:"yash",2:"goswami",3:"vinay",4:"ananya"}
set = {"yash","vinay","vinay","ananaya","chittransha","chirag"}
def show(nums):
    str = "yash goswami"
    
    for s in str:
        print(s+" ",end = " ")
    print()
    for n in nums:
        print(n)
        
# show(nums)

def dictonary(dict):
    
    for n in dict:
        print(n," : ",dict[n])
        
# dictonary(dict)

def setact(set):
    print("the values in set are")
    for n in set:
        print(n," ",end=" ")
    print()

# setact(set)

import random

def printrandom():
    print(*nums)

printrandom()


       
