import random

# ASCII art for each stage (6 lives to 0)
stages = [
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """
]

# Word list
word_list = ["python", "hangman", "developer", "challenge", "keyboard"]
chosen_word = random.choice(word_list)
word_display = ['_'] * len(chosen_word)
guessed_letters = set()
lives = 6

print("🎮 Welcome to Hangman with ASCII Art!")

while lives > 0 and '_' in word_display:
    print(stages[6 - lives])  # Show current stage
    print(f"Word: {' '.join(word_display)}")
    print(f"Lives left: {lives}")
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[i] = guess
        print("✅ Good guess!")
    else:
        lives -= 1
        print("❌ Wrong guess!")

# Final result
print(stages[6 - lives])
if '_' not in word_display:
    print(f"\n🎉 You won! The word was: {chosen_word}")
else:
    print(f"\n💀 You lost. The word was: {chosen_word}")
