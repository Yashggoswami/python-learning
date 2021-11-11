
def z_algorithm(s):
    size = len(s)
    l = r = 0
    z = [0 for i in range(size)]
    for i in range(1,size):
        if i>r:
            l = r = i
            while r<size and s[r] == s[r-l]:
                r += 1
            z[i] = r-l
            r -=1
        else:
            index = i - l
            if i + z[index] >= r:
                l  = i
                while r<size and s[r] == s[r-l]:
                    r += 1
                z[i] = r-l
                r -= 1
            else:
                z[i] = z[index]
    return z
            
            
def find(s1,s2):
    count = 0
    i = 0
    while i<len(s1) and i<len(s2) and s1[i] == s2[i]:
        count += 1
        i += 1
    return count
if __name__ == '__main__':
    s = input()
    t = z_algorithm(s)
    tc = int(input())
    while tc>0:
        n = int(input())
        if n>t[n]:
            print(t[n])
        else:
            print(n)
        tc -= 1