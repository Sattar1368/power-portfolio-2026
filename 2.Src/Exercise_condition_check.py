current = 280 
limit = 250 

if current > limit: 
    print("Warining: Line overload detected")


#                condition_check.py    else استفاده از          #
current = 220 
limit = 250 

if current > limit: 
    print("Warining: Line overload detected")
else:
    print("System is operating within safe current limit")

#                condition_check.py    elif استفاده از          #
current = 290 
if current<= 250 : 
    print("Normal operation")
elif current <= 300:
    print("Warning: Current is near critical level")
else:
    print("Critical: Overcurrent condition")    

power_factor = 0.84

if power_factor < 0.9:
    print("Warning: Power factor is low")
else:
    print("Power factor is acceptable")    

        