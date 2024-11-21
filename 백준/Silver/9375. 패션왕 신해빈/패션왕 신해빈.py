import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    c = int(input())
    closet = {}
    result = 1
    
    for i in range(c):
        name, cat = input().split()
        if cat not in closet:
            closet[cat] = 1
        else:
            closet[cat] += 1

    for v in closet.values():
        v += 1
        result = result * v

    print(result-1)