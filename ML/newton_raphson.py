import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-(x-5)**2) + 0.1*np.sin(x-2)
    
    

    
def dx(f, x, h = 1e-3):
    return (f(x + h) - f(x)) / h
    
def d2x(f, x, h = 1e-3):

    return((f(x+h) - 2*f(x) + f(x-h)) / h**2)

def newton_raphson(theta, f, c = 1, epsilon = 0.001, max_iter = 1000):

    x_values = []
    y_values = []

    print("--------------------")

    while max_iter >0 and abs(dx(f, theta)) > epsilon:


        step = 1

        x_values.append(theta)
        y_values.append(f(theta))

        gradient = dx(f, theta)
        hessian = d2x(f, theta)

        print("Theta: ", theta)
        print("Function value: ", f(theta))
        print("Gradient: ", gradient)
        print("Hessian: ", hessian)

        if hessian > 0:
            step = -step

    
        passed = False

        while not passed:
             
            passed = True 

            d = step * gradient / hessian
            theta_new = theta - d

            
            if f(theta_new) < f(theta) + c*d*gradient:
                    step = step / 2 
                    passed = False
            
            
    


                    
        print("Theta new: ", theta_new)
                
        theta = theta_new

        print("--------------------")
        max_iter -= 1

    return x_values, y_values, theta

theta = 3.5

x_values, y_values, optimal_theta = newton_raphson(theta, f)

print("Optimal theta: ", optimal_theta)

plt.plot(x_values, y_values, 'ro')

x = np.linspace(-5, 10, 100)
y = f(x)

plt.plot(x, y)
plt.show()
