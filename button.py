import RPi.GPIO as GPIO
import time


BUTTON_PIN = 10   
JOYSTICK_PIN = 11 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(JOYSTICK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0

def debounce_button():
    time.sleep(0.1) 

while True:
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        debounce_button()
        if counter < 2:
            counter += 1
        else:
            counter = 0
            

    if GPIO.input(JOYSTICK_PIN) == GPIO.HIGH:
        debounce_button()
        if counter == 0:
            print("O beautiful for spacious skies, For amber waves of grain, For purple mountain majesties, Above the enameled plain!")
        elif counter == 1:
            print("America,  ! God shed His grace on thee,")
        elif counter == 2:
            print("Till souls wax fair as earth and air And music-hearted sea!")