from types import SimpleNamespace
import math


constantsList = SimpleNamespace()

portsList.motorID = 1
portsList.encoderID = [0, 1] # Digital IO Channels for the Encoder

portsList.encodersDistancePerPulse = (math.pi * 8 / 360)
