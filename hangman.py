import random
words = ["python", "computer", "program", "keyboard", "internet"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6
display = ["_"] * len(word)
print("================================")
print("HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_wrong and "_" in display:

    print("\nWord:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong)

    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether letter is in the word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

if "_" not in display:
    print("\nCongratulations!")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)