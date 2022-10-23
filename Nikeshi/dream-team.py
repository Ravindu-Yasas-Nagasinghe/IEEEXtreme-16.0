budget= int(input())
aa=int(input())
a_name=[]
A=[]
for i in range(aa):
    x,y= input().split()
    a_name.append(x)
    A.append(int(y))
bb=int(input())
b_name=[]
B=[]
for i in range(bb):
    x,y= input().split()
    b_name.append(x)
    B.append(int(y))
cc=int(input())
c_name=[]
C=[]
for i in range(cc):
    x,y= input().split()
    c_name.append(x)
    C.append(int(y))
dd=int(input())
d_name=[]
D=[]
for i in range(dd):
    x,y= input().split()
    d_name.append(x)
    D.append(int(y))
ee=int(input())
e_name=[]
E=[]
for i in range(ee):
    x,y= input().split()
    e_name.append(x)
    E.append(int(y))

solutions = [(x1,x2,x3,x4,x5) for x1 in A for x2 in B for x3 in C for x4 in D for x5 in E if sum([x1,x2,x3,x4,x5]) <= budget]
an=list(map(sum, solutions))
max_value = max(an)
max_index = an.index(max_value)
answer=solutions[max_index]

print(a_name[A.index(answer[0])])
print(b_name[B.index(answer[1])])
print(c_name[C.index(answer[2])])
print(d_name[D.index(answer[3])])
print(e_name[E.index(answer[4])])
