num1 = int(input())

def piramid(num1=0):
    if num1 == 0:
        return
    for i in range(num1,0,-1):
       print("*"*(i))
    
piramid(num1=num1)
    
