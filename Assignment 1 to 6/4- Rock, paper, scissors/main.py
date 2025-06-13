import random
print("Welcome to the Rock, Paper, Scissors Game! ")

choices = ["rock", "paper", "scissor"]
user_score = computer_score = 0
print("Let\'s play!")

while True:
    user_input = input("Type rock, paper, scissor or Q to quit: ").lower()
    if user_input == 'q':
        print(f'Final score - you: {user_score}, computer: {computer_score}')
        print("Thanks for playing! ")
        break
    if user_input not in choices:
        print("Invalid input, please try again. ")
        continue
    computer_select = random.choice(choices)
    print(f'Computer select {computer_select}. ')
    if user_input == computer_select:
        print(f'It\'s a Tie!' )
    elif (user_input == "rock" and computer_select == "scissor") or \
         (user_input == "paper" and computer_select == "rock") or \
         (user_input == "scissor" and computer_select == "paper"):
        print("You Win! ")
        user_score += 1
    else:
        print("Computer Win! ")
        computer_score += 1

    print(f'Current score - you: {user_score}, computer: {computer_score}')