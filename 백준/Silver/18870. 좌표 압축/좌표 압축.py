N = int(input())
num = list(map(int, input().split()))

num2 = sorted(list(set(num)))
dic = {num2[i] : i for i in range(len(num2))}

for n in num:
    print(dic[n], end = ' ')