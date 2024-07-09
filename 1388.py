N,M = map(int,input().split())

graph= []

for i in range(N):
    list1=[]
    a = list(input())
    graph.append(a)
    
count =0

for k in range(N):
    for j in range(M):
        if graph[k][j] == "-":
            if j+1 < M:
                if graph[k][j+1] =="|":
                    count += 1
            else:
                count+=1    
                 
for j in range(M):
    for k in range(N):
        if graph[k][j]=="|":
            if k+1 < N:
                if graph[k+1][j] =="-":
                    count += 1
            else:
                count+=1   
print(count) 