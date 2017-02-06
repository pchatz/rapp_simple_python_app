#!/usr/bin/env python

import time
import sys

from rapp_robot_api import RappRobot
rh = RappRobot()
from RappCloud import RappPlatformAPI
ch = RappPlatformAPI()

rh.audio.setVolume(50)
rh.motion.enableMotors()
rh.audio.speak("Hello")
rh.motion.disableMotors()



