import matplotlib.pyplot as plt
from costFunction import *

data = open('ex2data1.txt','r')
x = []
y = []

for line in data:
    line = line.strip('\n')
    line = line.split(',')
    arr = [1.0]
    for i in range(len(line)):
        if i != len(line) - 1:
            arr.append(float(line[i]))
        else:
            y.append(float(line[i]))
    x.append(arr)
    del arr

x = npy.array(x)
y = npy.array(y)

print 'Plotting data with + indicating (y = 1) examples and o indicating (y = 0) examples.'
print '\nProgram paused. Exit plot to continue...'

plt.plot(x,y,'r+')
plt.xlabel('Exam 1 score')
plt.ylabel('Exam 2 score')
#plt.show()

m = len(x)
n = len(x[0]) - 1
theta = [0.0] * (n+1)
theta = npy.array(theta)

#'''
cost,grad = costFunction(theta,x,y)

print '\nCost at initial theta: ' + str(cost)
print 'Expected cost (approx): 0.693'
print 'Gradient at initial theta: ' + str(grad)
print 'Expected gradients (approx): [-0.1, -12.0092, -11.2628]'
#'''

theta = [-24.0, 0.2, 0.2]

cost,grad = costFunction(theta,x,y)

print '\nCost at test theta: ' + str(cost)
print 'Expected cost (approx): 0.218'
print 'Gradient at test theta: ' + str(grad)
print 'Expected gradients (approx): [0.043, 2.566, 2.647]'

#print '\nProgram paused. Press enter to continue.'
#wait = raw_input()
