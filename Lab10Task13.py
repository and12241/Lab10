import numpy as np
array_3x5 = np.random.rand(3, 5) * 10
print("13 (сума елементів):", np.sum(array_3x5))
print("13 (мінімальний елемент):", np.min(array_3x5))
print("13 (максимальний елемент):", np.max(array_3x5))
print("13 (мінімум у кожному стовпці):", np.min(array_3x5, axis=0))
print("13 (мінімум у кожному рядку):", np.min(array_3x5, axis=1))
print("13 (максимум у кожному стовпці):", np.max(array_3x5, axis=0))
print("13 (максимум у кожному рядку):", np.max(array_3x5, axis=1))
print("13 (індекси мінімального елемента):", np.unravel_index(np.argmin(array_3x5), array_3x5.shape))
print("13 (індекси максимального елемента):", np.unravel_index(np.argmax(array_3x5), array_3x5.shape))