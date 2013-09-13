f = open('cube.txt', 'r')
lines = []
for line in f:
    lines.append(line.split(","))
print lines
