import sympy


def isHappyNumber(num):    
    rem = sum = 0;    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
        
def write_data_into_file():
    file1 = open('first.txt', 'w')
    file2 = open('second.txt', 'w')

    l1 = list(map(str, sympy.primerange(0, 1000)))
    file1.write(' '.join(l1))
    file1.close()

    l2 = []
    for i in range(1,1000):
        result = i;    
     
        while(result != 1 and result != 4):    
            result = isHappyNumber(result);    
            
        #Happy number always ends with 1    
        if(result == 1):    
            l2.append(str(i))    
        
            
    file2.write(' '.join(l2))

    file2.close()


def read_and_calculate_overlapping():
    file1 = open('first.txt','r')
    file2 = open('second.txt','r')
    l1 = set(map(int,file1.readline().split()))
    l2 = set(map(int,file2.readline().split()))
    return l1.intersection(l2)
      
if __name__ == "__main__":
    result = read_and_calculate_overlapping()
    print(result)
    