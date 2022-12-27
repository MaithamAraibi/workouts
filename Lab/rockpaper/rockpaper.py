# Winning Rules of the Rock paper scissor game as follows: 
# Rock vs paper->paper wins 
# Rock vs scissor->Rock wins 
# paper vs scissor->scissor wins

import random
player_turn = (input("Enter a choice (rock, paper, scissors): "))

# random.choice()
gen_action = ['rock', 'paper', 'scissors']
pc_trun = random.choice(gen_action)
print(f"player choice {player_turn}, pc choice {pc_trun}")

if player_turn == pc_trun:
    print(f"Both players selected {player_turn}. Draw")
elif player_turn == "rock":
    if pc_trun == "scissors":
        print("Rock X scissors! You win thir round!")
    else:
        print("Paper X rock! You lost this round!?..?")
elif player_turn == "paper":
    if pc_trun == "rock":
        print("Paper X rock! You win thir round!")
    else:
        print("Scissors cuts paper! You lost this round!?..?")
elif player_turn == "scissors":
    if pc_trun == "paper":
        print("Scissors X Paper! You win thir round!")
    else:
        print("Rock X scissors! You lost this round!?..?")
retry = input("Do you want to play again? (Y/N): ")
if retry != "Y":
    print("Thanks for playing")
        