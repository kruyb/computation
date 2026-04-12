Q = input("choose what to calculate:\nA)simple interest \nB) Compund Interest      ")
if Q == "a" or  "A":
    p = float(input("Enter principle amount "))
    r = float(input("Enter rate %   "))
    t = float(input("Enter time in years    "))
    SI = p*r*t/100
    A = p + SI
    print(f"Your interest is: {SI} \nYour final amount is: {A} ")
elif Q == "B" or "b":
    p = float(input("Enter principle amount"))
    r = float(input("Enter rate %   "))
    t = float(input("Enter time in years    "))
    A = p * pow(1+(r/100),t)
    CI = A - p
    print(f"Your interest is: {CI} \nYour final amount is: {A} ")