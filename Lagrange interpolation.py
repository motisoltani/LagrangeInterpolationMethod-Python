'''
Interpolation and Curve Fitting
Lagrange Interpolation Method 
language: Python

Motahare Soltani
soltani.wse@gmail.com

'''
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

#Specifying X and Y values

x = list(input( 'Enter X = ' ))
y = [0, 9.1, 25, 31]

'''x =np.array([8.5, 10, 12], float)
y =  list(np.cos((np.pi / 4) * x)*x)'''

print('x=',x)
print('y=',y)

poly = lagrange(x, y)

#Equation coefficients
print('coef=',Polynomial(poly).coef)

#Enter the point at which you want to calculate
z = float(input('Enter the point at which you want to calculate:'))
print("The value of polynomial: ","%.3f"%poly(z))

#Plot 
step = 0.1
x_list = np.arange(x[0], x[-1]+0.1, step).tolist()
y_list = poly(x_list)
fig = figure(figsize=(8, 8), dpi=75)
font1 = {'color':'blue','size':15}
plt.scatter(x,y, marker='*', c='purple', s=250)
plt.plot(x_list, y_list, 'b-')
plt.xlabel('X', fontsize=12)
plt.ylabel('Function', fontsize=12)
plt.title('Lagrange Interpolation Method', fontdict=font1, loc='left')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend(['Interpolation', 'Data'], loc ="lower right")
plt.show()