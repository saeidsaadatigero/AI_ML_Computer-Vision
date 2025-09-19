import numpy as np                # برای کار با آرایه‌ها و محاسبات ریاضی
import matplotlib.pyplot as plt   # برای رسم نمودارها

# داده‌های اولیه: متراژ (X) و قیمت (Y)
X = np.array([50, 80, 120])       # ورودی‌ها (متراژ خانه)
Y = np.array([1500, 2200, 3000])  # خروجی‌ها (قیمت خانه)

# محاسبه شیب خط (w) به روش حداقل مربعات
# فرمول: w = covariance(X,Y) / variance(X)
w = np.cov(X, Y, bias=True)[0, 1] / np.var(X)

# محاسبه عرض از مبدأ (b)
# فرمول: b = میانگین(Y) - w * میانگین(X)
b = np.mean(Y) - w * np.mean(X)

# نمایش مقدارهای محاسبه‌شده
print("شیب خط (w):", w)
print("عرض از مبدأ (b):", b)

# محاسبه خروجی پیش‌بینی‌شده مدل
# فرمول: Y_pred = w*X + b
Y_pred = w * X + b

# رسم نمودار
plt.scatter(X, Y, color="red", label=" Real DATA")     # نقاط واقعی (قرمز)
plt.plot(X, Y_pred, color="blue", label="Line Regresion Pridict ")      # خط پیش‌بینی (آبی)
plt.xlabel("metr(m²)")                                    # برچسب محور X
plt.ylabel("Price (Toman)")                                # برچسب محور Y
plt.legend()                                                # نمایش راهنما (Legend)
plt.show()                                                  # نمایش نمودار
