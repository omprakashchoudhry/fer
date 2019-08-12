y=int(input())
x=list(map(int,input().split()))
sum=0
for i in range(len(x)):
    sum=sum+x[i]
print(sum)
