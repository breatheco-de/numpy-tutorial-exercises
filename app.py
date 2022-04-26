import numpy as np

Z = np.zeros((7,7),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)