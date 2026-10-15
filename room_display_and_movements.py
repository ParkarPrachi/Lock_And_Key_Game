def show_room(current_room):
    global score

    room=rooms[current_room]
    print("\n--",current_room,"--")
    print(room['description'])
    print('exits:',','.join(room['exits'])or 'none')
    if current_room not in visited_rooms:
        visited_rooms.add(current_room)
        score +=10
        print("+10 points for discovering a new room!")
        print("Current score:",score)
def move_player(current_room,direction):
    global unlocked
    if direction not in rooms[current_room]["exists"]:
        print("you cannot go that way.")
        return current_room
    if cuurent_room=='Locked Chamber' and direction=="north":
        if not unlocked:
            print("The door is locked. Collect the required items.")
            return current_room
        return rooms[current_room]['exists'][direction]

    





    