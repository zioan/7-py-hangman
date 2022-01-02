import random
from words import word_list
from art import stages, logo

game_over = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)
print(chosen_word)


display = []
for letter in range(word_length):
    display += '_'

print(display)


while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("Game over. You lose!")
            print(f"Corect answer is: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])
    print(display)
