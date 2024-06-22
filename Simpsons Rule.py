import math

def integralf(x):
    return math.sqrt(1 - (2/3) * math.sin(x)**2)

def simpsons_rule(f, a, b, n):
    h = (b-a) / n
    s = f(a) + f(b)

    for i in range(1,n,2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)

    return s * (h/3)

lower_bound = 0
upper_bound = math.pi/2

n = 100



integral_value = simpsons_rule(integralf, lower_bound, upper_bound, n)

circumference = 8 * math.sqrt(3) * integral_value

print (f"the circumference of the ellipses is approximatley {circumference}")
