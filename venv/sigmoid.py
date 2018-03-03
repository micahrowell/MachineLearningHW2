def sigmoid(theta,x):
    e = 2.718281828459
    exponent = 0
    for j in range(len(theta)):
        exponent -= theta[j] * x[j]
    return 1 / (1 + e ** exponent)
