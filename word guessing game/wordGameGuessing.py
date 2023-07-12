import random

def get_name():
    name = input("Write your Name please: ")
    print(f"Good luck! {name}")
    return name

def choose_word():
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']
    word = random.choice(words)
    return word

def print_words(words):
    i=1
    for w in words:
        print(f"{i}: {w}")
        i+=1

def play_game():
    name = get_name()
    word = choose_word()
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']
    print_words(words)

    count = 0
    while count < 3:
        guess = input("Enter a word from the above list: ")
        if guess not in words:
            print("Your word is not in the list. Please enter a word from the list.")
            continue
        elif guess == word:
            print("Congratulations, you won!")
            break
        elif 2 - count != 0:
            print(f"You have {2 - count} chance(s) left.")
        else:
            print(f"You lost! The word was {word}.")
        count += 1

play_game()
