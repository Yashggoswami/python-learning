num1 = int(input())
num2 = int(input())

def fun(num1,num2):
    '''this function compare two numbers and return the possible difference'''
    if num1>num2:
        print(num1,"is greater than",num2)
    elif num2>num1:
        print(num2,"is greater than",num1)
    else:
        print(num1," and ",num2," are equal")
    print("yash "*3)
    
fun(num1,num2)
print(fun.__doc__)