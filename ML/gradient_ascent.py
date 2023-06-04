import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-(x-5)**2) + 0.1*np.sin(x-2)
    

def dx(f, x, h = 1e-8):
    return (f(x + h) - f(x)) / h
    


def gradient_ascent(theta, f, c = 1, epsilon = 0.01, step = 5, max_iter = 100):

    x_values = []
    y_values = []

    while max_iter > 0 and abs(dx(f, theta)) > epsilon:
       
        x_values.append(theta)
        y_values.append(f(theta))

        gradient = dx(f, theta)

        theta_new = theta + step * gradient

        if f(theta_new) < f(theta) + c * step * gradient:
            step = step / 2
        
        theta = theta_new

    return x_values, y_values, theta


    
theta = 3.5

x_values, y_values, optimal_theta = gradient_ascent(theta, f)

print("Optimal theta: ", optimal_theta)

#plot function

x = np.linspace(-5, 10, 100)
y = f(x)

plt.plot(x, y)
plt.plot(x_values, y_values, 'ro')
plt.show()

    




