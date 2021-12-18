from oops import demo

if __name__=='__main__':
    obj2 = demo(100,200)
    # sum function is called
    print(obj2.sum())
    # show function is called
    obj2.show()
    # using class variable directly
    print('outer use of class variable',demo.y)
    # instance variable using reference variable
    print('m and n values are',obj2.m,obj2.n)
    demo.y = 'manish chouhan'
    print(demo.y)
    
    