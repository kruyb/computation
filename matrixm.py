#Matrix Multiplication 
q1=input("Enter order of Matrix:\n A:2x2    B:3x3 \n ")
if q1 == "A":
    a1=float(input("What is a1  "))
    a2=float(input("What is a2  "))
    b1=float(input("What is b1  "))
    b2=float(input("What is b2  "))
    print("This is your premultiplier ")
    print(f"[{a1} {a2}]")  
    print(f"[{b1} {b2}]")
    a_1=float(input("What is a'1  "))
    a_2=float(input("What is a'2  "))
    b_1=float(input("What is b'1  "))
    b_2=float(input("What is b'2  "))
    print("This is your postmultiplier ")
    print(f"[{a_1} {a_2}]")  
    print(f"[{b_1} {b_2}]")
    # confirmation=input("confirm matrix? type YES")
    # if confirmation == "YES":

    print(f"[{a1} {a2}][{a_1} {a_2}]")  
    print(f"[{b1} {b2}][{b_1} {b_2}]")
    intermediate=input("Type ""YES"" to multiply?   ")
    c1 = a1*a_1 + a2*b_1
    c2 = a1*a_2 + a2*b_2
    c3 = b1*a_1 + b2*b_1
    c4 = b1*a_2 + b2*b_2
    print("Here is the resultant matrix")
    print(f"[{c1} {c2}]")  
    print(f"[{c3} {c4}]")

elif q1 == "B":
    a1=float(input("What is a1  "))
    a2=float(input("What is a2  "))
    a3=float(input("What is a2  "))
    b1=float(input("What is b1  "))
    b2=float(input("What is b2  "))
    b3=float(input("What is a2  "))
    c1=float(input("What is a2  "))
    c2=float(input("What is a2  "))
    c3=float(input("What is a2  "))
    print("This is your premultiplier ")
    print(f"[{a1} {a2} {a3}]")  
    print(f"[{b1} {b2} {b3}]")
    print(f"[{c1} {c2} {c3}]")
    a_1=float(input("What is a1  "))
    a_2=float(input("What is a2  "))
    a_3=float(input("What is a2  "))
    b_1=float(input("What is b1  "))
    b_2=float(input("What is b2  "))
    b_3=float(input("What is a2  "))
    c_1=float(input("What is a2  "))
    c_2=float(input("What is a2  "))
    c_3=float(input("What is a2  "))
    print("This is your postmultiplier ")
    print(f"[{a_1} {a_2} {a_3}]")  
    print(f"[{b_1} {b_2} {b_3}]")
    print(f"[{c_1} {c_2} {c_3}]")
    # if a1==1 and a2==0 and b1==0 and b2==1:
    #     print("This is a special matrix! it is called an Identity matrix of order 2")
    # elif a1 ==0 and a2 ==0 and b1 ==0 and b2 ==0:
    #     print("This is a special matrix! it is called an Null matrix of order 2")

    # det = a1*b2 - a2*b1
    # print(f"The determinant of this 2x2 matrix is {det}")
else:
    print("Choose A or B")
#Completed