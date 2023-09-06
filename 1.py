n, s = str(input()).split()
n = int(n)
s = int(s)
costs = str(input()).split()
costs = list(map(lambda x: int(x), costs))
costs = sorted(costs)
left = 0
right = n - 1

if s >= costs[0]:
    while left < right:
        median = (left + right + 1) // 2
        if s >= costs[median]:
            left = median
        else:
            right = median - 1
    print(costs[left])
else:
    print(0)
