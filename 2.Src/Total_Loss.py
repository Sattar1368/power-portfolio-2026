#     Total loss    #

Currents = [25, 25 , 25, 25]
resistances = [0.2, 0.3, 0.15, 0.4]

total_loss = 0 
for i in range(len(currents)):
    loss = currents[i]**2 * resistances[i]
    total_loss += loss
    print(f"Line {i+1} Loss = {loss:.2f} W")
print("\nTotal Network Loss =" , total_loss, "W")