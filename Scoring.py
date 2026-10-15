def show_score():
    print("Your current score:", score)


def main():
    current_room = "Entrance Hall"
    show_instructions()
    show_room(current_room)

    while True:
        command = input("\n> ").strip().lower()

        if command == "quit":
            print("Thanks for playing!")
            break

        elif command == "help":
            show_instructions()

        elif command == "look":
            show_room(current_room)

        elif command.startswith("go "):
            direction = command[3:].strip()
            new_room = move_player(current_room, direction)

            if new_room != current_room:
                current_room = new_room
                show_room(current_room)

                if current_room == "Treasure Room":
                    global_score = score + 50
                    print("You won!", player_name)
                    print("Final score:", global_score)
                    break

        elif command.startswith("take "):
            take_item(command[5:].strip(), current_room)

        elif command.startswith("drop "):
            drop_item(command[5:].strip(), current_room)

        elif command == "inventory":
            show_inventory()

        elif command.startswith("inspect "):
            inspect_item(command[8:].strip())

        elif command == "hints":
            show_hints()

        elif command.startswith("hint "):
            try:
                read_hint(int(command[5:].strip()))
            except ValueError:
                print("Enter a valid hint number.")

        elif command == "unlock":
            if current_room == "Locked Chamber":
                try_unlock()
            else:
                print("You must be at the locked chamber.")

        elif command == "score":
            show_score()

        else:
            print("Invalid command. Type help for instructions.")


if __name__ == "__main__":
    main()