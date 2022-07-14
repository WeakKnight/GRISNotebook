def problem(x):
    return x*x*x + x*x + x + 1

def targetFunction(x):
    return x*x*x

def analyticalIntegral(x):
    return 0.25 * x*x*x*x + x*x*x/3.0 + 0.5 * x*x + x

def integralOverDomain(a, b):
    return analyticalIntegral(min(a, b)) - analyticalIntegral(max(a, b))

