import random

game_count = 0 

def play_rps():
    global game_count
    print("\n=== Rock Paper Scissors ===")

    while True:
        user = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        while user not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Try again.")
            user = input("Choose Rock, Paper, or Scissors: ").strip().lower()

        computer = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'scissors' and computer == 'paper') or \
             (user == 'paper' and computer == 'rock'):
            print("You win!")
        else:
            print("You lose!")

        game_count += 1
        print(f"Games played: {game_count}")

        if not play_again("Rock Paper Scissors"):
            break

def number_game():
    global game_count

    while True:
        print("\n=== Guess the Number (1 to 10) ===")
        number = random.randint(1, 10)
        tries = 3

        while tries > 0:
            guess = input(f"Try #{4 - tries} - Enter your guess: ")
            if not guess.isdigit():
                print("Please enter a number.")
                continue

            guess = int(guess)
            if guess < 1 or guess > 10:
                print("Number must be between 1 and 10.")
                continue

            if guess == number:
                print("You guessed it! You win!")
                break
            elif guess < number:
                print("Too low.")
            else:
                print("Too high.")

            tries -= 1

        if tries == 0 and guess != number:
            print(f"You're out of tries! The number was {number}.")

        game_count += 1
        print(f"Games played: {game_count}")

        if not play_again("Guess the Number"):
            break

def play_again(game_name):
    answer = input(f"\nDo you want to play {game_name} again? (yes/no): ").strip().lower()
    return answer == 'yes'

def main_menu():
    print("\n=== Game Menu ===")
    print("1. Rock Paper Scissors")
    print("2. Guess the Number (1 to 10)")
    choice = input("Choose a game (1 or 2): ").strip()

    if choice == '1':
        play_rps()
    elif choice == '2':
        number_game()
    else:
        print("Invalid choice. Try again.")
        main_menu()

    if input("\nDo you want to return to the main menu? (yes/no): ").strip().lower() == 'yes':
        main_menu()
    else:
        print("Thanks for playing!")

main_menu()

