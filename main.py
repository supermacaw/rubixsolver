
def parse(filename = "cube.txt"):
    f = open(filename, 'r')
    lines = []
    for line in f:
        line = line.strip().split(",")
        lines.append([l.strip() for l in line])
    return lines

print parse()
