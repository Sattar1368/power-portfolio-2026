# interactive_calc.py
# این برنامه پارامترهای شبکه را از کاربر گرفته و جریان و توان ظاهری را محاسبه می‌کند.

print("=== ماشین حساب محاسبات خط انتقال ===")

# ۱. دریافت ورودی‌ها از کاربر و تبدیل آن‌ها به عدد اعشاری (float)
p_input = input("Enter the active power (kW): ")
P = float(p_input)

q_input = input("Enter the Reactive power.(kvar): ")
Q = float(q_input)

v_input = input("Enter the line voltage (V): ")
V = float(v_input)

# ۲. محاسبات مهندسی
# محاسبه توان ظاهری S = sqrt(P^2 + Q^2)
S = (P**2 + Q**2)**0.5

# محاسبه جریان بار I = S_VA / V
# توجه: چون توان‌ها به کیلو (k) هستند، برای محاسبه جریان ضرب در 1000 می‌کنیم تا به ولت-آمپر تبدیل شود.
S_VA = S * 1000
current = S_VA / V

# محاسبه ضریب توان (Power Factor = P / S)
power_factor = P / S

# ۳. نمایش نتایج با فرمت زیبا و دقیق
print("\n" + "="*30)
print(" Output results: ")
print("="*30)
print(f"Apparent network power: {S:.2f} kVA")
print(f"Current flowing through the line: {current:.2f} A")
print(f"Power factor (PF): {power_factor:.3f}")
print("="*30)
