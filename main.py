import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
import numpy as np

def import_dat(filename):
    text = ""
    counts = []
    theta = []  
    with open(filename, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                try:
                    num1 = float(parts[0])
                    num2 = float(parts[1])
                    theta.append(num1)
                    counts.append(num2)
                except ValueError:
                    print(f"Skipping line {line}")
    return counts, theta
    
counts, theta = import_dat("diagrama.dat")

plt.plot(theta,counts)
plt.show()
