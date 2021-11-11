tc = int(input())
while tc>0:
    n = int(input())
    ar = list(int(i) for i in input().split())
    ar.sort()
    mi = ar[0]
    ma = ar[n-1]
    l,r = 0,n-1
    ans = float('inf')
    while l<=r:
        mid = l + (r-l)//2
        left = ar[mid] - mi
        right = ma - ar[mid+1]
        if left == right:
            ans = 0
            break
        elif left>right:
            ans = min(left-right,ans)
            r = mid-1
        else:
            ans = min(right-left,ans)
            l = mid+1
    print(ans)
    tc -= 1





tc = int(input())
while tc>0:
    n = int(input())
    ar = list(int(i) for i in input().split())
    ar.sort()
    if n==2:
        print(0)
        continue
    elif n==3:
        print(min(ar[1]-ar[0],ar[2]-ar[1]))
        continue
    mi = ar[0]
    ma = ar[n-1]
    l,r = 1,n-2
    ans = float('inf')
    ansone = anstwo = 0
    for i in range(n-1):
        ansone += abs(ar[i]-ar[(n-1)//2])
    for i in range(1,n):
        anstwo += abs(ar[i]-ar[1+(n-1)//2])
    ans = min(ansone,anstwo)
    while l<r:
       left,right = ma-ar[l],ar[r]-mi
       ans = min(ans,abs(left-right))
       if(right<left):
           l+=1
       else:
           r-=1
    print(ans)
    tc -= 1
