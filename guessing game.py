import random
n = random.randint(1, 10)
i = 0
while True:
    i += 1
    x = int(input("Guess the number: "))
    if x == n:
        print(f"Correct! You got it in {i} attempts!")
        break
    elif x > n:
        print("Too high! Try again...")
    elif x < n:
        print("Too low! Try again...")