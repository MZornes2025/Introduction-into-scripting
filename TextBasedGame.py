# TextBasedGame.py
# Author: Mariana Zornes

import sys


# Function to display instructions
def show_instructions():

    print("Welcome to the Cursed Temple Adventure Game!")
    print("Collect all 6 relics to escape the temple without being caught by the Guardian Spirit.")
    print("Commands:")
    print("  go North, go South, go East, go West")
    print("  get [item name]")
    print("  quit - to exit the game at any time\n")


# Function to show player status
def show_status(current_room, inventory, rooms):

    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    # Show item in the room if available
    if "item" in rooms[current_room]:
        print(f"You see {rooms[current_room]['item']}")
    print("----------------------------")


# Function to restart the game
def restart_game():

    replay = input("Would you like to play again? (yes/no): ").strip().lower()
    if replay == 'yes':
        main()
    else:
        print("Thanks for playing! Goodbye!")
        sys.exit()


# Main function to handle the game
def main():
    # Dictionary linking rooms and items within each room
    rooms = {
        'Entrance Hall': {'North': 'Treasure Vault', 'South': 'Tomb of the Pharaoh', 'East': 'Hall of Mirrors', 'West': 'Garden of Statues', 'item': 'No Relic'},
        'Treasure Vault': {'South': 'Entrance Hall', 'East': "Guardian's Lair", 'item': "Guardian's Lair Key"},
        "Guardian's Lair": {'West': 'Treasure Vault', 'item': 'the Guardian Spirit'},  #Villain's room
        'Garden of Statues': {'East': 'Entrance Hall', 'item': 'Emerald Necklace'},
        'Chamber of Secrets': {'South': 'Hall of Mirrors', 'item': 'Ancient Scroll'},
        'Forgotten Library': {'West': 'Tomb of the Pharaoh', 'item': 'Crystal Skull'},
        'Tomb of the Pharaoh': {'East': 'Forgotten Library', 'North': 'Entrance Hall', 'item': 'Scepter of the Pharaoh'},
        'Hall of Mirrors': {'West': 'Entrance Hall', 'North': 'Chamber of Secrets', 'item': 'Golden Idol'}
    }

    # Initialize game state variables
    inventory = []
    current_room = 'Entrance Hall'
    relics_needed = 6  # Number of relics needed to win
    game_over = False

    # Show game instructions
    show_instructions()

    # Check if player has entered the villain's room
    if current_room == "Guardian's Lair":
        if len(inventory) == relics_needed:
            print("You have all relics and can now defeat the Guardian Spirit!")
            print("Congratulations! You have escaped the temple with all relics!")
            game_over = True
        else:
            print("You encountered the Guardian Spirit without all relics! Game Over.")
            game_over = True

    # Main game loop
    while not game_over:
        # Display the current status of the player
        show_status(current_room, inventory, rooms)

        # Get the player's next move
        move = input("Enter your move: ").split()

        if len(move) < 1:
            print("Invalid command. Please enter a command in the form 'go [direction]', 'get [item]', or 'quit'.")
            continue

        action = move[0].lower()
        target = ' '.join(move[1:])

        # Handle quit command
        if action == "quit":
            print("Thanks for playing! Goodbye!")
            sys.exit()

        # Handle room movement
        elif action == "go":
            # Check if movement direction is valid
            if target in rooms[current_room]:
                current_room = rooms[current_room][target]

                # Check if player has entered the villain's room
                if current_room == "Guardian's Lair":
                    if len(inventory) == relics_needed:
                        print("You have all relics and can now defeat the Guardian Spirit!")
                        print("Congratulations! You have escaped the temple with all relics!")
                        game_over = True
                    else:
                        print("You encountered the Guardian Spirit without all relics! Game Over.")
                        game_over = True
            else:
                print(f"You can't go {target} from {current_room}. Check for valid directions.")


        # Handle item collection
        elif action == "get":
            # Check if the item is in the current room and matches the target item
            if "item" in rooms[current_room] and rooms[current_room]["item"].lower() == target.lower():
                if target not in inventory:
                    # Add item to inventory and remove it from the room
                    inventory.append(rooms[current_room]["item"])
                    print(f"{rooms[current_room]['item']} has been added to your inventory.")
                    del rooms[current_room]["item"]

                    # Check if all relics have been collected
                    if len(inventory) == relics_needed:
                        print("You have collected all relics! Find the Guardians Lair to defeat the Guardian Spirit.")
                else:
                    print("Item already in inventory.")
            else:
                print(f"'{target}' doesn't seem quite right. Make sure you are entering the correct command or word.")

        # Handle invalid commands
        else:
            print("Invalid command. Try again.")

        # Prompt replay if game over
        if game_over:
            restart_game()


# Run the game
if __name__ == "__main__":
    main()
