# Python 2.7
import time
import RPi.GPIO as GPIO

# Use physical pin numberings on GPIO

GPIO.setmode(GPIO.BOARD)

# This command clears the configuration from the GPIO interface
#GPIO.cleanup()

class Motor():
    def __init__(self, forwards_pin, backwards_pin):
        """Initialize pins for forwards and backwards GPIO pin to
        control which input powers the DC motor"""
        GPIO.setmode(GPIO.BOARD)
        self.pinF = forwards_pin
        self.pinB = backwards_pin
        GPIO.setup(self.pinF, GPIO.OUT)
        GPIO.setup(self.pinB, GPIO.OUT)

    def forwards(self):
        """Make motor move backwards by sending high signal to forwards pin"""
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinF, GPIO.OUT)
        GPIO.setup(self.pinB, GPIO.OUT)
        GPIO.output(self.pinF, GPIO.HIGH)
    def backwards(self):
        """Make motor move backwards by sending high signal to backwards pin"""
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinF, GPIO.OUT)
        GPIO.setup(self.pinB, GPIO.OUT)
        GPIO.output(self.pinB, GPIO.HIGH)
    def stop(self):
        """Stop motor by outputting low to both pins"""
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinF, GPIO.OUT)
        GPIO.setup(self.pinB, GPIO.OUT)
        GPIO.output(self.pinF, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.LOW)


class Car():
    def __init__(self):
        # Choose GPIO pins for motor signals and directions
        self.motorBL = Motor(11, 13)
        self.motorBR = Motor(18, 16)
        self.motorFL = Motor(31, 29)
        self.motorFR = Motor(35, 33)

    def forwards(self, duration):
        """Turn all motors forwards for duration seconds"""
        self.motorBL.forwards()
        self.motorBR.forwards()
        self.motorFL.forwards()
        self.motorFR.forwards()

        time.sleep(duration)

        self.motorBL.stop()
        self.motorBR.stop()
        self.motorFL.stop()
        self.motorFR.stop()

    def backwards(self, duration):
        """Turn all motors backwards for duration seconds"""
        self.motorBL.backwards()
        self.motorBR.backwards()
        self.motorFL.backwards()
        self.motorFR.backwards()

        time.sleep(duration)

        self.motorBL.stop()
        self.motorBR.stop()
        self.motorFL.stop()
        self.motorFR.stop()

    def turn(self, direction, duration):
        """Pivot around the pairs of wheels on right and left sides
        to make wider turns"""
        if direction == "right":
            # Turn left motors forward
            self.motorBL.forwards()
            self.motorFL.forwards()

            time.sleep(duration)

            self.motorBL.stop()
            self.motorFL.stop()
        elif direction == "left":
            # Turn right motors forward
            self.motorBR.forwards()
            self.motorFR.forwards()

            time.sleep(duration)

            self.motorBR.stop()
            self.motorFR.stop()
    def rotate(self, direction, duration):
        """Rotate in place by turning wheels on opposite sides
        in opposite directions"""
        if direction == "right":
            # Turn left motors forward
            self.motorBL.forwards()
            self.motorFL.forwards()
            # Turn right motors backward
            self.motorBR.backwards()
            self.motorFR.backwards()

            time.sleep(duration)

            self.motorBL.stop()
            self.motorBR.stop()
            self.motorFL.stop()
            self.motorFR.stop()

        elif direction == "left":
            # Turn left motors backwards
            self.motorBL.backwards()
            self.motorFL.backwards()

            # Turn right motors forwards
            self.motorBR.forwards()
            self.motorFR.forwards()

            time.sleep(duration)

            self.motorBL.stop()
            self.motorBR.stop()
            self.motorFL.stop()
            self.motorFR.stop()
