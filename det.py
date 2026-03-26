#Determinant Calculator
q1=input("Enter order of determinant:\n A:2x2    B:3x3 \n ")
if q1 == "A" or "a":
    a1=float(input("What is a1  "))
    a2=float(input("What is a2  "))
    b1=float(input("What is b1  "))
    b2=float(input("What is b2  "))
    print("This is your matrix")
    if a1==1 and a2==0 and b1==0 and b2==1:
        print("This is a special matrix! it is called an Identity matrix of order 2")
    elif a1 ==0 and a2 ==0 and b1 ==0 and b2 ==0:
        print("This is a special matrix! it is called an Null matrix of order 2")
    print(f"[{a1} {a2}]")  
    print(f"[{b1} {b2}]")
    det = a1*b2 - a2*b1
    print(f"The determinant of this 2x2 matrix is {det}")

elif q1 == "B" or "b":
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
    if a1==1 and a2==0 and a3==0 and b1==0 and b2==1 and b3==0 and c1==0 and c2==0 and c3==1:
        print("This is a special matrix! it is called an Identity matrix of order 3")  
    elif a1==0 and a2==0 and a3==0 and b1==0 and b2==0 and b3==0 and c1==0 and c2==0 and c3==0:
        print("This is a special matrix! it is called an Null matrix of order 3")
    print(f"[{a1} {a2} {a3}]")  
    print(f"[{b1} {b2} {b3}]")  
    print(f"[{c1} {c2} {c3}]")  
    det = (a1*(b2*c3 - b3*c2) - a2*(b1*c3 - b3*c1)  + a3*(b1*c2 - b2*c1))

    print(f"The determinant of this 3x3 matrix is {det}")
else:
    print("Choose an valid option")
#Completed