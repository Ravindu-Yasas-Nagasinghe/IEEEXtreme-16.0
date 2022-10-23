T=int(input())
for k in range(T):
    M=int(input())
    # a={'Alice':0, 'Bob':0,'Chuck':0,'Dave':0,'Eve':0}
    # b={'Alice':0, 'Bob':0,'Chuck':0,'Dave':0,'Eve':0}
    a={}
    b={}
    c=[]
    d=[]
    for j in range(M):
        input_string=input()
        s = input_string.split()
        l = int(s[1])
        if s[0] not in a.keys():
            a[s[0]] = 0
        if s[0] not in b.keys():
            b[s[0]] = 0
        a[s[0]]=a.get(s[0])+int(s[1])
        for i in range(2,l+2):
            if s[i] not in b.keys():
                b[s[i]] = 0
            elif s[i] not in a.keys():
                a[s[i]] = 0
            b[s[i]]=b.get(s[i])+1
    # print(a,b)
    for i in a:
        if (a.get(i) > b.get(i)):
            p=(a.get(i)-b.get(i))
            c.append(p)
        elif (a.get(i) < b.get(i)):
            q=(b.get(i)-a.get(i))
            d.append(q)
    print(sum(c),max(c))

