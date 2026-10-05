import random

# Word categories
categories = {
    "animals": ["tiger", "lion", "elephant", "monkey", "giraffe"],
    "sports": ["cricket", "football", "tennis", "hockey", "badminton"],
    "programming": ["python", "javascript", "variable", "function", "computer"]
}

# Welcome screen
print("=" * 50)
print("🎮 WELCOME TO HANGMAN")
print("=" * 50)

# Show categories
print("\nAvailable Categories:")
print("1. Animals")
print("2. Sports")
print("3. Programming")

# Take category choice
choice = input("\nChoose a category (1-3): ")

# Select category
if choice == "1":
    category = "animals"
elif choice == "2":
    category = "sports"
elif choice == "3":
    category = "programming"
else:
    print("Invalid choice! Starting with Animals.")
    category = "animals"

# Select a random word
word = random.choice(categories[category])

# Game variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Hidden word
display_word = ["_"] * len(word)

print("\nCategory:", category.title())
print("The word has", len(word), "letters.")
print("You have", max_wrong_guesses, "wrong guesses.")

# Main game loop
while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))

    if guessed_letters:
        print("Guessed letters:", ", ".join(guessed_letters))
    else:
        print("Guessed letters: None")

    print("❤️ Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("\nEnter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one alphabet letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    # Add letter to guessed list
    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("✅ Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    # Wrong guess
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")

# Game result
print("\n" + "=" * 50)

if "_" not in display_word:
    print("🎉 CONGRATULATIONS!")
    print("You guessed the word:", word)
else:
    print("💀 GAME OVER!")
    print("The correct word was:", word)

print("=" * 50)