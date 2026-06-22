# Feeder_ Current_Check.py
Currents = [120, 180, 260, 210, 300]
limit = 250  

for current in Currents :
    
    if current > limit: 
        print(f"Current {current} A  Overload")
    else:
        print(f"Current {current} A  Normal")
        
            