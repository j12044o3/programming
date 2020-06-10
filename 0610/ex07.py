import sys

max = -sys.maxsize -1
min = sys.maxsize

num = [8, 7, 3, 2, 9, 4, 1, 6, 5]

for i in num:
    if max < i:
        max = i
    if min > i:
        min = i
print("최댓값 :",max)
print("최솟값 :",min)
