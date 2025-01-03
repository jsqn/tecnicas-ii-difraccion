import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
import numpy as np
from data import data

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
    counts = np.array(counts)
    two_theta = np.array(theta)
    return counts, two_theta

def d_to_theta(d, lambda_k  = 1.5406):
    return np.arcsin(lambda_k/2*d)


def two_theta_to_d(two_theta_deg, lambda_k=1.5406):
  theta_rad = np.deg2rad(two_theta_deg / 2)  # Convert 2θ to θ and then to radians
  d = lambda_k / (2 * np.sin(theta_rad))
  return d

def plot_lines():
    for element in data:
        color = element['color']
        for line in element['lines']:
            plt.axvline(x= line['d'], color= color)
    
counts, two_theta = import_dat("diagrama.dat")

# Plot all of the lines
# plot_lines()
plt.plot(two_theta_to_d(two_theta),counts)
plt.show()

