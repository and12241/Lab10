import numpy as np
random_array = np.random.rand(4, 4) * 10 + 1  # Уникаємо log(0)
log_array = np.log(random_array)
print("12 (натуральні логарифми):", log_array)