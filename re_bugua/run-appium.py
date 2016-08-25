#__author__ = 'yuelian'
#-*- coding: utf-8 -*-
import os
import subprocess
import time

a = subprocess.Popen('appium --session-override', shell=True)
a.wait()
# time.sleep(5)
# a.kill()
