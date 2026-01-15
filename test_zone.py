#test zone

import numpy as np

a = np.array([11, 11, 0, 0, 8, 1])
b = np.array([18, 18, 18, 18, 18, 0])

if (a > b).any() :
    print("Horrayy!!")

