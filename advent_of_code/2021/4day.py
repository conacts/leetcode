import numpy as np
nums = [23,30,70,61,79,49,19,37,64,48,72,34,69,53,15,74,89,38,46,36,28,32,45,2,39,58,11,62,97,40,14,87,96,94,91,92,80,99,6,31,57,98,65,10,33,63,42,17,47,66,26,22,73,27,7,0,55,8,56,29,86,25,4,12,51,60,35,50,5,75,95,44,16,93,21,3,24,52,77,76,43,41,9,84,67,71,83,88,59,68,85,82,1,18,13,78,20,90,81,54]

def q1():
    l = []
    def createBoards():
        with open('4day.txt') as f:
            i, x = 0, 0
            lines = f.read().splitlines()
            tmp = []
            for line in range(len(lines)):
                add = lines[line].split()
                if not lines[line]:
                    l.append('')
                    l[i] = np.array(tmp)
                    tmp = []
                    i += 1
                else:
                    tmp.append(add)
        return np.where(l[0] == 22)


    def updateBoards():
        pass

    def checkWinners():
        pass

    return createBoards()

print(q1())
