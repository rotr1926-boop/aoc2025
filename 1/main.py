with open('input.txt', 'r') as f:
    data = f.read().strip().split()

start = 50 
zero_c = 0

for x in data:
    direction = x[0]
    distance = int(x[1:])

    if direction == 'L':
        start -= distance
    else:  
        start += distance

    start %= 100

    if start == 0:
        zero_c += 1

print(zero_c)

start = 50 
zero_c = 0

for x in data:
    direction = x[0]
    distance = int(x[1:])

    if direction == 'R':
        step = 1
    else:
        step = -1

    for _ in range(distance):
        start = (start + step) % 100 
        if start == 0:
            zero_c += 1

print(zero_c)
