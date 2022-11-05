import numpy as np
import matplotlib.pyplot as plt

'''
- If sigmoid_fn has been a step function, then sigmoid neuron would be a perceptron, since output will be 0 or 1
'''

def sigmoid_fn(z):
    return 1/(1+ np.exp(-z))

x = [i for i in range(-4, 4)]
y = [sigmoid_fn(i) for i in x]

plt.plot(x, y)
plt.show()