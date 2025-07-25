# This is my Rock Paper Scissors Game
import random
print("Welcome to the best Rock Paper Scissors Game")

player_choice = input("Please select an option ('rock', 'paper', 'scissor')")
print("USER CHOSE:", player_choice)

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print("COMPUTER CHOSE:", computer_choice)

