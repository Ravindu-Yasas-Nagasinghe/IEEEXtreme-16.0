
A = [0, 100, -100, 50, 200]
B = [30, 100, 20, 0]
C = [0, 20, -1, 80]
D = [50, 0, -200, 1]

solutions = [(x1,x2,x3,x4) for x1 in A for x2 in B for x3 in C for x4 in D if sum([x1,x2,x3,x4]) <= 0]
an=list(map(sum, solutions))
print (an)
max_value = max(an)
max_index = an.index(max_value)
answer=solutions[max_index]
print(answer)