# Task 4 - Rock Paper Scissors Game
# CodSoft Python Internship - Azhaan Azam

import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_choices(user, computer):
    emojis = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
    print(f"\nYou chose:      {emojis[user]} {user.upper()}")
    print(f"Computer chose: {emojis[computer]} {computer.upper()}")

print("===== Rock Paper Scissors Game =====")

user_score = 0
computer_score = 0
ties = 0

while True:
    print("\n1. Rock 🪨")
    print("2. Paper 📄")
    print("3. Scissors ✂️")
    print("4. Show Score")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == '5':
        print(f"\n🏆 Final Score:")
        print(f"   You: {user_score} | Computer: {computer_score} | Ties: {ties}")
        print("Thanks for playing! Goodbye! 👋")
        break

    elif choice == '4':
        print(f"\n📊 Current Score:")
        print(f"   You: {user_score} | Computer: {computer_score} | Ties: {ties}")

    elif choice in ('1', '2', '3'):
        moves = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        user_choice = moves[choice]
        computer_choice = get_computer_choice()

        display_choices(user_choice, computer_choice)

        winner = get_winner(user_choice, computer_choice)

        if winner == 'tie':
            print("🤝 It's a TIE!")
            ties += 1
        elif winner == 'user':
            print("🎉 YOU WIN!")
            user_score += 1
        else:
            print("💻 COMPUTER WINS!")
            computer_score += 1

    else:
        print("❌ Invalid choice! Please enter 1-5.")