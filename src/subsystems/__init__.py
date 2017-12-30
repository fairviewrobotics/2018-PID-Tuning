from subsystems.motor import Motor

motor = None

def init():
    global motor

    motor = Motor()
