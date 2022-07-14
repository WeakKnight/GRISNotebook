import matplotlib.pyplot as plt
import numpy as np
import math

def problem(x):
    return x*x*x + x*x + x + 1

def constructReferenceImage():
    width = 256
    height = 256
    x = []
    for i in range(width):
        x.append(0.5 *  1.0 / (width - 1))

def targetFunction(x):
    return x*x*x

def analyticalIntegral(x):
    return 0.25 * x*x*x*x + x*x*x/3.0 + 0.5 * x*x + x

def integralOverDomain(a, b):
    return analyticalIntegral(min(a, b)) - analyticalIntegral(max(a, b))

def display2DArray(data):
    plt.imshow(data)
    plt.gray()
    plt.show()