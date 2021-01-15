import numpy as np
"""Randomly finding order of our Fantasy Football Draft 2021"""

# Final ranks from 2021 along with weights. Last place is index 0 on the list.
ranking = [12, 11, 10, 9, 8, 7, 6]
weight = [0.448, 0.16, 0.128, 0.096, 0.08, 0.048, 0.04]

# Initialize draft order list
order = []
# Loop of 'selecting ping pong balls' until full order is chosen.
while len(order) < len(ranking):
    pick = np.random.choice(ranking, p=weight)
    if pick not in order:
        order.append(pick)
print(order)
