def gcd(a,b):
    while b != 0:
        n = a % b
        a = b
        b = n
    return a

n = int(input())
num = []
diff = []
gap = float("inf") 
count = 0

for i in range(n):
    num.append(int(input()))

for i in range(1,n):
    diff.append(num[i] - num[i-1]) 

for i in diff:
    max_d = max(diff[0],i)
    min_d = min(diff[0],i)
    gap = min(gap, gcd(max_d,min_d))

for i in range(1,len(num)):
    count += (num[i] - num[i-1]) // gap - 1
print(count) 