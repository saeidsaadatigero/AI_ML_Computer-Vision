import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# داده‌های رزولوشن (ضلع تصویر)
resolutions = np.array([64, 128, 256, 512])
resolutions = np.array([64, 128, 256, 512])
x = resolutions**2   # تعداد پیکسل‌ها
x = resolutions**2
y = np.array([5, 20, 80, 320])  # زمان اجرا (ms)
y = np.array([5, 20, 80, 320])

# ------------------------------
# نرمال‌سازی ویژگی‌ها (Feature Scaling)
# ------------------------------
mu = np.mean(x)
mu = np.mean(x)
sigma = np.std(x)
x_scaled = (x - mu) / sigma   # استانداردسازی
x_scaled = (x - mu) / sigma

# تابع فرضیه
def hypothesis(x, theta0, theta1):
    return theta0 + theta1 * x
def hypothesis(x, theta0, theta1):
    return theta0 + theta1 * x    

# تابع هزینه
def cost_function(x, y, theta0, theta1):
    m = len(y)
    predictions = hypothesis(x, theta0, theta1)
    cost = (1/(2*m)) * np.sum((predictions - y) ** 2)
    return cost

def cost_fanction(x, y, theta0, theta1):
    m = len(y)
    predictions = hypothesis(x, theta0, theta1)
    cost = (1/(2*m)) * np.sum((predictions - y) ** 2)
    return cost    

# گرادیان نزول
def gradient_descent(x, y, alpha, iterations):
    theta0, theta1 = 0, 0
    m = len(y)
    costs = []

def gradient_descent(x, y, alpha, interations):
    theta0, theta1 = 0, 0
    m = len(y)
    costs = []


    for _ in range(iterations):
        predictions = hypothesis(x, theta0, theta1)
        error = predictions - y

    for _ in range    

        # آپدیت θ0 و θ1
        theta0 -= alpha * (1/m) * np.sum(error)
        theta1 -= alpha * (1/m) * np.sum(error * x)

        costs.append(cost_function(x, y, theta0, theta1))
    return theta0, theta1, costs

# اجرای گرادیان نزول روی داده‌ی نرمال‌شده
alpha = 0.1   # الان می‌تونیم α بزرگ‌تر بذاریم
iterations = 500
theta0, theta1, costs = gradient_descent(x_scaled, y, alpha, iterations)

print(f"θ0 = {theta0:.4f}, θ1 = {theta1:.4f}")
print(f"Final cost = {costs[-1]:.6f}")

# ------------------------------
# رسم نمودار
# ------------------------------

plt.figure(figsize=(12, 5))

# نمودار داده‌ها و خط رگرسیون
plt.subplot(1, 2, 1)
plt.scatter(x, y, color="red", label="Real Data")
plt.plot(x, hypothesis((x - mu) / sigma, theta0, theta1), color="blue", 
         label=f"Learned Line (with scaling)")
plt.xlabel("Number of Pixels (x²)")
plt.ylabel("Processing Time (ms)")
plt.title("Image Resolution vs Processing Time (Feature Scaling)")
plt.legend()
plt.grid(True)

# نمودار هزینه
plt.subplot(1, 2, 2)
plt.plot(range(len(costs)), costs, color="green")
plt.xlabel("Iterations")
plt.ylabel("Cost J(θ)")
plt.title("Cost Decrease with Feature Scaling")
plt.grid(True)

plt.tight_layout()
plt.show()