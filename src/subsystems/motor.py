import wpilib
from wpilib.command.pidsubsystem import PIDSubsystem

import robotmap


class Motor(PIDSubsystem):

    def __init__(self):
        super().__init__(2, 0, 0, name='Motor')

        self.motor = wpilib.TalonSRX(robotmap.portsList.motorID)
        self.encoder = wpilib.Encoder(*robotmap.portsList.encoderID)

    def initDefaultCommand(self):
        pass

    def returnPIDInput(self):
        return self.encoder.getDistance()

    def usePIDOutput(self, output):
        self.motor.pidWrite(output)
