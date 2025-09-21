import numpy as np

# داده‌های نمونه (x: ورودی‌ها، y: خروجی‌های واقعی)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])  # رابطه واقعی y = 2x

# فرض می‌کنیم مدل ما y = θ0 + θ1 * x
def hypothesis(x, theta0, theta1):
    return theta0 + theta1 * x

# تابع هزینه
def cost_function(x, y, theta0, theta1):
    m = len(y)
    predictions = hypothesis(x, theta0, theta1)
    errors = predictions - y
    cost = (1/(2*m)) * np.sum(errors ** 2)
    return cost

# تست: خطی که بد باشه
print("Cost when θ0=1, θ1=1.5:", cost_function(x, y, 1, 1.5))

# تست: خط درست (y=2x)
print("Cost when θ0=2, θ1=3:", cost_function(x, y, 2, 3))