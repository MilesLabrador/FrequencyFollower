from client import *
import time
from motorConfig import *
from eyeball import *

car = Car()
YIELD_DISTANCE = 18 # Minimum distance that we'll keep between sensor and object
deg_90 = 1
deg_180 = deg_90 * 2

while True:
    current_signal = detect_sig()
    starting_signal = current_signal
    if get_distance() < YIELD_DISTANCE: # if front blocked
        car.rotate("left", deg_90) # left rotate
        if get_distance() < YIELD_DISTANCE: # if left blocked
            car.rotate("left", deg_180) # 180 turn
            car.forwards(1) # forward
        else:
            car.forwards(1) #forward
            current_signal = detect_sig()
            if (current_signal < starting_signal): # if signal is worse
                car.rotate("left", deg_180)
                car.forwards(1) # undo last forwards. Backtrack
                car.forwards(1)
    else:
        car.forwards(1)
        current_signal = detect_sig()
        if (current_signal < starting_signal): # if signal is worse, turn left and run algorithm
            car.rotate("left", deg_90)