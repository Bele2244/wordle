import sys
import csv
import random
from pyfiglet import figlet_format
from colorama import Fore,Style
# import pyfiglet

def main():
    # Welcome_screen
    print(figlet_format("Wordle"))
    
    print("Chose difficulty or type 'q' to exit\n")
    # Get difficulty if input is valid
    
    user_input = ""
    while(user_input == ""):
        user_input = input("1 - Hard\n2 - Medium\n3 - Easy\n\nNumber: ")
        difficulty = get_difficulty(user_input)
        user_input = difficulty

    print("\nPick the subject or type 'q' to exit\n")
    # Get subject if input is valid
    subject = get_subject()
    # Get random word based on chosen subject
    word = get_word(subject)

    # Start the game
    start_game(word, difficulty)

# Start the game
def start_game(word, difficulty):
    tries = difficulty * 3
    word = word.lower()
    while(True):
        # Reset color output
        print(Style.RESET_ALL)
        word_len = len(word)
        user_guess = input(f"{word_len} letter word: ")
        user_guess = user_guess.lower()

        if user_guess == word:
            print(Fore.GREEN + "You win")
            print(f"The word was: {Fore.GREEN + word.title()}")
            sys.exit(1)
        else:
            guess_attempt = check_word(user_guess, word)
            if guess_attempt == word:
                print(Fore.GREEN + "You win")
                print(f"The word was: {Fore.GREEN + word.title()}")
                sys.exit(1)
            else:
                print(guess_attempt)
                tries -= 1
        if tries == 0:
            print(Fore.RED + "You lose")

            print(f"The word was: {Fore.RED + word.title()}")
            sys.exit(1)
        # Reset color output
        print(Style.RESET_ALL)
        print(f"{tries} tries left")

# Check and color the letters
def check_word(user_guess, word):
    result = "" 

    x = 0
    for guess_letter in user_guess:
        try:
            if guess_letter == word[x]:
                result += Fore.GREEN + guess_letter
            elif guess_letter != word[x]:
                if guess_letter in word:
                    result += Fore.YELLOW + guess_letter
                else:
                    result += Fore.RED + guess_letter
            x += 1
        except IndexError:
            continue
    return result

# Get difficulty if input is valid 
def get_difficulty(user_input):

    if user_input.lower() == 'q':
        sys.exit()
    try:
        user_input = int(user_input)
        if user_input >= 1 and user_input <= 3:
            return user_input
        elif user_input < 1 or user_input > 3:
            print("Invalid input, accepted numbers are:1, 2 or 3")
            return ""
    except ValueError:
        print("Invalid input")
        return ""

# Test user input - return subject if valid
def get_subject():
    subjects = ["animals", "countries", "disney movies", "fruits", "vegetables"]
    flag = 1
    while(flag):

        # Print available subjects
        i = 1
        index = 0
        for subject in subjects:
            print(str(i) + '.' + subject) 
            i += 1
        # Get user choice
        user_input = input(("\nNumber: "))
        # Quit the program
        if user_input.lower() == 'q':
            print("Program exited successfully")
            sys.exit(1)
        
        if user_input.lower() in subjects:
            flag = 0
        else:
            try:
                user_input = int(user_input)
                if int(user_input) >= 1 and int(user_input) <= 5:
                # send subjects[user_input] to function
                    flag = 0
                    index = int(user_input)
            except ValueError:
                print("Invalid input try again")
        if not flag:
            break

    if index:
        return subjects[index-1]
    else:
        return user_input.lower()

# Get random word from chosen subject
def get_word(subject):
    filename = "subjects/" + subject + ".csv"
    words = load_csv(filename)
    return random.choice(words)

# Load csv file and return it as a list of items
def load_csv(filename):
    subject_list = []
    with open(filename) as f_csv:
        reader_csv = csv.DictReader(f_csv)
        subjects = list(reader_csv)
    for row in subjects:
        subject_list.append(row["name"])
    # Return list of words on chosen subject
    return subject_list

if __name__ == "__main__":
    main()