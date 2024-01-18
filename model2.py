import math

from matplotlib import pyplot as plt

def velocity_at_angle(u, theta, radius):
    
    theta = math.radians(theta)
    mu = 0.3

    v = math.sqrt(u**2 - 2* (mu * (u**2/radius + 9.8*math.sin(theta)) - 9.8*math.cos(theta)) * (2*math.pi*radius/360))

    return v

v = 50
results = {}

for i in range(0, 360):

    v = velocity_at_angle(v, i, 10)
    results[i] = v



plt.plot(results.keys(), results.values())
plt.xlabel('theta (degrees)')
plt.ylabel('velocity (m/s)')
plt.show()



def min_velocity(r):
    for j in range(0, 10000, 1):
        v = j
        try:
            for i in range(0, 360):
                v = velocity_at_angle(v, i, r)
            return j       
        except ValueError:
            continue

res = {}

for i in range(1, 101, 10):
    j = min_velocity(i)
    res[i] = j

plt.plot(res.keys(), res.values(), 'ro')
plt.xlabel('radius (m)')
plt.ylabel('minimum velocity (m/s)')

plt.show()