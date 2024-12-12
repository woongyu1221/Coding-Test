def self_num(n):
    return n + sum(list(map(int,list(str(n)))))

n = [1] * 10001
n[0] = 0
for i in range(1,10001):
    if n[i]:
        num = i
        while True:
            if self_num(num) <= 10000:
                n[self_num(num)] = 0
                num = self_num(num)
            else:
                break
for idx, i in enumerate(n):
    if i:
        print(idx)