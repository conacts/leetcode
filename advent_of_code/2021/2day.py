d = {'forward':1, 'backward':-1, 'up':1, 'down':-1}

def game1(file='2day.txt'):
    with open(file) as f:
        h = 0
        v = 0
        lines = f.read().splitlines()
        for line in lines:
            if line[0] == 'f':
                h += int(line[-1])
            elif line[0] == 'b':
                h -= int(line[-1])
            elif line[0] == 'u':
                v -= int(line[-1])
            elif line[0] == 'd':
                v += int(line[-1])

        return v * h

def game2(file='2day.txt'):
    with open(file) as f:
        h = 0
        v = 0
        aim = 0
        lines = f.read().splitlines()
        for line in lines:
            if line[0] == 'f':
                num = int(line[-1])
                h += num
                v += aim * num
            elif line[0] == 'b':
                num = int(line[-1])
                h -= num
                v += aim * num
            elif line[0] == 'u':
                aim -= int(line[-1])
            elif line[0] == 'd':
                aim += int(line[-1])

        return v * h

print(game2())
