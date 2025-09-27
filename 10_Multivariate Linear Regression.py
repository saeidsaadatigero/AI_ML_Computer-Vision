import numpy as np
import matplotlib.pyplot as plt

# داده‌های نمونه
X = np.array([
    [1, 2],
    [2, 0],
    [3, 1],
    [4, 3]
])
y = np.array([4, 3, 5, 6])
m = len(y)

# اضافه کردن ستون 1 برای theta0
X_b = np.c_[np.ones((m, 1)), X]

# θ اولیه
theta = np.zeros(X_b.shape[1])

alpha = 0.01
iterations = 1000

# برای ذخیره روند cost و thetaها
theta_history = []

# Gradient Descent
for i in range(iterations):
    gradients = (1/m) * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - alpha * gradients
    theta_history.append(theta.copy())

# پیش‌بینی نهایی
predictions = X_b.dot(theta)

print("θ0, θ1, θ2 =", theta)
print("Predictions:", predictions)

# --- رسم نمودار ---
fig = plt.figure(figsize=(10,5))

# نمودار واقعی و پیش‌بینی
plt.scatter(range(m), y, color='blue', label='Actual y')
plt.scatter(range(m), predictions, color='red', marker='x', label='Predicted y')
plt.title("Multivariate Linear Regression: Actual vs Predicted")
plt.xlabel("Data Point Index")
plt.ylabel("y value")
plt.legend()
plt.show()

