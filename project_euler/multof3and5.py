import math
# naive solution  ---> O(N)
def threefivesum(n):
    s = 0
    for i in range(n):
        if i % 3 == 0:
            s += i
        elif i % 5 == 0:
            s += i
    print(s)

# Optimized Algorithm ----> O(1)

def threefivesum2(n):
    three = math.floor(n / 3)
    five = math.floor(n / 5)
    ft = math.floor(n / 15)

    three = 3 * three * (three + 1)
    five = 5 * five * (five + 1)
    ft = 15 * ft * (ft + 1)
    print(int(.5 * (three + five - ft)))

threefivesum2(1000)
