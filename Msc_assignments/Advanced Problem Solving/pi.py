#!/usr/bin/python3
import numpy as np   
import matplotlib.pyplot as plt

def e(x):
    return (np.exp(-x**2))

def pi(max):
     
    
    # step 0 initializa variables
    pi_arr = []  # to visualize as a histogram
    n_circle = 0
    # step 2 check if the point is inside the circle or not
    # step 1 generate randome number
    for i in range (1, max):
        color = 'b'
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        
        if x**2 + y**2 <= 1:
            color = 'r'
            n_circle += 1

        pi_estimate = 4 * (n_circle/i)
        #e stimiate = e(x, y)
        pi_arr.append(pi_estimate)

    return pi_arr

if __name__ == "__main__":
    print("thomas kitaba")
    pi_arr = pi(10000)
    print(np.mean(pi_arr))
    # draw Graph 
    fig, ax = plt.subplots(1, 2, figsize=(10, 6))
    
    # draw the historgram first
    ax[0].hist(pi_arr, bins=50)
    ax[0].set_title("Historgram")
    ax[0].set_xlabel("pi bin")
    ax[0].set_ylabel("frequence")
    
    # draw line graph (we need 2 arrays pi_arr and n)
    iteration = []
    # iteration = list(range(1, len(pi_arr) + 1))
    for i in range(len(pi_arr)):
        iteration.append(i)

    ax[1].plot(iteration, pi_arr)
    ax[1].set_title("line graph")
    ax[1].set_xlabel("pi bin")
    ax[1].set_ylabel("frequence")
    
    plt.grid()
    plt.show()
   