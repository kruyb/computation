#Matrix Inverter
q1=input("Enter order of Matrix:\n A:2x2    B:3x3 \n ")
if q1 == "A":
    a1=float(input("What is a1  "))
    a2=float(input("What is a2  "))
    b1=float(input("What is b1  "))
    b2=float(input("What is b2  "))
    print("This is your matrix")
    print(f"[{a1} {a2}]")  
    print(f"[{b1} {b2}]")
    det = a1*b2 - a2*b1
    if det ==0:
        print("This is an non-invertible matrix")
    else:
        a_1 = a2/det
        a_2 = a1/det
        b_1 = b1/det
        b_2 = b2/det
        print(f"The inverse of your matrix is")
        print(f"[{a_1} {a_2}]")
        print(f"[{b_1} {b_2}]")


elif q1 == "B":
    a1=float(input("What is a1  "))
    a2=float(input("What is a2  "))
    a3=float(input("What is a3  "))
    b1=float(input("What is b1  "))
    b2=float(input("What is b2  "))  
    b3=float(input("What is b3  "))
    c1=float(input("What is c1  "))
    c2=float(input("What is c2  "))
    c3=float(input("What is c3  "))
    print("This is your matrix")
    print(f"[{a1} {a2} {a3}]")  
    print(f"[{b1} {b2} {b3}]")  
    print(f"[{c1} {c2} {c3}]")  
    det = (a1*(b2*c3 - b3*c2) - a2*(b1*c3 - b3*c1)  + a3*(b1*c2 - b2*c1))
    if det ==0:
        print("This matrix is non-invertible")
    else:
        a_1 = a1/det
        a_2 = a2/det
        a_3 = a3/det
        b_1 = b1/det
        b_2 = b2/det
        b_3 = b3/det
        c_1 = c1/det
        c_2 = c2/det
        c_3 = c3/det
        print("The inverse of your matrix is")
        print(f"[{a_1} {a_2} {a_3}]")  
        print(f"[{b_1} {b_2} {b_3}]")  
        print(f"[{c_1} {c_2} {c_3}]")  

else:
    print("Choose an valid option")
#Completed