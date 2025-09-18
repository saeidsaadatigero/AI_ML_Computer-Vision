import numpy as np
import matplotlib.pyplot as plt

# داده نمونه: متراژ خونه و قیمت
X = np.array([50, 60, 80, 100, 120])
Y = np.array([150000, 180000, 240000, 300000, 380000])  # میلیون ریال

# پارامترهای اولیه
w = 2   # وزن (شیب خط)
b = 50  # بایاس (عرض از مبدا)

# تابع پیش‌بینی
def predict(x, w, b):
    return w * x + b

# محاسبه هزینه (تابع هزینه MSE)
def cost(X, Y, w, b):
    m = len(X)
    total = 0
    for i in range(m):
        y_hat = predict(X[i], w, b)
        total += (y_hat - Y[i])**2
    return total / (2*m)

print("هزینه اولیه:", cost(X, Y, w, b))

# رسم داده‌ها و خط رگرسیون
plt.scatter(X, Y, color='blue', label="داده واقعی")
plt.plot(X, predict(X, w, b), color='red', label="پیش‌بینی مدل")
plt.xlabel("متراژ (متر)")
plt.ylabel("قیمت (میلیون ریال)")
plt.legend()
plt.show()
