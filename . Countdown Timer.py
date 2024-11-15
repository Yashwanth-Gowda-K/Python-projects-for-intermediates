import time
from playsound import playsound

def countdown_timer_with_alarm(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("00:00 - Time's up!")
    playsound('alarm.mp3')  # Replace 'alarm.mp3' with your alarm sound file path

# Example usage:
time_in_seconds = int(input("Enter time in seconds: "))
countdown_timer_with_alarm(time_in_seconds)
