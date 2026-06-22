print("Basic power system Calculations")
voltage = 400 
current = 25 
power = voltage * current
print("voltage=",voltage,"v") 
print("current=",current,"A")
print("Power =",power,"w")

#basic_calculations.py
p = 300    # Active power in kW
q = 150    # Reactive power in kvar

s = (p**2 + q**2)**0.5

print("===Apparent power Calculation ===")
print(f"Active power (p):  {p} kW")
print(f"Reactive power (Q):  {q} kvr")
print(f"Apparent power (s):{s:.2f} KVA")

I=20
R=0.2
loss = I**2 * R
print("\n=== Line Loss Calculation ===")
print(f"Current:    {I} A")
print(f"Resistance: {R} ohm")
print(f"Loss:      {loss:.2f} W")
