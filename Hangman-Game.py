import random

# Words categorized by themes
word_categories = {
    "Animals": ["elephant", "giraffe", "tiger", "kangaroo", "dolphin"],
    "Countries": ["canada", "brazil", "france", "germany", "india"],
    "Technology": ["python", "internet", "keyboard", "monitor", "algorithm"]
}

# Difficulty levels mapped to number of allowed incorrect guesses
difficulty_levels = {
    "Easy": 8,
    "Medium": 6,
    "Hard": 4
}

# Hangman drawing for up to 8 incorrect guesses
hangman_stages = [
    "",
    "  O  ",
    "  O  \n  |  ",
    "  O  \n /|  ",
    "  O  \n /|\\",
    "  O  \n /|\\\n / ",
    "  O  \n /|\\\n / \\",
    " [O] \n /|\\\n / \\",
    "[O__]\n /|\\\n / \\"
]

def choose_word_and_category():
    category = random.choice(list(word_categories.keys()))
    word = random.choice(word_categories[category])
    return category, word

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def get_difficulty():
    print("Select difficulty level:")
    for level in difficulty_levels:
        print(f"- {level}")
    while True:
        choice = input("Enter difficulty (Easy/Medium/Hard): ").capitalize()
        if choice in difficulty_levels:
            return choice
        print("Invalid choice. Try again.")

def hangman():
    print("🎮 Welcome to Enhanced Hangman Game!")
    difficulty = get_difficulty()
    max_incorrect = difficulty_levels[difficulty]

    category, word = choose_word_and_category()
    guessed_letters = set()
    incorrect_guesses = 0

    print(f"\n📚 Category: {category}")
    print(f"🎯 Difficulty: {difficulty} ({max_incorrect} lives)\n")

    while incorrect_guesses < max_incorrect:
        print("\n" + hangman_stages[incorrect_guesses])
        print("Word: ", display_word(word, guessed_letters))
        print("Guessed Letters:", " ".join(sorted(guessed_letters)))

        guess = input("🔤 Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Enter a single alphabet letter.")
            continue
        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct!")
            if all(letter in guessed_letters for letter in word):
                print("\n🎉 You win! The word was:", word)
                return
        else:
            print("❌ Incorrect!")
            incorrect_guesses += 1

    print("\n" + hangman_stages[min(incorrect_guesses, len(hangman_stages)-1)])
    print("💀 You lost! The word was:", word)

# Run the enhanced game
if __name__ == "__main__":
    hangman()
