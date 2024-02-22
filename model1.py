import matplotlib.pyplot as plt
import math
import pandas as pd
import numpy as np

r = 10

def plot_model1(u):
    results = {}
    u = int(u)
    for theta in range(0, 360, 5):
        theta = math.radians(theta)
        v = math.sqrt((u**2 - 2*9.8*r) + 2*9.8*r*(math.cos(theta)))
        results[math.degrees(theta)] = v
    plt.plot(results.keys(), results.values())
    plt.xlabel('theta (degrees)')
    plt.ylabel('velocity (m/s)')

def plot_min_vs_rad(r):
    min_u = round(math.sqrt(5*9.8*r), 0)
    min_u = int(min_u)
    res[r] = min_u    


if __name__ == '__main__':
    min_u = round(math.sqrt(5*9.8*r), 0)
    min_u = int(min_u)
    
    print(f'Minimum u = {min_u} m/s')

    for i in range(min_u, min_u + 11, 2):
        plot_model1(i)
        plt.legend([f'u = {min_u}', f'u = {min_u + 2}', f'u = {min_u + 4}', f'u = {min_u + 6}', f'u = {min_u + 8}', f'u = {min_u + 10}'])

    plt.show()

    res = {}
    for i in range(0, 101, 10):
        plot_min_vs_rad(i)

    plt.plot(res.keys(), res.values())
    # convert res to pd datafram
    # plot curve of best fit for minimum velocity vs radius
    import matplotlib.pyplot as plt

    res_df = pd.DataFrame({'radius': list(res.keys()), 'minimum_velocity': list(res.values())})

    # Plot curve of best fit for minimum velocity vs radius
    x = res_df['radius']
    y = res_df['minimum_velocity']
    coefficients = np.polyfit(x, y, 2)
    polynomial = np.poly1d(coefficients)
    x_new = np.linspace(x.min(), x.max(), 100)
    y_new = polynomial(x_new)

    plt.plot(x, y, 'o', label='Data')
    plt.plot(x_new, y_new, label='Best Fit Curve')
    plt.xlabel('radius (m)')
    plt.ylabel('minimum velocity (m/s)')
    plt.legend()
    plt.show()
