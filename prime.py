n = int(input("what is n    "))
verifier= False
for i in range(2,int(pow(n,0.5))+1):
    if n%i==0:
        verifier = True
        break
if verifier:
    print(f"{n} is not prime")
else:
    print(f"{n} is prime")
