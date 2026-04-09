print("The linear equation must be in the form: ax + by + c = 0 ")
a=float(input("Enter coefficient of x in equation 1   "))
b=float(input("Enter coefficient of y in equation 1   "))
c=float(input("Enter constant term in equation 1  "))
a0=float(input("Enter coefficient of x in equation 2  "))
b0=float(input("Enter coefficient of y in equation 2  "))
c0=float(input("Enter constant term in equation 2 "))



if abs(a) < 1e-9 and abs(a0) < 1e-9:
    if abs(b) < 1e-9 and abs(b0) < 1e-9:
        if abs(c) < 1e-9 and abs(c0) < 1e-9:
            print("infinitely many solutions")
        else:
            print("Equations are inconsistent")
    else:
        # One equation is 0=0, other is a line
        print("infinitely many solutions")
else:
    determinant = a * b0 - a0 * b
    if abs(determinant) < 1e-9:
        print("Equations are inconsistent")
    else:
        x = (b * c0 - b0 * c) / determinant
        y = (c * a0 - c0 * a) / determinant
        print(f"The solutions are x = {x} and y= {y}")
