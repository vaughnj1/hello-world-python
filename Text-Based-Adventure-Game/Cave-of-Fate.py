# James Vaughn
# Cave of Fate
# Being stuck in a cave you woke up in, you must fight or flee your way out. 
# Will you find your way through, uncover the cave's secrets, or be lost forever?  
# Main function to start the game
def start_game():
    print("You wake up to find yourself in a cold, dark cave. The air is damp, and the faint echo of dripping water fills your ears.")
    print("To your left, a narrow tunnel leads deeper into darkness. The air is colder there, and you can faintly hear the sound of rushing water.")
    print("To your right, a wider passage seems to have some light coming from it. The source of the light is unclear, but you hear distant whispers.")
    
    first_choice()

# First decision point
def first_choice():
    choice = input("Do you go left (1) or right (2)? ")
    
    if choice == "1":
        go_left()
    elif choice == "2":
        go_right()
    else:
        print("Invalid input, please try again.")
        first_choice()

# Path for going left
def go_left():
    print("You decide to brave the narrow, dark tunnel, following the sound of rushing water...")
    print("After a while, you come across a river blocking your path.")
    second_choice_left()

# Path for going right
def go_right():
    print("You choose to investigate the wider passage, drawn by the mysterious light and whispers...")
    print("As you move forward, you find a glowing artifact on a pedestal.")
    second_choice_right()

# Second decision if the player chose left
def second_choice_left():
    choice = input("Do you try to swim across the river (1), or follow the riverbank (2)? ")
    
    if choice == "1":
        swim_across()
    elif choice == "2":
        follow_riverbank()
    else:
        print("Invalid input, please try again.")
        second_choice_left()

# Second decision if the player chose right
def second_choice_right():
    choice = input("Do you touch the glowing artifact (1), or ignore it and keep walking (2)? ")
    
    if choice == "1":
        touch_artifact()
    elif choice == "2":
        keep_walking()
    else:
        print("Invalid input, please try again.")
        second_choice_right()

# Path if the player tries to swim across the river
def swim_across():
    print("You bravely attempt to swim across the rushing river...")
    print("But the current is too strong!")
    ending_1()

# Path if the player follows the riverbank
def follow_riverbank():
    print("You follow the riverbank and discover a small, hidden boat.")
    choice = input("Do you take the boat (1), or ignore it and keep walking along the river (2)? ")
    
    if choice == "1":
        take_boat()
    elif choice == "2":
        ignore_boat()
    else:
        print("Invalid input, please try again.")
        follow_riverbank()

# Path if the player touches the artifact
def touch_artifact():
    print("You touch the glowing artifact...")
    print("Suddenly, the world around you disappears, and you find yourself in a mystical realm!")
    ending_4()

# Path if the player ignores the artifact and keeps walking
def keep_walking():
    print("You ignore the artifact and continue down the passage.")
    print("Soon, you encounter a group of strange beings who seem to be guarding something.")
    choice = input("Do you approach the beings (1), or flee (2)? ")
    
    if choice == "1":
        approach_beings()
    elif choice == "2":
        flee_from_beings()
    else:
        print("Invalid input, please try again.")
        keep_walking()

# Path if the player takes the boat
def take_boat():
    print("You get into the boat and begin to paddle downstream...")
    print("Eventually, you sail safely out of the cave and find your way to freedom!")
    ending_2()

# Path if the player ignores the boat and keeps walking
def ignore_boat():
    print("You continue walking along the riverbank, but the path becomes more and more difficult to follow.")
    print("You notice a small, hidden tunnel entrance that seems to lead somewhere.")
    choice = input("Do you enter the secret tunnel (1), or keep following the river (2)? ")
    
    if choice == "1":
        secret_tunnel()
    elif choice == "2":
        keep_following_river()
    else:
        print("Invalid input, please try again.")
        ignore_boat()

# New path if the player enters the secret tunnel
def secret_tunnel():
    print("You enter the secret tunnel and find an underground sanctuary.")
    ending_7()

# New path if the player keeps following the river
def keep_following_river():
    print("You keep following the river but eventually collapse from exhaustion.")
    ending_3()

# Path if the player approaches the beings
def approach_beings():
    print("You cautiously approach the strange beings...")
    print("They seem to recognize you and guide you to a hidden exit.")
    choice = input("Do you trust them (1), or ask more questions (2)? ")
    
    if choice == "1":
        ending_5()
    elif choice == "2":
        ask_questions()
    else:
        print("Invalid input, please try again.")
        approach_beings()

# New path if the player asks more questions
def ask_questions():
    print("You ask the beings more questions, but they seem agitated...")
    print("Suddenly, they turn hostile!")
    ending_8()

# Path if the player flees from the beings
def flee_from_beings():
    print("You panic and run away from the beings, but you become hopelessly lost in the cave.")
    ending_6()

# Different endings
def ending_1():
    print("\nEnding 1: The current sweeps you away, and the cave claims you. You are never seen again.")
    play_again()

def ending_2():
    print("\nEnding 2: You sail out of the cave and find your way to freedom. Congratulations!")
    play_again()

def ending_3():
    print("\nEnding 3: Lost and exhausted, you wander the cave endlessly. Eventually, you are forgotten.")
    play_again()

def ending_4():
    print("\nEnding 4: You are transported to a mystical realm, where you begin a new adventure in an unknown world.")
    play_again()

def ending_5():
    print("\nEnding 5: The beings help you find a hidden exit, and you safely escape the cave.")
    play_again()

def ending_6():
    print("\nEnding 6: You flee in terror, but in doing so, you trap yourself deeper in the cave forever.")
    play_again()

def ending_7():
    print("\nEnding 7: You find peace in the sanctuary, living out your days in tranquility.")
    play_again()

def ending_8():
    print("\nEnding 8: The beings turn hostile, and you meet a grim end in the cave.")
    play_again()

# Function to ask the player if they want to play again
def play_again():
    choice = input("\nDo you want to play again? (yes/no) ")
    
    if choice.lower() == "yes":
        start_game()
    elif choice.lower() == "no":
        print("Thank you for playing! Goodbye.")
    else:
        print("Invalid input, please try again.")
        play_again()

# Start the game for the first time
start_game()
