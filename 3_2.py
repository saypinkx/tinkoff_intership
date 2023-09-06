n = int(input())
a = str(input()).split()
a = list(map(lambda x: int(x), a))
b = str(input()).split()
b = list(map(lambda x: int(x), b))

left = - 1
right = -1

for i in range(n):
    if a[i] != b[i]:
        left = i
        break
for j in range(n - 1, -1, -1):
    if a[j] != b[j]:
        right = j
        break

if left == -1 and right == -1:
    print('YES')

else:
    if b[left:right + 1] == sorted(a[left:right + 1]):
        print('YES')
    else:
        print('NO')
