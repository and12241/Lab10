import numpy as np
arr1 = np.random.rand(4, 4)
arr2 = np.random.rand(4, 4)
print("15 (поелементні максимуми):", np.maximum(arr1, arr2))
print("15 (поелементні мінімуми):", np.minimum(arr1, arr2))