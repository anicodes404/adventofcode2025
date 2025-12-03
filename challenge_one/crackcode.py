def count_zero_hits(lines):
    pos = 50
    hits = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        n = int(line[1:])
        if direction == 'R':
            pos = (pos + n) % 100
        else:
            pos = (pos - n) % 100
        if pos == 0:
            hits += 1
    return hits

with open("input.txt", "r") as file: 
    line = file.readlines()

answer = count_zero_hits(line)
print(answer)  
