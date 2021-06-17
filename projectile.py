from math import pi, tan, cos

#Accelaration due to gravity, 9.81ms^2
g = 9.81

# Horizontal distance x
x = float(input("Please enter the horizontal distance travelled in metres: "))

# Height of barrel y0
y0 = float(input("Please enter the height of the barrel in metres: "))

# Elevation angle in degrees (deg)
deg = float(input("Please enter the angle of elevation in degrees: "))

# Initial velocity v0
v0 = float(input("Please enter the initial velocity in m/s: "))

# degrees in rad, theta
theta = deg * (pi/180)

# Calculation for height of projectile y

y = y0 + (x * tan(theta)) - ((g * (x**2)) / (2 * (v0 * cos(theta)) ** 2))
print(y)