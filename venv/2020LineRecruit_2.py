
n_messages, n_consumers = map(int, input().strip().split(' '))

consumer = [[] for _ in range(n_consumers)]

stack = []

for i in range(n_messages):
    time = int(input())

    stack.append(time)

    if i < len(consumer):
        consumer[i].append(stack[i])

        # stack[0] -> consumer[0]
        # stack[1] -> consumer[1]

        # stack[2] -> consumer[0] or consumer[1] / or consumer[2]
        # stack[3] -> consumer[0] or consumer[1] / or consumer[2]
        # stack[4] -> consumer[0] or consumer[1] / or consumer[2]

    if i >= len(consumer):
        # print("stack", stack)
        sum_time = []
        for j in range(len(consumer)):
            sum_time.append(sum(consumer[j]))

        # print("sum_time", sum_time)

        if min(sum_time):
            m = min(sum_time)
            # print(sum_time.index(m))
            consumer[sum_time.index(m)].append(stack[i])

if consumer:
    sum_time = []
    for i in range(len(consumer)):
        sum_time.append(sum(consumer[i]))

    # print(sum_time)

    print(max(sum_time))

'''
5 2
4
3
5
2
8
'''
