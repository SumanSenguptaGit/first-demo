import time

x = int(input('choose a num: '))

for i in range(1, 11):
    print(x, 'x', i, '=', x*i)

time.leep(2)
print('success')

