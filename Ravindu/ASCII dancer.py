T = int(input())
for i in range(T):
    d = int(input())
    arr = [[' ', 'o',' '],['/','|','\\'],['/',' ','\\']]
    cmnds=["left hand to head","left hand to hip","left hand to start","left leg in",
    "left leg out","right hand to head","right hand to hip",
    "right hand to start","right leg in","right leg out","turn"]
    turncount = 0
    forwrd = True
    for c in range(d):
        comnd = input().strip()
        if comnd[0]=='s':
            print(comnd[4::])
            continue
        val = cmnds.index(comnd)
        if val == len(cmnds)-1:
            t1 = arr[0][0]
            t2 = arr[1][0]
            t3 = arr[2][0]
            t4= arr[0][2]
            t5 = arr[1][2]
            t6 = arr[2][2]
            
            if t1 == '(':
                t1 = ')'
            if t2 == '<':
                t2 = '>'
            if t2 == '/':
                t2 = '\\'
            if t3 == '/':
                t3 = '\\'
            if t3 == '<':
                t3 = '>'
            
            if t4 == ')':
                t4 = '('
            if t5 == '>':
                t5 = '<'
            if t5 == '\\':
                t5 = '/'
            if t6 == '\\':
                t6 = '/'
            if t6 == '>':
                t6 = '<'
            
            arr[0][0] = t4
            arr[1][0] = t5
            arr[2][0] = t6
            arr[0][2] = t1
            arr[1][2] = t2
            arr[2][2] = t3
            turncount+=1
            if turncount%2 ==1:
                forwrd = False
            else:
                forwrd = True
        if forwrd == False:
            if val==5:
                arr[0][2] = ')'
                arr[1][2] = ' '
            elif val ==6:
                arr[1][2] = '>'
                arr[0][2] = ' '
            elif val ==7:
                arr[1][2] = '\\'
                arr[0][2] = ' '
            elif val ==8:
                arr[2][2] = '>'
            elif val ==9:
                arr[2][2] = '\\'
            elif val ==0:
                arr[0][0] = '('
                arr[1][0] = ' '
            elif val ==1:
                arr[1][0] = '<'
                arr[0][0] = ' '
            elif val ==2:
                arr[1][0] = '/'
                arr[0][0] = ' '
            elif val ==3:
                arr[2][0] = '<'
            elif val ==4:
                arr[2][0] = '/'
        else:
            if val==0:
                arr[0][2] = ')'
                arr[1][2] = ' '
            elif val ==1:
                arr[1][2] = '>'
                arr[0][2] = ' '
            elif val ==2:
                arr[1][2] = '\\'
                arr[0][2] = ' '
            elif val ==3:
                arr[2][2] = '>'
            elif val ==4:
                arr[2][2] = '\\'
            elif val ==5:
                arr[0][0] = '('
                arr[1][0] = ' '
            elif val ==6:
                arr[1][0] = '<'
                arr[0][0] = ' '
            elif val ==7:
                arr[1][0] = '/'
                arr[0][0] = ' '
            elif val ==8:
                arr[2][0] = '<'
            elif val ==9:
                arr[2][0] = '/'
        for i in arr:
            line=''
            for j in i:
                line+=j
            print(line)
    
