import matplotlib.pyplot as plt
x =[0, 1, 2, 3]
y =[0, 10, 20, 30]
plt.plot(x, y)
plt.title("Power Curve")
plt.xlabel("Time")
plt.ylabel("Power")
plt.grid(True)
plt.show()

V = 230 
I = 4.5 
P = V * I 
print(f"Voltage = {V} V")
print(f"Current = {I} A")
print(f"Power = {P: .2f} w")

p = 100 
q = 60 
s = (p**2 + q**2)**0.5
print(s)

power = 5000
voltage = 400 
current = power / voltage 
print(current)

I = 15 
R = 0.3
Ploss = I**2 * R
print(Ploss)

p = 300 
Q = 150 
s = (p**2 + Q**2)**0.5
print(s)

voltage = 400 
Power = 10000 
current = power / voltage 
print(current)

I = 25 
R = 0.4
loss = I**2 * R
print(loss)

