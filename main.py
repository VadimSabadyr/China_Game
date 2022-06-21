sticks = int(input("Number: "))
user1 = input("name user 1: ")
user2 = input("name user 2: ")

while sticks > 0:
    step1 = int(input(f"Your step {user1}! : "))
    if step1 >= 4 or step1 <= 0:
        print("You can take 1, 2, 3 sticks!")
    elif step1 <= 3 and sticks >= 1:
        sticks = sticks - step1
    if sticks < 0:
        sticks = sticks + step1
        print("Wrong step!!! ")
    print(f"Sticks left {sticks}!")
    if sticks == 0:
        print(f"You win {user1}, Congratulations!")
        break

    step2 = int(input(f"Your step {user2}! : "))
    if step2 >= 4 or step2 <= 0:
        print("You can take 1, 2, 3 sticks!")
    elif step2 <= 3:
        sticks = sticks - step2
    if sticks < 0:
        sticks = sticks + step2
        print("Wrong step!!!")
    print(f"Sticks left {sticks}!")
    if sticks == 0:
        print(f"You win {user2}, Congratulations!")
        break
