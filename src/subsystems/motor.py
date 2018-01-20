import wpilib
from wpilib.command.pidsubsystem import PIDSubsystem

import ctre

import robotmap


class Motor(PIDSubsystem):

    def __init__(self):
        super().__init__(2, 0, 0, name='Motor')

        self.motor = ctre.WPI_TalonSRX(1)

        self.encoder = wpilib.Encoder(0, 1)
        self.encoder.setDistancePerPulse(robotmap.portsList.encodersDistancePerPulse)

    def initDefaultCommand(self):
        pass

    def returnPIDInput(self):
        return self.encoder.getDistance()

    def usePIDOutput(self, output):
        self.motor.pidWrite(output)
