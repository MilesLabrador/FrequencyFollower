from signals import detect_sig
import time

time.sleep(2)
print("slept")
signal_set = detect_sig()
print("signals")
print(signal_set)