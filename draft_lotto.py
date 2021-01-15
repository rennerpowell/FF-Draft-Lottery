import numpy as np


ranking = [12, 11, 10, 9, 8, 7, 6]
weight = [0.448, 0.16, 0.128, 0.096, 0.08, 0.048, 0.04]

order = []
while len(order) < len(ranking):
    pick = np.random.choice(ranking, p=weight)
    if pick not in order:
        order.append(pick)
print(order)
