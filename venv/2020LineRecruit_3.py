# k 번째 순열 찾기

# import itertools
from itertools import permutations

# num = list(map(int, input().split()))
# num = ['1', '0', '2']
num = list(input().split())
print(num)
k = int(input())

sorted_list = sorted(list(map(''.join, permutations(num))))
print(sorted_list)

result = sorted_list[k - 1]
print(result)


# print(list(map(int, map(''.join, permutations(num)))))
# print(list(map(lambda x: int(x), list(map(''.join, permutations(num))))))


'''
입력
1 0 2
5
출력
201

Test Case
0 1 2
3
'''
