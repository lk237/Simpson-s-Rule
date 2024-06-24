# cs 3308 
# groupe name: Leonel Kachie Takoudjou, Alessio Naji-Sepasgozar, Minh Anh Thai

# Import the math module for mathematical functions
import math

# Define the function f1(alpha) for the elliptic integral
def f1(alpha):
  # Return the value of the function at point alpha
  return 8*math.sqrt(3) * math.sqrt(1 - (2/3)*math.sin(alpha)**2)

# Define the function f2(x) for the variable force
def f2(x):
  # Return the value of the function at point x
  return 100*x*math.sqrt(125 - x**3)

# Define a function to implement Simpson's Rule
def simpson(f, a, b, n):
  # Calculate the step size h
  h = (b - a) / n
  
  # Initialize the sum with the function values at the endpoints
  sum = f(a) + f(b)
  
  # Iterate over the interior points and add their function values to the sum
  # with appropriate weights (4 for odd indices, 2 for even indices)
  for i in range(1, n, 2):
    sum += 4 * f(a + i*h)
  for i in range(2, n-1, 2):
    sum += 2 * f(a + i*h)
  
  # Return the approximate integral value
  return sum * h / 3

# Approximate the circumference of an ellipse 
a = 0
b = math.pi/2
n = 100

# Approximate the circumference of an ellipse using Simpson's Rule
print("the circumference of the ellipses is approximatley:", simpson(f1, a, b, n))

# Approximate the work done 
a = 0
b = 5
n = 100
# Approximate the work done using Simpson's Rule
print("Simpson's Rule:", simpson(f2, a, b, n))