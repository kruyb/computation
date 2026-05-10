k = int(input("Enter an integer k: "))
n = int(input("Enter an natural number n: "))

if n>=1:
    residue = k%n
    print(f"{k}≡{residue}(mod{n})")
else:
    print("n must be a natural number")