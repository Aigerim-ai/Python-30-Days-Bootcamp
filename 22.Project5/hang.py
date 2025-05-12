import random

# ASCII art for each stage (6 lives to 0)
STAGES = [
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
WORD_LIST = ["python", "hangman", "developer", "challenge", "keyboard"]

def choose_word():
    return random.choice(WORD_LIST)

def display_status(word_display, guessed_letters, lives):
    print(STAGES[6 - lives])
    print(f"Word: {' '.join(word_display)}")
    print(f"Guessed Letters: {' '.join(sorted(guessed_letters))}")
    print(f"Lives Left: {lives}\n")

def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single alphabet letter.")
        elif guess in guessed_letters:
            print("🔁 Letter already guessed.")
        else:
            return guess

def update_display(chosen_word, word_display, guess):
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            word_display[i] = guess

def play_hangman():
    chosen_word = choose_word()
    word_display = ['_'] * len(chosen_word)
    guessed_letters = set()
    lives = 6

    print("🎮 Welcome to Hangman with ASCII Art!\n")

    while lives > 0 and '_' in word_display:
        display_status(word_display, guessed_letters, lives)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in chosen_word:
            update_display(chosen_word, word_display, guess)
            print("✅ Good guess!\n")
        else:
            lives -= 1
            print("❌ Wrong guess!\n")

    # Final status
    display_status(word_display, guessed_letters, lives)
    if '_' not in word_display:
        print(f"🎉 You won! The word was: {chosen_word}")
    else:
        print(f"💀 You lost. The word was: {chosen_word}")

if __name__ == "__main__":
    play_hangman()
