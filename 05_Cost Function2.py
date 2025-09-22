# import numpy as np

# # داده‌های نمونه (x: ورودی‌ها، y: خروجی‌های واقعی)
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 4, 6, 8, 10])  # رابطه واقعی y = 2x

# # فرض می‌کنیم مدل ما y = θ0 + θ1 * x
# def hypothesis(x, theta0, theta1):
#     return theta0 + theta1 * x

# # تابع هزینه
# def cost_function(x, y, theta0, theta1):
#     m = len(y)
#     predictions = hypothesis(x, theta0, theta1)
#     errors = predictions - y
#     cost = (1/(2*m)) * np.sum(errors ** 2)
#     return cost

# # تست: خطی که بد باشه
# print("Cost when θ0=1, θ1=1.5:", cost_function(x, y, 1, 1.5))

# # تست: خط درست (y=2x)
# print("Cost when θ0=2, θ1=3:", cost_function(x, y, 2, 3))
import numpy as np
import matplotlib.pyplot as plt

# Data (x = size in m², y = price in million Toman)
x = np.array([50, 60, 70, 80, 90])
y = np.array([150, 180, 210, 240, 270])

# Model parameters
# theta0 عرض از مبدا
# theta1 شیب
theta0 = 0
theta1 = 3

def compute_cost(x, y, theta0, theta1):
    m = len(y)
    predictions = theta0 + theta1 * x
    errors = predictions - y
    cost = (1 / (2 * m)) * np.sum(errors ** 2)
    return cost

# Compute cost
print("Model cost:", compute_cost(x, y, theta0, theta1))

# Predictions
predictions = theta0 + theta1 * x

# Plot
plt.scatter(x, y, color="red", label="Actual data")   # Real data
plt.plot(x, predictions, color="blue", label="Model line")   # Model line
plt.xlabel("Size (m²)")
plt.ylabel("Price (Million Toman)")
plt.title("Linear Regression - Size vs Price")
plt.legend()
plt.grid(True)
plt.show()
