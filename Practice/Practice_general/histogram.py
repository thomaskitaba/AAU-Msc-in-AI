#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np   


pi_arr = []
def pi(MAXN):
    # Initialize variables
    # MAXN = 1000  # Total number of iterations for the simulation
    n = 1  # Current iteration number
    n_circle = 0  # Counter for points inside the circle
    
    for i in range(1, MAXN):
        # toss 
        x, y = np.random.uniform(-1, 1, 2)
        color = 'b'
        if x**2 + y**2 <= 1:
            n_circle += 1
            color = 'r'
        pi_estimate = 4 * n_circle / i # Calculate the approximation of π
        pi_arr.append(pi_estimate)
        
    
    return pi_estimate

toss = input("Enter the number of tosses: ")
print(eval(toss))
pi(eval(toss))
plt.hist(pi_arr, bins=200, color='blue', edgecolor='black')
plt.xlabel("pi estimates")
plt.ylabel("number of tosses")
plt.axvline(x=3.14, color='red', linestyle='--', label="π ≈ 3.14")
plt.show()


