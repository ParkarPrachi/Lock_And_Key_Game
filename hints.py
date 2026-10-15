def show_hints():
    available = []
    for room_name, room in rooms.items():
        if room['hint'] and room_name in visited_rooms:
            available.append(room_name)

    if not available:
        print("Explore more rooms to unlock hints!")
    else:
        for i, room_name in enumerate(available, 1):
            print(f"Hint{i}: Found in {room_name}")


def read_hint(number):
    global score
    available = [
        name
        for name, room in rooms.items()
        if room['hint'] and name in visited_rooms
    ]
    if number < 1 or number > len(available):
        print("Invalid hint number.")
        return

    room_name = available[number - 1]
    if room_name not in discovered_hints:
        discovered_hints.add(room_name)
        score += 5
        print("+5 points for discovering a hint!")

    print(rooms[room_name]['hint'])


def try_unlock():
    global unlocked, score

    required = {"brass key", "silver coin", "ancient gem"}
    if unlocked:
        print("the door is already unlocked.")
        return

    correct = inventory.copy()
    correct_items = [item for item in correct if item in required]
    wrong_items = [item for item in correct if item not in required]

    print("correct items:", correct_items or "none")
    print("wrong items:", wrong_items or "none")

    if required.issubset(set(correct_items)) and not wrong_items:
        unlocked = True
        score += 30
        print("the door is unlocked! +30 points")
    else:
        print("the door remains locked. Review your hints and try again.")
