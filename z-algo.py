
def zAlgo(s):
    size = len(s)
    z = list(0 for i in range(size))
    
    l = r = 0
    for i in range(1, size):
        if i > r:
            l = r = i
            while r < size and s[r] == s[r-l]:
                r += 1
            z[i] = r-l
            r -= 1
        else:
            index = i-l
            if i + z[index] >= r:
                l = i
                while r < size and s[r] == s[r-l]:
                    r += 1
                z[i] = r-l
                r -= 1
            else:
                z[i] = z[index]
    return z


if __name__ == '__main__':
    print('enter the string and pattern of the string')
    st, pat = input().split()
    total = pat+'$'+st
    ar = zAlgo(total)
    print(ar)
