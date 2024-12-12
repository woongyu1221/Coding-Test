a = int(input())

n = [1 for i in range(1000001)]
answer = []
for i in range(2,1000001):
    if n[i] != 0:
        for j in range(i+i,1000001,i):
            n[j] = 0

def gold(num):
    count = 0
    for i in range(2,num//2+1):
        if n[i] and n[num-i]:
            count += 1
    return count

for i in range(a):
    num = int(input())
    answer.append(gold(num))

for i in answer:
    print(i)