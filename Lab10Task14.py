import numpy as np
random_4x3 = np.random.randn(4, 3)
print("14 (середнє значення всіх елементів):", np.mean(random_4x3))
print("14 (середнє значення по рядках):", np.mean(random_4x3, axis=1))
print("14 (середнє значення по стовпцях):", np.mean(random_4x3, axis=0))
random_4x3[random_4x3 >= 0] = 5
random_4x3[random_4x3 > 0] = 3
print("14 (модифікований масив):", random_4x3)