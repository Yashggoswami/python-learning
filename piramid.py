num1 = int(input())

def piramid(num1=0):
    if num1 == 0:
        return
    for i in reversed(range(1,num1+1)):
       print("*"*(i))
    
piramid(num1=num1)
    
