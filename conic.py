#Determine type of conic
# Equation must be of the form : ax²+ 2hxy + by² + 2gx + 2fy + c = 0
print(" Equation must be of the form : ax²+ 2hxy + by² + 2gx + 2fy + c = 0")
a = float(input("What is coefficient of x²    "))
h = float(input("What is coefficient of xy    "))
b = float(input("What is coefficient of y²    "))
g = float(input("What is coefficient of x    "))
f = float(input("What is coefficient of y    "))
c = float(input("What constant term   "))
g=g/2
f=f/2
h=h/2
det=a*(b*c-f**2)-h*(h*c-f*g)+g*(h*f-g*h)
if det == 0:
    print("This is the equation of a Pair of Straight Lines")
else:
    if a==b and h==0:
        print("This is the equation of a Circle")
    elif pow(h,2)-a*b<0:
        print("This is the equation of an Ellipse")
    elif pow(h,2)==a*b:
        print("This is the equation of a Parabola")
    elif pow(h,2)-a*b>0:
        print("This is the equation of a Hyperbola")
