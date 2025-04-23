import time

def countdown(seconds, note):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print(f"\n⏰ Time's up! Reminder: {note}")

# Get input from user
try:
    user_input = int(input("Enter countdown time in seconds: "))
    reminder_note = input("Enter a reminder note: ")
    countdown(user_input, reminder_note)
except ValueError:
    print("Please enter a valid number of seconds.")
