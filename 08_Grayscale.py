import numpy as np

# شبیه‌سازی روشنایی یک تصویر (ستونی از پیکسل‌ها)
pixels = np.array([10, 20, 30, 40, 50])  # شدت روشنایی
labels = np.array([12, 22, 29, 41, 52])  # مقدار واقعی (کمی نویزدار)

m = len(pixels)
theta0, theta1 = 0.0, 0.0
alpha = 0.001

h = theta0 + theta1 * pixels
d_theta0 = (1/m) * np.sum(h - labels)
d_theta1 = (1/m) * np.sum((h - labels) * pixels)

theta0 = theta0 - alpha * d_theta0
theta1 = theta1 - alpha * d_theta1

print("theta0:", theta0, "theta1:", theta1)