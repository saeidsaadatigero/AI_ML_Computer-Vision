import numpy as np
import matplotlib.pyplot as plt

# داده‌ی ساده برای تست (یک خط تقریبا y = 2x)
X = np.array([1, 2, 3, 4, 5])  
y = np.array([2, 4, 6, 8, 10])  
m = len(X)  # تعداد داده‌ها

# تابع گرادیان نزولی
def gradient_descent(alpha, iterations):
    # شروع از مقدار اولیه (هر دو پارامتر صفر هستن)
    theta0, theta1 = 0, 0  
    cost_history = []  # لیست برای ذخیره‌ی هزینه‌ها در هر تکرار

    for _ in range(iterations):
        # پیش‌بینی خروجی‌ها با خط فعلی
        predictions = theta0 + theta1 * X  
        
        # خطا = پیش‌بینی - مقدار واقعی
        error = predictions - y  
        
        # آپدیت کردن θ0 و θ1 با فرمول گرادیان نزولی
        theta0 -= alpha * (1/m) * np.sum(error)  
        theta1 -= alpha * (1/m) * np.sum(error * X)  
        
        # محاسبه‌ی هزینه (MSE) برای ثبت روند کاهش
        cost = np.sum((predictions - y) ** 2) / (2 * m)  
        cost_history.append(cost)

    return theta0, theta1, cost_history

# تست نرخ‌های یادگیری مختلف
alphas = [0.001, 0.01, 0.1, 1]  # لیستی از نرخ‌های یادگیری
iterations = 50  # تعداد تکرارها

plt.figure(figsize=(10,6))  # تنظیم اندازه‌ی نمودار
for alpha in alphas:
    # اجرای گرادیان نزولی با هر نرخ یادگیری
    _, _, cost_history = gradient_descent(alpha, iterations)
    
    # رسم نمودار هزینه بر اساس تعداد تکرار
    plt.plot(cost_history, label=f"alpha={alpha}")

# تنظیمات نمودار
plt.xlabel("تکرارها (Iterations)")  
plt.ylabel("هزینه (Cost)")  
plt.legend()  
plt.title("مقایسه نرخ‌های یادگیری مختلف")  
plt.show()