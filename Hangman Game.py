import random

print("=" * 20)
print("WELCOME TO HANGMAN")
print("=" * 20)

words = ["python", "apple", "computer", "school", "intern"]

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

display_word = []

for letter in secret_word:
    display_word.append("_")

print("\nGuess the Secret Word!")
print("You have", max_attempts, "wrong attempts.\n")

while wrong_guesses < max_attempts:

    print("Word:", " ".join(display_word))
    print("Guessed Letters:", " ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:

        print("✅ Correct Guess!\n")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess

    else:

        wrong_guesses += 1

        print("❌ Wrong Guess!")
        print("Remaining Attempts:", max_attempts - wrong_guesses)
        print()

    if "_" not in display_word:
        print("=" * 20)
        print("✅ YOU WON!")
        print("The word is:", secret_word.upper())
        print("=" * 20)
        break

else:

    print("=" * 20)
    print("❌ GAME OVER!")
    print("The correct word was:", secret_word.upper())
    print("=" * 20)