sticks = int(input("Number: "))
user1 = input("name user 1: ")
user2 = input("name user 2: ")

while sticks > 0:
    step1 = int(input(f"Your move {user1}! : "))
    if step1 >= 4 or sticks <= 0:
        print("You can take 1, 2, 3 sticks!")
    elif step1 <= 3:
        sticks = sticks - step1
    print(f"Stikcs left {sticks}!")
    if sticks == 0:
        print(f"You win {user1}, Congratulations!")
        break

    step2 = int(input(f"Your move {user2}! : "))
    if step2 >= 4 or sticks <= 0:
        print("You can take 1, 2, 3 sticks!")
    elif step2 <= 3:
        sticks = sticks - step2
    print(f"Stikcs left {sticks}!")
    if sticks == 0:
        print(f"You win {user2}, Congratulations!")
        break
