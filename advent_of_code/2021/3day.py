def q1():
    with open('3day.txt') as f:
        lines = f.read().splitlines()
        
        l = [[] for i in range(len(lines[0]))]
        for j in range(len(lines)):
            for x in range(len(lines[j])):
                l[x] += lines[j][x]

        gamma = ''
        epsilon = ''
        for col in range(len(l)):
            zeros = l[col].count('0')
            if zeros > 500:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'
        
        gamma = int(gamma, 2)
        epsilon = int(epsilon, 2)
        return gamma * epsilon
            
def q2():
    with open('3day.txt') as f:
        lines = f.read().splitlines()

        '''
        l = []
        for line in lines:
            l.append(line.split())

        scrubber = ''
        count = 0
        generator = ''
        for i in range(len(l[0])):
            for j in range(len(l)):
                if int(j) == 0:
                    count -= 1
                else:
                    count += 1
            if count >= 0:
                scrubber += '1'
                generator += '0'
        '''
