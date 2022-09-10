import numpy as np

def perceptron(inp, wt):
    s = 0
    for i in range(len(inp)):
        s += inp[i]*wt[i]
    if s>=0:
        val = 1
    else:
        val = 0
    return val

inp = np.array([8,2,4])
wt = np.array([-1,5,0])
output = perceptron(inp,wt)
print('Output: ', output)

