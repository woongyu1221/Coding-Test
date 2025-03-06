n = int(input())
day = []

for i in range(n):
    day.append(list(map(int, input().split())))
day.sort(key=lambda x:(-x[1],x[0]))

ans = [0] * max(day)[0]
for d, point in day:
    if ans[d-1] == 0:
        ans[d-1] = point
    else:
        for i in range(1,d):
            if ans[d - 1 - i] == 0:
                ans[d - 1 - i] = point
                break
print(sum(ans))