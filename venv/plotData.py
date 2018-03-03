import matplotlib.pyplot as plt

def plotData(x,y):
    plt.plot(x, y, 'r+')
    plt.xlabel('Exam 1 score')
    plt.ylabel('Exam 2 score')
    plt.show()