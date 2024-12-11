#!/usr/bin/python3
import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
G = nx.Graph()

# Add nodes
cities = ["Addis Ababa", "Mekelle", "Hawassa", "Dire Dawa", "Bahir Dar",
          "Jimma", "Gondar", "Adama", "Debre Berhan", "Harar"]

for city in cities:
    G.add_node(city)

# Add edges with distances
traveling_sales_man = {
    "Addis Ababa": {"Mekelle": 447, "Hawassa": 533, "Dire Dawa": 380, "Bahir Dar": 225,
                    "Jimma": 230, "Gondar": 166, "Adama": 598, "Debre Berhan": 276, "Harar": 201},
    "Mekelle": {"Addis Ababa": 447, "Hawassa": 331, "Dire Dawa": 394, "Bahir Dar": 644,
                "Jimma": 329, "Gondar": 273, "Adama": 150, "Debre Berhan": 161, "Harar": 426},
    "Hawassa": {"Addis Ababa": 533, "Mekelle": 331, "Dire Dawa": 569, "Bahir Dar": 682,
                "Jimma": 250, "Gondar": 396, "Adama": 164, "Debre Berhan": 275, "Harar": 546},
    "Dire Dawa": {"Addis Ababa": 380, "Mekelle": 394, "Hawassa": 569, "Bahir Dar": 430,
                  "Jimma": 615, "Gondar": 344, "Adama": 477, "Debre Berhan": 424, "Harar": 123},
    "Bahir Dar": {"Addis Ababa": 225, "Mekelle": 644, "Hawassa": 682, "Dire Dawa": 430,
                  "Jimma": 405, "Gondar": 378, "Adama": 729, "Debre Berhan": 482, "Harar": 197},
    "Jimma": {"Addis Ababa": 230, "Mekelle": 329, "Hawassa": 250, "Dire Dawa": 615,
              "Bahir Dar": 405, "Gondar": 227, "Adama": 422, "Debre Berhan": 223, "Harar": 400},
    "Gondar": {"Addis Ababa": 166, "Mekelle": 273, "Hawassa": 396, "Dire Dawa": 344,
               "Bahir Dar": 378, "Jimma": 227, "Adama": 329, "Debre Berhan": 142, "Harar": 206},
    "Adama": {"Addis Ababa": 598, "Mekelle": 150, "Hawassa": 164, "Dire Dawa": 477,
              "Bahir Dar": 729, "Jimma": 422, "Gondar": 329, "Debre Berhan": 280, "Harar": 546},
    "Debre Berhan": {"Addis Ababa": 276, "Mekelle": 161, "Hawassa": 275, "Dire Dawa": 424,
                     "Bahir Dar": 482, "Jimma": 223, "Gondar": 142, "Adama": 280, "Harar": 282},
    "Harar": {"Addis Ababa": 201, "Mekelle": 426, "Hawassa": 546, "Dire Dawa": 123,
              "Bahir Dar": 197, "Jimma": 400, "Gondar": 206, "Adama": 546, "Debre Berhan": 282},
}

# Add edges to the graph
for city, destinations in traveling_sales_man.items():
    for dest, distance in destinations.items():
        G.add_edge(city, dest, weight=distance)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Traveling Salesman State Space Graph")
plt.show()
