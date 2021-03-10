#18870
import sys
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
dic = { value : idx for idx, value in enumerate(sorted(list(set(nums))))}
for i in nums:
    print(dic[i], end = ' ')