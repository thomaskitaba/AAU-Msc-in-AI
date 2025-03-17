#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt  # Import for plotting

def estimate_pi(N):
    """
    Estimate the value of π using the Monte Carlo method.
    
    Parameters:
    N : int : Number of random samples to generate.
    
    Returns:
    float : Estimated value of π.
    """
    # Generate random (x, y) points in the range [-1, 1]
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    
    # Points inside the unit circle
    inside_circle = x**2 + y**2 <= 1
    
    # Estimate π
    pi_estimate = 4 * np.sum(inside_circle) / N
    return pi_estimate

# Testing for different N values (10^3, 10^4, 10^5, 10^6)
N_values = [10**3, 10**4, 10**5, 10**6]
pi_estimates = [estimate_pi(N) for N in N_values]

# Print the estimated π values
for N, estimate in zip(N_values, pi_estimates):
    print(f"N = {N}, Estimated π = {estimate}")

# Plotting convergence of estimated π with respect to N
plt.figure(figsize=(8, 6))
plt.plot(N_values, pi_estimates, marker='o', label="Estimated π")
plt.axhline(y=np.pi, color='r', linestyle='--', label="Actual π")
plt.xscale('log')  # Use log scale to highlight the convergence
plt.xlabel("Number of Points (N)")
plt.ylabel("Estimated π")
plt.title("Convergence of Monte Carlo Estimation of π")
plt.legend()
plt.show() 


