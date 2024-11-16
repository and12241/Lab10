import numpy as np
# 2. Перетворити його на масиви з елементами типу float та complex.
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
arr_float = arr.astype(float)
arr_complex = arr.astype(complex)
print("2 (float):", arr_float)
print("2 (complex):", arr_complex)