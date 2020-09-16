import numpy as np
import matplotlib.pyplot as plt

def  numpyTests():
    ages = np.random.randint(low=10, high=50, size=5)
    nums = np.arange(12).reshape(12,1)
    return nums* np.array([2,3])


def matplotlibTests():
    plt.rcParams['figure.figsize'] = [10, 7]
    x = np.linspace(0, 2*np.pi, 400)
    y1 = np.tanh(x)
    y2 = np.cos(x**2)
    fig, axes = plt.subplots(1, 2, sharey=True)
    axes[1].plot(x, y1)
    axes[1].plot(x, -y1)
    axes[0].plot(x, y2)
    plt.show()


def runScript():
    #numpyTests()
    return matplotlibTests()


if __name__ == '__main__':
    print(runScript())
