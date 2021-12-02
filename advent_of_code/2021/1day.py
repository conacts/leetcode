# my horrible implementations

def part1(file):
    count = 0
    prev_line = 0
    with open(file) as f:
        out = f.readlines()
        for line in out:
            line = int(line.strip('\n'))
            if prev_line < line:
                count+= 1
            prev_line = line

        return count-1

def part2(file):
    with open(file) as f:
        lines = list(map(int, f.read().splitlines()))
        prev_line = sum(lines[:2])
        count = 0
        s = 3
        while s < len(lines):
            line = sum(lines[s-3:s])
            if prev_line < line:
                count += 1
            s += 1
            prev_line = line

    return count
