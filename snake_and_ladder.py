import random

def ladder(current_value, increment):
    return current_value + increment

def snake(current_value, decrement):
    return current_value - decrement

a = 0
b = 0

print("Welcome to Snake and Ladder!")
while a < 100 and b < 100:
    # Player A turn
    input("Player A: Press Enter to roll the dice...")
    roll_a = random.randint(1, 6)
    if a + roll_a <= 100:
        a += roll_a
        print(f"Player A rolled {roll_a}, reached {a}")
        if a == 25:
            a = ladder(a, 23)
            print("Player A got a ladder! Now at", a)
        if a == 47:
            a = snake(a, 10)
            print("Player A got bitten by a snake! Now at", a)
        if a == 100:
            print("Player A wins!")
            break
    else:
        print("Player A rolled too high, staying at", a)

    # Player B turn
    input("Player B: Press Enter to roll the dice...")
    roll_b = random.randint(1, 6)
    if b + roll_b <= 100:
        b += roll_b
        print(f"Player B rolled {roll_b}, reached {b}")
        if b == 25:
            b = ladder(b, 23)
            print("Player B got a ladder! Now at", b)
        if b == 47:
            b = snake(b, 10)
            print("Player B got bitten by a snake! Now at", b)
        if b == 100:
            print("Player B wins!")
            break
    else:
        print("Player B rolled too high, staying at", b)