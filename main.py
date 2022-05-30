sticks = int(input("Number: "))
user1 = input("name user 1: ")
user2 = input("name user 2: ")

while sticks > -5:
    step1 = int(input(f"Your move {user1}! : "))
    if step1 >= 4:
        print("You can't take more than 3 sticks!")
        pass
    if step1 <= 3:
        sticks = sticks - step1
    print(f"Stikcs left {sticks}!")
    if sticks < 0:
        sticks = sticks + step1
        print("Wrong step!!!")
        print(f"Stikcs left {sticks}!")
    if sticks == 0:
        print(f"You win {user1}, Congratulations!")
        break


    step2 = int(input(f"Your move {user2}! : "))
    if step2 >= 4:
        print("You can't take more than 3 sticks!")
        pass
    if step2 <= 3:
        sticks = sticks - step2
    print(f"Stikcs left {sticks}!")
    if sticks < 0:
        sticks = sticks + step2
        print("Wrong step!!!")
        print(f"Stikcs left {sticks}!")
    if sticks == 0:
        print(f"You win {user2}, Congratulations!")
        break
