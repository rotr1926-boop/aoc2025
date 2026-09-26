import re

with open('input.txt', 'r') as f:
    f = f.read().split(',')
    
r = []
for x in f:
    start, end = [int(p) for p in x.split('-')]
    r.append((start, end))

invalid_ids = 0
for x in range(len(r)):
    for i in range(r[x][0], r[x][1] + 1):
        match = re.search(r'^(\d+)\1$', str(i))
        if match:    
            invalid_ids += i
            print(i)


print(invalid_ids)
