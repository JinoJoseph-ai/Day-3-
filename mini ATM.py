bala = 10000

def dep(bala, depo):
    bala = bala + depo
    return bala

def withd(bala, wi):
    if wi > bala:
        print("Insufficient balance!")
        return bala       
    else:
        return bala - wi

while True:
    print("\nWelcome to ATM!")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    x = int(input("Enter: "))
    
    if x == 1:
        print(f"Your balance is: {bala}")
    elif x == 2:
        depo = int(input("Enter deposit amount: "))
        bala = dep(bala, depo)
        print(f"New balance: {bala}")
    elif x == 3:
        wi = int(input("Enter withdraw amount: "))
        bala = withd(bala, wi)
        print(f"New balance: {bala}")
    elif x == 4:
        print("Goodbye! 👋")
        break