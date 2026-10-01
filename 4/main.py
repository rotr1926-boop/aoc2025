with open('input.txt', 'r') as f:
    grid = f.read().strip().split('\n')

d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

total = 0
for i_index, row in enumerate(grid):
    for f_index, cell in enumerate(row):
        if cell != '@':
            continue

        c = 0
        for dx, dy in d:
            n_index, n_findex = i_index + dx, f_index + dy

            if 0 <= n_index < len(grid) and 0 <= n_findex < len(grid[n_index]):
                if grid[n_index][n_findex] == '@':
                    c += 1

        if c < 4:
            total += 1

print(total)
