#!/usr/bin/python3
print("Thomas kitaba")

import matplotlib.pyplot as plt

# plt.ion()

# Prepare data to be ploted
y = [1, 2, 3, 4, 5]
x = ["a", "b", "c", "d", "e"]

q = [11, 12, 13, 14, 15]
p = ["a", "b", "c", "d", "e"]


# set the size of figure
fig, ax = plt.subplots(1, 2, figsize=(8, 6))

# now ax is like plt
ax[0].bar(x, y,  color="red")
ax[0].set_ylabel("city")
# ~ plt.ylabel("city")

ax[0].set_xlabel("population") # ~ plt.ylabel("population")
ax[0].set_title("x and y graph")


ax[1].plot(p, q, color='g', marker='x')
ax[1].set_xlabel("population")
ax[1].set_ylabel("")
ax[1].set_title("p and q graph")

plt.legend()      
plt.tight_layout()  # Adjust spacing to avoid overlap
plt.tight_layout()  # Adjust spacing to avoid overlap
# plt.iof()
plt.show()






