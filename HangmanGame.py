import random
words = ["python", "coding", "program", "developer", "hangman"]
secret_word = random.choice(words)
guessed_letters = []
attempts = 6
display_word = ["_"] * len(secret_word)

print("🎯 Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print(" ".join(display_word))
while attempts > 0 and "_" in display_word:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)
    if guess in secret_word:
        print("✅ Correct guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", attempts)

    print(" ".join(display_word))

if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game Over! The word was:", secret_word)
