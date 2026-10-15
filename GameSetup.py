player_name = input("Enter your name:").strip().title();

rooms = { "Entrance Hall":
         {"descrption": "You are at the entrance of an old mansion.",
         "exits": {"north": "Library", "east": "Laboratory"},
         "items": ["brass key"],
         "hint": None
         },
         "Library": {
         "descrption": "Dusty Bookshelves cover the walls.",
         "exits": {"south": "Entrance Hall", "east": "Storage Room"},
         "items": ["silver coin"],
         "hint": "The first object opens the door"
         },
         "Laboratory": {
         "descrption": "Old equipment is scattered around.",
         "exits": {"west": "Entrance Hall", "north": "Storage Room"},
         "items": ["ancient gem"],
         "hint": "The second object bears a kingdom's mark"
         },
         "Storage Room": {
         "descrption": "You find boxes filled with forgetten objects.",
         "exits": {"west": "Library", "south": "Laboratory", "north": "Locked Chamber"},
         "items": ["wooden token"],
         "hint": "The final object shines in many colours."
         },
         "Locked Chambers": {
         "descrption": "A mysterious locked door blocks your path.",
         "exits": {"south": "Storage Room", "north": "Treasure Room"},
         "items": [],
         "hint": None
         },
         "Treasure Room": {
         "descrption": "Congratulations! You found the treasure.",
         "exits": {},
         "items": [],
         "hint": None
         }
        }

inventory = []
visited_rooms = set()
discovered_hints = set()
score = 0
unlocked = False

def show_instructions():
    print("\nWelcome to the lost treasure,",player_name)
    print("\n There are 6 rooms:")
    for room in rooms:
        print("-",room)
    print("\nCommands:")
    print("go north/south/east/west")
    print("look, take item, drop item")
    print("inventory, hints, hint 1")
    print("unlock, score, help, quit")
    print("\nInventory limit: 3 items")
    print("Explore rooms, discover hints and unlock the door.")
    