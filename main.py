from client import *
import time
from motorConfig import *
from eyeball import *
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
car = Car()
YIELD_DISTANCE = 50 # Minimum distance that we'll keep between sensor and object
deg_90 = 1
deg_180 = deg_90 * 2
step_size = 1
#doubleCheck = False

while True:
    current_signal = detect_sig()
    if(current_signal > 0.01):
        break
    starting_signal = current_signal
    #print(get_distance())
    if get_distance() < YIELD_DISTANCE: # if front blocked
        print("front blocked, going back")
        car.backwards(.5)
        car.rotate("left", deg_90) # left rotate
        if get_distance() < YIELD_DISTANCE: # if left blocked
            print("tried left, blocked")
            car.rotate("left", deg_180) # 180 turn
            car.forwards(step_size) # forward
        else:
            car.forwards(step_size) #forward
            current_signal = detect_sig()
            if (starting_signal/current_signal > 1.1): # if signal is worse
                print("went left, weaker signal, backtrack")
                car.rotate("left", deg_180)
                car.forwards(step_size) # undo last forwards. Backtrack
                car.forwards(step_size)
    else:
        print("front not blocked")
        car.forwards(step_size)
        time.sleep(2)
        current_signal = detect_sig()
        if (starting_signal/current_signal > 1.1): # if signal is worse, turn left and run algorithm
            print("front not blocked, but signal worse")
            #if doubleCheck:
            car.rotate("left", deg_90)
                #doubleCheck = False
            #else:
                #current_signal = starting_signal
                #doubleCheck = True
            #or starting_signal/current_signal < 0.8
        else:
            print("signal better")
GPIO.cleanup()
