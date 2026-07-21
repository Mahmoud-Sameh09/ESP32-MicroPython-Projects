from machine import Pin, PWM, time_pulse_us
import time

# ============================================================
# Hardware Configuration
# ============================================================

# Ultrasonic Sensor Pins
trig = Pin(19, Pin.OUT)
echo = Pin(18, Pin.IN)

# Servo Motor (50 Hz for SG90)
servo = PWM(Pin(5), freq=50)

# Warning LED
led = Pin(15, Pin.OUT)

# Buzzer
buzzer = PWM(Pin(2))
buzzer.freq(1000)

# ============================================================
# Function: Measure Distance
# ============================================================

def dist():
    """
    Measures the distance using the HC-SR04 ultrasonic sensor.

    Returns:
        float : Distance in centimeters.
        None  : If no valid echo is received.
    """

    # Send a 10 µs trigger pulse
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    try:
        # Measure the echo pulse duration
        duration = time_pulse_us(echo, 1)
    except OSError:
        # Return None if the sensor times out
        return None

    # Convert pulse duration to distance (cm)
    distance = (duration * 0.0343) / 2

    return distance


# ============================================================
# Function: Rotate Servo
# ============================================================

def set_angle(angle):
    """
    Rotates the servo motor to the desired angle.

    Args:
        angle (int): Angle between 0° and 180°.
    """

    # Convert angle to PWM duty cycle
    duty = int((((angle / 180) * 2 + 0.5) / 20) * 1023)
    servo.duty(duty)


# ============================================================
# Function: Scan One Angle
# ============================================================

def scan(angle):
    """
    Rotates the servo, measures the distance,
    and activates the alarm if an object is too close.
    """

    # Move servo to the required angle
    set_angle(angle)

    # Give the servo enough time to reach the position
    time.sleep_ms(20)

    # Read the current distance
    distance = dist()

    # Skip invalid readings
    if distance is None:
        return

    # Print angle and distance for debugging
    print(f"Angle: {angle:3d}° | Distance: {distance:.1f} cm")

    # Object detected
    if distance < 20:

        led.on()
        buzzer.duty(512)

        # Stop scanning until the object is removed
        while True:

            distance = dist()

            if distance is None:
                continue

            if distance >= 20:
                break

        # Turn off warning devices
        led.off()
        buzzer.duty(0)
 

# ============================================================
# Main Program
# ============================================================

while True:

    # Make sure everything starts in OFF state
    led.off()
    buzzer.duty(0)

    # Scan from 0° to 180°
    for angle in range(181):
        scan(angle)

    # Scan back from 180° to 0°
    for angle in range(180, -1, -1):
        scan(angle)