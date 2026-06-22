# power_monitor.py
print("=== Power System Monitoring Tool ===")

p = float(input("Enter Active power P(kW): "))
q = float(input("Enter Reactive power q(kvar): "))
v = float(input("Enter voltage V (V): "))
current_limit = float(input("Enter current limit (A): "))

s =(p**2 + q**2)**0.5
current = (s * 1000) / v
pf = p / s

print("\n=== Results ===")
print(f"Apparent Power : {s:.2f} kVA")
print(f"Current:         {current:.2f} A")
print(f"Power Factor:    {pf:.3f}")

print("\n=== Condition Assessment ===")

if current > current_limit:
    print("Warning: Current exceeds the allowble limit")
else:
    print("current is within allowable range")

if pf< 0.9:
    print("Warning: Power factor is low ")
else:
    print("Power factor is acceptable")

# condition_levels.py 

current = float(input("Enter current (A): "))

if current <= 250: 
    print("Status: Normal")
elif current <= 300:
    print("Statis: Warning")
else:
    print("Status: Critical")        