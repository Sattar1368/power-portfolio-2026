voltage_pu = float(input("Enter voltage in per unit"))

if voltage_pu < 0.95: 
    print("Undervoltage condition")
elif voltage_pu <= 1.05:
    print("voltage is normal")
else: 
    print("Overvoltage condition")       