from flask import Flask
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50)

app = Flask(__name__)

@app.route('/')

def index():
    return 'This is it!'

if(__name__) == '__main__':
    app.run(debug=True, host='0.0.0.0')



@app.route('/move-servo')

def move_servo():
    print('moving servo!')
    servo.start(0)
    time.sleep(1)
    print("rotating")
    duty = 2
    while duty <= 17:
        servo.ChangeDutyCycle(duty)
        time.sleep(1)
        duty = duty + 1
    servo.stop()
    GPIO.cleanup()
    print("all cleared")

    return 'servo moved'
