import wpilib
from commandbased import CommandBasedRobot

import subsystems


class MyRobot(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()

        wpilib.LiveWindow.addActuator("Subsystem", "Motor", subsystems.motor.motor)
        wpilib.LiveWindow.addSensor("Subsystem", "Encoder", subsystems.motor.encoder)
        wpilib.LiveWindow.addActuator("Subsystem", "PID Controller", subsystems.motor.getPIDController())


    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass

    def testInit(self):
        pass

    def testPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(MyRobot)
