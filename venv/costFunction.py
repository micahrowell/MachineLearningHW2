import numpy as npy
from sigmoid import *

'''
COSTFUNCTION Compute cost and gradient for logistic regression
   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
   parameter for logistic regression and the gradient of the cost
   w.r.t. to the parameters.
'''

def costFunction(theta,x,y):
    '''
    Instructions: Compute the cost of a particular choice of theta.
                  You should set J to the cost.
                  Compute the partial derivatives and set grad to the partial
                  derivatives of the cost w.r.t. each parameter in theta
    '''
    m = len(y)
    n = len(x[0])
    J = 0
    grad = [0] * len(theta)

    for i in range(m):
        hyp_theta = sigmoid(theta,x[i])
        J -= y[i] * npy.log(hyp_theta) + (1 - y[i]) * npy.log(1 - hyp_theta)

        for j in range(n):  # partial derivative
            grad[j] -= y[i] * x[i][j] - x[i][j] * hyp_theta

    for k in range(n):
        grad[k] /= m
    J /= m
    return J, grad
