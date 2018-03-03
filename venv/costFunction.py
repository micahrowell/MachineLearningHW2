import numpy as npy

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
    J = 0
    grad = [0] * len(theta)
    for i in range(m):
        hyp_theta = hyp(theta,x[i])
        J -= y[i] * npy.log10(hyp_theta) + (1 - y[i]) * npy.log10(1 - hyp_theta)
    J /= m
    return J, grad

def hyp(theta,x):
    e = 2.718281828459
    exponent = 0
    for j in range(len(theta)):
        exponent -= theta[j] * x[j]
    return 1/(1 + e**exponent)
