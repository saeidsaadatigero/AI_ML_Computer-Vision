import numpy as np
import matplotlib.pyplot as plt

# داده‌های آموزشی ساده
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])   # خط y = x

# تابع فرضیه
def hypothesis(x, theta0, theta1):
    return theta0 + theta1 * x

# تابع هزینه
def cost_function(x, y, theta0, theta1):
    m = len(y)
    predictions = hypothesis(x, theta0, theta1)
    cost = (1/(2*m)) * np.sum((predictions - y) ** 2)
    return cost

# گرادیان نزول
def gradient_descent(x, y, alpha, iterations):
    theta0, theta1 = 0, 0   # شروع از صفر
    m = len(y)
    costs = []

    for _ in range(iterations):
        predictions = hypothesis(x, theta0, theta1)
        error = predictions - y

        # آپدیت θ0 و θ1
        theta0 -= alpha * (1/m) * np.sum(error)
        theta1 -= alpha * (1/m) * np.sum(error * x)

        costs.append(cost_function(x, y, theta0, theta1))
    return theta0, theta1, costs

# اجرای گرادیان نزول
alpha = 0.01   # نرخ یادگیری
iterations = 1000
theta0, theta1, costs = gradient_descent(x, y, alpha, iterations)

print(f"θ0 = {theta0:.4f}, θ1 = {theta1:.4f}")
print(f"Final cost = {costs[-1]:.6f}")

# ------------------------------
# رسم نمودار
# ------------------------------

# English explanation on chart
plt.figure(figsize=(12, 5))

# داده‌ها و خط یادگیری
plt.subplot(1, 2, 1)
plt.scatter(x, y, color="red", label="Training Data")
plt.plot(x, hypothesis(x, theta0, theta1), color="blue", label=f"Learned Line (θ0={theta0:.2f}, θ1={theta1:.2f})")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression with Gradient Descent")
plt.legend()
plt.grid(True)

# نمودار کاهش هزینه
plt.subplot(1, 2, 2)
plt.plot(range(len(costs)), costs, color="green")
plt.xlabel("Iterations")
plt.ylabel("Cost J(θ)")
plt.title("Cost Function Decrease Over Iterations")
plt.grid(True)

plt.tight_layout()
plt.show()