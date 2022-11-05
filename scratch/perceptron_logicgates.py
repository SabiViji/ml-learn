import numpy as np

# AND
def AND(x):
    w = np.array([1, 1])
    b = -1
    x = np.array(x)
    val = x.dot(w) + b
    return 1 if val >= 1 else 0

tt = [[0,0], [0,1], [1,0], [1,1]]
result = [AND(i) for i in tt]
print(f"AND {result}")

# OR
def OR(x):
    w = np.array([2, 2])
    b = -1
    x = np.array(x)
    val = x.dot(w) + b
    return 1 if val >= 1 else 0

tt = [[0,0], [0,1], [1,0], [1,1]]
result = [OR(i) for i in tt]
print(f"OR {result}")

# NAND
def NAND(x):
    w = np.array([-2, -2])
    b = 3
    x = np.array(x)
    val = x.dot(w) + b
    return 1 if val >= 1 else 0

tt = [[0,0], [0,1], [1,0], [1,1]]
result = [NAND(i) for i in tt]
print(f"NAND {result}")

# NOR
def NOR(x):
    w = np.array([-1, -1])
    b = 1
    x = np.array(x)
    val = x.dot(w) + b
    return 1 if val >= 1 else 0

tt = [[0,0], [0,1], [1,0], [1,1]]
result = [NOR(i) for i in tt]
print(f"NOR {result}")

# NOT
def NOT(x):
    w = np.array([-1])
    b = 1
    x = np.array(x)
    val = x.dot(w) + b
    return 1 if val >= 1 else 0

tt = [[0], [1]]
result = [NOT(i) for i in tt]
print(f"NOT {result}")