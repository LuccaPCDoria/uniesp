import time

span = 0
while span < 100:
    print(f'O valor de span é {span}')
    time.sleep(1)
    span = span + 1

# x = 0
for x in range(10):
    print(f'Jimmy Fives Times({x})')
#
for x in range(1, 10, 2): #range(início, Final, Step ou pulo)
    print(f'olá {x}')