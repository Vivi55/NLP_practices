#steven 01/03/2020
#calculate pi using random method. (Monte Carlo method)
import numpy as np 
import matplotlib.pyplot as plt

def fun(x):
    #y=x+1
    return x**2
    #return np.sin(x)

def integral(N):
    s = 0
    for i in range(N):
        x=1/N
        y = fun(i/N)
        s += x*y
    return s

def randomSeries(N):
    """generate series number between 0~1"""
    return np.random.rand(N)
   
def distance(a, b):
    """calculate the distence from point(a,b) to point(0,0)"""
    return np.sqrt(a**2 + b**2)
    #return np.power(a**2 + b**2,0.5)

def plotFuc(x_data,y_data):
    _,ax =plt.subplots()
    ax.plot(x_data, y_data, lw=2, color='#539caf', alpha=1)
    ax.set_title('')
    #ax.set_xlabel(x_label)
    #ax.set_ylabel(y_label)
    pass

def plotXY(x,y):
    plt.figure(num='Calculate Pi')
    ax = plt.gca()
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    for a,b in zip(x,y):
        if distance(a, b) > 1:
            ax.scatter(a, b, c='r', s=5, alpha=0.5)
        else:
            ax.scatter(a, b, c='b', s=5, alpha=0.5)

    plt.show()
def showFuc():
    x = np.linspace(-5,5,100)
    print(x)
    y = fun(x)
    plt.show(plotFuc(x,y))
    pass

def main():
    return showFuc()

    N = 10  #samples
    x = randomSeries(N)
    y = randomSeries(N)

    print(x)
    print(y)

    print(distance(x,y))

    res = np.where(distance(x,y) > 1, 0, 1)
    print(res)
    
    pi = np.sum(res)*4.0/len(res)
    print(pi)
    
    plotXY(x,y)

if __name__ == "__main__":
    main()
ef randomSeries(N):
    return np.random.rand(N)

def fun():
    if x_data>o.5:


def lineplot (x_data, y_data, x_label="", y_label="", title=""):
    _,ax =plt.subplots()
    ax.plot(x_data, y_data, lw=2, color='#539caf', alpha=1)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
plt.show(lineplot(x_data, y_data, x_label= 'x_label', y_label="y_label", title="title"))

def plotXY(x,y):
    plt.figure(num='toss coin')
    ax = plt.gca()
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    for a in zip(x,y):
        if a > 0.5:
            ax.scatter(a, b, c='r', s=5, alpha=0.5)
        else:
            ax.scatter(a, b, c='b', s=5, alpha=0.5)

def main():
    N = 100  #samples
    x = randomSeries(N)
    toss = all[random.randint(0,1)]
    print(res)


if __name__ == "__main__":

