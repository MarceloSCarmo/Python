from time import sleep

n = 10

for x in range(n):
    x += 1
    print(x, end=" ", flush=True)
    #sleep(1)

print()

count = 1

while count <= n:
    print(n, end=" ", flush=True)
    #sleep(1)
    n -= 1


    