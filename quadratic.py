#Determine roots of a quadratic
print("General form of a quadratic is: ax² + bx + c")
a= float(input("What is a     "))
b= float(input("What is b     "))
c= float(input("What is c     "))
disc = pow(b,2) - 4*a*c
if disc >0:
    x1 = round(float(-b/(2*a)+ pow(disc,0.5)/(2*a)),3)
    x2 = round(float(-b/(2*a)- pow(disc,0.5)/(2*a)),3)
    print(f"It has real roots : {x1}, {x2}")
elif disc ==0:
    x= round(float(-b/(2*a)),3)
    print(f"It has a unique root : {x}")
elif disc <0:
    disc=-disc
    re_x1 = round(float(-b/(2*a)),3)
    im_x1 = round(float(pow(disc,0.5)/(2*a)),3)
    re_x2 = round(float(-b/(2*a)),3)
    im_x2 = round(float(- pow(disc,0.5)/(2*a)),3)
    print(f"It has complex roots : {re_x1} + {im_x1}i, {re_x2} + {im_x2}i")