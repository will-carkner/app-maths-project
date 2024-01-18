import math
from matplotlib import pyplot as plt

def plot_model3(u):
    results = {}
    u = int(u)
    mu = 0.3
    g = 9.8
    r = 10
    for theta in range(0, 360, 5):
        theta = math.radians(theta)
        w_f =  (2 * mu * ((u**2 * theta) + (3 * g * r * math.sin(theta)) - (2 *g * r * theta))) / (1 + 2 * mu * theta)
        v = math.sqrt(u**2 - w_f + (2 * g * r * (math.cos(theta) - 1)))
        results[math.degrees(theta)] = v
    plt.plot(results.keys(), results.values())
    plt.xlabel('theta (degrees)')
    plt.ylabel('velocity (m/s)')
    plt.show()

def min_u(r):
    pass


plot_model3(30)

min_u(10)