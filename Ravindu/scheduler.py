T = list(map(int,input().split()))
N = T[0]
M = T[1]
arr = list(map(int,input().split()))
Men = [0]*M #list to assign work hours for each man
for i in range(len(arr)):
    arr[i] = 2**arr[i]
arr.sort(reverse=True)
for i in range(N):
    Men.sort()
    Men[0] = Men[0]+arr[i]
Men.sort()
print((Men[-1])%1000000007)
