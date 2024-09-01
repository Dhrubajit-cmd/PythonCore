# Question :
'''
Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system.
'''
import platform
import time
import subprocess


def beep():
    try:
        # Play a short beep sound using paplay
        play_command = 'paplay /usr/share/sounds/freedesktop/stereo/bell.oga'
        result = subprocess.run(play_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if result.returncode != 0:
            raise Exception("paplay command failed")
    except FileNotFoundError:
        print("paplay command not found. Please install it using 'sudo apt-get install pulseaudio-utils'.")
    except Exception as e:
        print(f"Error running paplay command: {e}")


def notify(message):
    # Display notification using notify-send
    try:
        result = subprocess.run(['notify-send', 'Notification', message], check=True)
        if result.returncode != 0:
            raise Exception("notify-send command failed")
    except FileNotFoundError:
        print("notify-send command not found. Please install it using 'sudo apt-get install libnotify-bin'.")
    except Exception as e:
        print(f"Error displaying notification: {e}")


if platform.system() == "Linux":
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(current_time)

        message = "Hey It's been two hours. Take a break and drink water!"
        beep()
        notify(message)

        # Sleep for two hours (7200 seconds)
        time.sleep(7200)
