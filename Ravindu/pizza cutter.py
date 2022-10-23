# Read the number of testcases
T = int(input())

# Process each test case
for t in range(T):
    ang= list(map(int,input().split()))
    angle=ang[1:]
    answer = 0
    if ang[0]==0:
        answer=1
        print(answer)
        continue
    angle.sort(reverse = True)
    for j in range(0,len(angle)) :
        if(angle[j]>=360):
            angle[j]=(angle[j])%360
        if (angle[j]<=(-360)):
                angle[j]=(angle[j])%(-360)
        if (angle[j]<0):
            if angle[j]>=-180:
                pos = abs(angle[j]+180)
            else:
                pos = abs(angle[j]+360)
            angle[j] = pos
        if (angle[j]>= 180):
            angle[j]=angle[j]+180
            angle[j]=angle[j]%360
    s=set(angle)
    answer= len(s)*2
    # Output your answer
    print(answer)
