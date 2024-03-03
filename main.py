# A table to keep the 'X' and 'O'
table = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Keep values which selected before
selected_before = []

# Check is app still working
is_continue = True

# Get names
first_name = input("First Player's name: ")
second_name = input("Second Player's name: ")

# Control mechanism to draw situation
one_to_nine = []
for i in range(1, 10):
    one_to_nine.append(i)


def first_player():
    choice = input(f"{first_name}'s Choice: ")
    # Check choice is integer,between to 1 and 9
    try:
        choice = int(choice)
        if choice in selected_before:
            print("You Choose a value which already choice")
            first_player()
        selected_before.append(choice)

    except ValueError:
        print("You need to choose a number 1 to 9")
        first_player()

    except IndexError:
        print("You need to choose a number 1 to 9")
        first_player()
    # Put the 'X'
    else:
        table[choice] = "X"


def second_player():
    choice = input(f"{second_name}'s Choice: ")

    # Check choice is integer,between to 1 and 9
    try:
        choice = int(choice)
        if choice in selected_before:
            print("You Choose a value which already choice")
            second_player()
        selected_before.append(choice)

    except ValueError:
        print("You need to choose a number 1 to 9")
        second_player()

    except IndexError:
        print("You need to choose a number 1 to 9")
        second_player()
    # Put the 'O'
    else:
        table[choice] = "O"


# Check who is winner and complete the process
def winner():
    global is_continue
    if table[4:7] == ["X", "X", "X"] or table[1:4] == ["X", "X", "X"] or table[7:10] == ["X", "X", "X"] or table[1:8:3] == ["X", "X", "X"] or table[2:9:3] == ["X", "X", "X"] or table[3:10:3] == ["X", "X", "X"] or table[1:10:3] == ["X", "X", "X"] or table[3:8:2] == ["X", "X", "X"]:
        print(f"The winner is {first_name}")
        is_continue = False
    elif table[1:4] == ["O", "O", "O"] or table[4:7] == ["O", "O", "O"] or table[7:10] == ["O", "O", "O"] or table[1:8:3] == ["O", "O", "O"] or table[2:9:3] == ["O", "O", "O"] or table[3:10:3] == ["O", "O", "O"] or table[3:8:3] == ["O", "O", "O"] or table[1:10:3] == ["O", "O", "O"]:
        print(f"The winner is{second_name}")
        is_continue = False
    elif selected_before == one_to_nine:
        print("Nobody won! The result is draw.")
        is_continue = False


# Table Appearance
def table_app():
    print(f"\n {table[1]} | {table[2]} | {table[3]} \n"
          "-----------\n"
          f" {table[4]} | {table[5]} | {table[6]} \n"
          "-----------\n"
          f" {table[7]} | {table[8]} | {table[9]} \n"
          "-----------\n"
          )


# Controlling all function
def control():
    while is_continue:
        table_app()
        first_player()
        winner()
        if is_continue:
            table_app()
            second_player()
            winner()


control()
