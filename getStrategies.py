import matplotlib.pyplot as plt
import numpy as np

MAX = 36

def progressBar(curr, end):
    prog = round(curr/end * 10)
    bar = "|" + "=" * prog + ">" + "." * (10-prog) + "|"
    print(f'Working on it... {bar}', end='\r')
    return

def getFactors():
    factors = [ factorize(x) for x in range(2,MAX) ]
    return [0, 0] + factors # This fixes the indices so that factors[54] refers to the factors of 54 e.g. :)

# Get prime factors of a number. For example 30 yields [2,3,5]
def factorize(x): 
    if x % 2 == 0:
        if x == 2:
            return [2]
        else:
            return [2] + factorize(x//2)
    i = 3;
    while i*i <= x:
        if x % i == 0:
            return [i] + factorize(x//i)
        i += 2
    return [x]

def findProbability(factors, have, goal):
    probability = 1
    goalFactors = factors[goal]
    haveFactors = factors[have]
    haveSet = set(haveFactors)
    for factor in goalFactors:
        factorOffBy = 0
        while not set(factors[factor + factorOffBy]) <= haveSet:
            if factor + factorOffBy < MAX - 1:
                factorOffBy += 1
            else:
                break # THIS MIGHT CAUSE TROUBLE WHEN IT COMES TO PROBAIBILIES
        probability *= factor/(factor+factorOffBy)
    return probability

if __name__ =="__main__":

    factors = getFactors()

    xs = ys = np.arange(2, MAX, 1)
    X, Y = np.meshgrid(xs, ys)

    zs = np.array([])
    for have in xs:
        probs = []
        for goal in ys:
            zs = np.append(zs, findProbability(factors, have, goal))
        progressBar(have, MAX)
    Z = zs.reshape(X.shape)

    ax = plt.axes(projection = "3d")
    ax.plot_surface(X, Y, Z)
    plt.show()
