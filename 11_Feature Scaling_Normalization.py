import numpy as np
import matplotlib.pyplot as plt

# داده‌ها (متراژ، تعداد اتاق)
X = np.array([
    [500, 1],
    [1500, 2],
    [2000, 3],
    [2500, 3],
    [3000, 4],
    [3500, 5]
])

y = np.array([150, 300, 350, 400, 450, 500])  # قیمت خانه (هزار دلار)
m = len(y)

# --- بدون Feature Scaling ---
X_b = np.c_[np.ones((m, 1)), X]
theta = np.zeros(X_b.shape[1])
alpha = 0.0000001  # نرخ یادگیری کوچیک چون مقیاس بزرگ
iterations = 5000

theta_history = []

for i in range(iterations):
    gradients = (1/m) * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - alpha * gradients
    theta_history.append(theta.copy())

predictions_no_scaling = X_b.dot(theta)

# --- با Feature Scaling (Mean Normalization) ---
X_scaled = (X - X.mean(axis=0)) / X.std(axis=0)
X_b_scaled = np.c_[np.ones((m, 1)), X_scaled]
theta_scaled = np.zeros(X_b_scaled.shape[1])
alpha_scaled = 0.01
theta_history_scaled = []

for i in range(iterations):
    gradients = (1/m) * X_b_scaled.T.dot(X_b_scaled.dot(theta_scaled) - y)
    theta_scaled = theta_scaled - alpha_scaled * gradients
    theta_history_scaled.append(theta_scaled.copy())

predictions_scaled = X_b_scaled.dot(theta_scaled)

# --- رسم نمودار ---
plt.figure(figsize=(12,5))

plt.plot(range(m), y, 'bo', label='Actual Price')
plt.plot(range(m), predictions_no_scaling, 'rx', label='Predicted without Scaling')
plt.plot(range(m), predictions_scaled, 'g+', label='Predicted with Scaling')
plt.title("Effect of Feature Scaling on Gradient Descent")
plt.xlabel("House Index")
plt.ylabel("Price (k$)")
plt.legend()
plt.show()
