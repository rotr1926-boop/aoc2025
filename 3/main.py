with open('input.txt', 'r') as f:
    file = f.readlines()

    numbers = []
    for x in file:
        numbers.append([int(xx) for xx in x.strip()])

s = 0

for x in numbers:
    if not x: break
    z = max(x[:-1])
    z_index = x.index(z)

    y = max(x[z_index + 1:])

    s += (z * 10) + y

print(s)
