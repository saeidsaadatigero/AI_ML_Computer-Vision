import numpy as np

# داده نمونه
x = np.array([1, 2, 3])
y = np.array([2, 4, 6])

m = len(x)

# پارامترها (theta0 = 0 , theta1 = 0)
theta0, theta1 = 0.0, 0.0
alpha = 0.01  # نرخ یادگیری

# پیش‌بینی
h = theta0 + theta1 * x

# گرادیان‌ها
d_theta0 = (1/m) * np.sum(h - y)
d_theta1 = (1/m) * np.sum((h - y) * x)

# آپدیت پارامترها
theta0 = theta0 - alpha * d_theta0
theta1 = theta1 - alpha * d_theta1

print("theta0:", theta0, "theta1:", theta1)