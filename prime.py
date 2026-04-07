n = int(input("What is n? "))

if n < 2:
    print(f"{n} is not prime")
elif n == 2:
    print(f"{n} is prime")
elif n % 2 == 0:
    print(f"{n} is not prime")
else:
    verifier = False
    for i in range(3, int(pow(n, 0.5)) + 1, 2):
        if n % i == 0:
            verifier = True
            break
    if verifier:
        print(f"{n} is not prime")
    else:
        print(f"{n} is prime")
