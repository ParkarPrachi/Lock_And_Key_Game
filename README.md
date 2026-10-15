# Lock and Key

## Project Overview

**Lock and Key** is a console-based Python text adventure game.

The player explores different rooms, finds clues, collects keys, solves confusing clue-based puzzles, and opens the correct doors to reach the treasure room.

The game is completely played in the terminal by typing commands.

---

## Problem Statement

Build a text-based adventure game where the player moves through connected rooms, collects clues and keys, solves puzzles, opens locked doors, and reaches the final treasure room to win the game.

---

## Game Story

The player is trapped inside a mysterious building.

To escape and win the treasure, the player must explore six rooms, find three confusing clues, collect three keys, and unlock three final doors.

Each clue leads to a key. At the end, the player must use the correct keys to open the final doors. If even one door is opened incorrectly, the player must go back, understand the clue again, and try the correct key.

---

## Rooms in the Game

The game has six rooms:

1. Entrance Hall
2. Library
3. Laboratory
4. Storage Room
5. Locked Chamber
6. Treasure Room

Each room contains:
- A room description
- Available exits
- Clues or items
- Possible actions

---

## Game Concept

The player starts in the **Entrance Hall**.

The player must explore the rooms and solve three clues:

- Clue 1 gives Key 1
- Clue 2 gives Key 2
- Clue 3 gives Key 3

At the end, the player reaches a place with three locked doors.

The player must open all three doors correctly. If the player uses the wrong key for any door, they must go back, read the clue again, and solve it properly.

After opening all three doors correctly, the player enters the **Treasure Room** and wins the game.

---

## Features

- Console-based gameplay
- Six connected rooms
- Room descriptions and exits
- Three clue-based puzzles
- Three keys
- Three locked doors
- Inventory system
- Help command
- Wrong key handling
- Win condition
- Invalid command handling

---

## Commands

The player can use commands such as:

```text
go north
go south
go east
go west
look
take key
take clue
inventory
read clue
use key
help
quit
