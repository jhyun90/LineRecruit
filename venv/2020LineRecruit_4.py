
n = int(input())

seats = list(map(int, input().split()))
# print(seats)

dist_from_left = 0
dist_from_right = 0
dis_list = []

for i in range(len(seats)):
    if seats[i] == 0:
        # left -> seat[:i]
        stack = []

        for seat in reversed(seats[:i]):
            stack.append(seat)

        # print("stack", stack)

        idx = []
        for j in range(len(stack)):
            if stack[j] == 1:
                # print("idx", j)
                idx.append(j)

        dist_from_left = min(idx) + 1

        # print("dist from left", dist_from_left)

        # right -> seat[i:]
        stack = []

        for seat in seats[i + 1:]:
            stack.append(seat)

        # print("stack", stack)

        idx = []
        for j in range(len(stack)):
            if stack[j] == 1:
                # print("idx", j)
                idx.append(j)

        dist_from_right = min(idx) + 1

        # print("dist from right", dist_from_right, '\n')

        if dist_from_left == dist_from_right:

            dis = dist_from_right
            # print("dis", dis)

            dis_list.append(dis)
            # print(dis_list)

        else:
            if dist_from_left < dist_from_right:
                dis = dist_from_left
            elif dist_from_right < dist_from_left:
                dis = dist_from_right

            dis_list.append(dis)

print(max(dis_list))

'''
7
1 0 1 0 0 0 1
7
1 1 0 0 0 1 1
4
1 0 0 1
5
1 0 1 0 1
'''
