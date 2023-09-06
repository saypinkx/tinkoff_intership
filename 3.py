n = int(input())
a = str(input()).split()
a = list(map(lambda x: int(x), a))
b = str(input()).split()
b = list(map(lambda x: int(x), b))
left = None
right = -1
for i in range(n):
    if a[i] != b[i]:
        if left is None:
            left = i
        else:
            if i > right:
                right = i
new_a = a[left:right + 1]
new_b = b[left:right + 1]
new_a = sorted(new_a)
if new_a == new_b:
    print('YES')
else:
    print('NO')
