#python bus_voltage_analysis.py

voltages =[1.02, 0.97, 0.93, 1.01, 1.07]
for v in voltages:
    if v < 0.95:
        print(f"Voltage {v} pu  Undervoltage")
    elif v <= 1.05:
        print(f"Voltage {v} pu  Normal")    
    else:
        print(f"Voltage {v} pu  Overvoltage") 

#         Python example for loop (for)        #

voltages =[1.02, 0.97, 0.93]
for i in range(len(voltages)):
    print("Bus", i+1, "Voltage =" , voltages[i])

    #        line_loss_analysis.py     #

currents = [20, 20 , 20, 20]
resistances = [0.2, 0.3, 0.15, 0.4]


for i in range(len(currents)):
    I = currents[i]
    R = resistances [i]
    loss = i**2 * R
    print(f"line {i+1} Loss = {loss:.2f} W")

 
 