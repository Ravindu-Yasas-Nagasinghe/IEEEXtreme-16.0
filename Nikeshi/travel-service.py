t=int(input())
for i in range(t):
    s,c,r=map(int, input().split()) 
    cost=c*r
    tem=c
    d=[]
    p=[]
    for k in range(s):
        f,x=map(int, input().split())
        d.append(f)
        p.append(x)
    for k in range(s-1):
        tem=tem-d[k]
        if (tem<d[k+1]):
            if p[k]>p[k+1]:
                a=c-tem
                tem=c
                cost=cost+500+a*p[k]
            else:
                a=c-tem
                tem=c
                cost=cost+500+a*p[k]
        else:
            if p[k]<p[k+1]:
                a=c-tem
                tem=c
                cost=cost+500+a*p[k]  
print(cost)
