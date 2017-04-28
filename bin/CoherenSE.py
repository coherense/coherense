# -*- coding: cp1252 -*-

### =============================================
###  MODULE: CoherenSE 
###  DESCRIPTION: CoherenSE Project Class
###  VERSION: 1.0
###  DEVELOPER: Bruno Calado
###  TEAM: AVV
###  DATE: 13-04-2017
###  PRE-REQ:
###      (see classes.py)
###  Copyright 2017 Altran
### =============================================

############################
### --- IMPORTATIONS --- ###
############################
import os
from classes import _ApplicationsHandling
from time import sleep, time
from telnetlib import Telnet


#########################
### --- VARIABLES --- ###
#########################
## GUI Project Location
project_folder = r"E:\Work\CoherenSE\INFRA_R3.3_RC3\bin"

### GUI Applications
from collections import OrderedDict
applications = OrderedDict()
applications["MongoDB"] = {
                            'options' : None,               # Application parameters
                            'wait'    : None,               # Wait Application to Finish
                            }
applications["CseInitDB-3.3.jar"] = {
                            'options' : '--init-DB',        # Application parameters
                            'wait'    : True,               # Wait Application to Finish
                            }
applications["CSEToolchain-3.3.jar"] = {
                               'options' : None,               # Application parameters
                               'wait'    : False,              # Wait Application to Finish
                               }


###############################
### --- CoherenSE CLASS --- ###
###############################

class CoherenSE:
    def __init__ (self):
        self.Apps = _ApplicationsHandling(applications)

## Robot Keywords

    def run(self, ip="localhost", port="8080", timeout="10"):
        self.Apps.run()
        print "Wait for connection..."
        self._wait_for_connection(ip, int(port), int(timeout)*1000)

    def kill(self):
        self.Apps.kill()

    def kill_driver(self, browser):
        driver = {'firefox' : 'geckodriver.exe',
                  'chrome'  : 'chromedriver.exe',
                  'ie'      : 'iedriver'        }[browser.lower()]
        cmd = "taskkill /F /IM %s" % driver
        os.system(cmd)

## Private Keywords

    def _wait_for_connection(self, ip, port, timeout):
        link = Telnet()
        ini = time()
        end = ini * timeout
        status = False
        while not (status or time() > end):
            try:
                link.open(ip, port)
                link.close()
                status = True
            except :
                sleep(1)

