import numpy as np

zeros = np.zeros(10)

mem_size = zeros.itemsize * zeros.size

print(mem_size)