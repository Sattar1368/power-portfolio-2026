# یک مثال حرفه ای تر # ترکیب محاسبه + شرط 
# power_factor_check.py

p = 120   #KW
q = 90    #kvar

s = (p**2 + q**2)**0.5
pf = p / s

print("=== Power Factor Check ===")
print(f"Active Power:  {p} kW")
print(f"Reactive Power: {q} kvar")
print(f"Apparent Power: {s:.2f} kVA")
print(f"Power Factor:  {pf:.3f}")

if pf < 0.9: 
    print("Warning: Power factor is below acceptable limit")
else:
    print("Power fator is within acceptable range")    