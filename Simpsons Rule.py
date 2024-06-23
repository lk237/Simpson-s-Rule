import math                                       # import python math functions

def integralf(x):                                 # Integral function declaration for f(x)
    return math.sqrt(1 - (2/3) * math.sin(x)**2)  # Integral f(x)

def simpsons_rule(f, a, b, n):                     # Simpsons function with param f - function, a & b = interval, n - subinterval
    h = (b-a) / n                                  # calculates h = width of sub interval using end points
    s = f(a) + f(b)                                # initialize sum with values of f at endpoints 

    for i in range(1,n,2):                         # odd index Loops for summation aspect of Simpson's rule 
        s += 4 * f(a + i * h)                      # f(a + i * h) caclculates the x coordinate for odd number terms on subinterval, multiplied by 4 then added to s
    for i in range(2, n-1, 2):                     # even index Loops for summation aspect of Simpson's rule 
        s += 2 * f(a + i * h)                      # f(a + i * h) caclculates the x coordinate for even number terms on subinterval, multiplied by 2 then added to s

    return s * (h/3)                               # final integral approx, simpsons formula

lower_bound = 0                                    # lower bound delcaration
upper_bound = math.pi/2                            # upper bound delcaration

n = 100                                            # subinterval declaration



integral_value = simpsons_rule(integralf, lower_bound, upper_bound, n) # intergral value calculated using simspsons rule

circumference = 8 * math.sqrt(3) * integral_value  # Circumfrence of elipses formula multipled by integral value found aoboce 

print (f"the circumference of the ellipses is approximatley {circumference}") # Output print state ment 
