# -*- coding: cp1252 -*-

### =============================================
###  MODULE: (Classes) 
###  DESCRIPTION: CoherenSE project classes definition
###  VERSION: 1.0
###  DEVELOPER: Bruno Calado
###  TEAM: AVV
###  DATE: 13-04-2017
###  PRE-REQ:
###      https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/
###      pip install psutil
###  Copyright 2017 Altran
### =============================================

############################
### --- IMPORTATIONS --- ###
############################
import os, psutil
from subprocess import Popen
from time import sleep
from win32serviceutil import StopService, StartService, QueryServiceStatus

#########################
### --- VARIABLES --- ###
#########################

## GUI Project Location
project_folder = r"E:\Work\CoherenSE\INFRA_R3.3_RC3\bin"


##########################################
### --- APPLICATION HANDLING CLASS --- ###
##########################################

class _ApplicationHandling:
    def __init__ (self, app_name, app_attributes):
        self.app = app_name
        self.options = app_attributes['options']
        self.wait = app_attributes['wait']
        self.type = self._get_type()
        self.job = None

    def _get_type(self):
        _, ext = os.path.splitext(self.app)
        if len(ext) < 1 : return 'service'
        else : return ext[1:].lower()

    def set_job(self, job):
        self.job = job

###########################################
### --- APPLICATIONS HANDLING CLASS --- ###
###########################################

class _ApplicationsHandling:
    def __init__ (self, apps):
        self.apps = [_ApplicationHandling(app, apps[app]) for app in apps]

    def run(self):
        for app in self.apps:
            self._launch(app)
            self._waiting(app)

    def kill(self):
        for app in self.apps:
            if not app.job is None:
                parent = psutil.Process(app.job.pid)
                children = parent.children(recursive=True)
                for child in children:
                    child.kill()
                    psutil.wait_procs(children, timeout=5)
                try:
                    parent.kill()
                    parent.wait(5)
                except:
                    pass
            elif app.type == 'service':
                exec(self._build_service_cmd(app.app, False))
          

    def _launch(self, app):
        cmd = self._build_general_cmd(app)
        if not cmd is None : exec(cmd)
        try:
            app.set_job(job)
        except:
            pass
        sleep(1)

    def _build_general_cmd(self, app):
        if app.type == 'service' : cmd = self._build_service_cmd(app.app, True)
        else : cmd = self._build_app_cmd(app)
        return cmd

    def _build_app_cmd(self, app):
        if app.type == 'jar' : app_cmd = ["cmd", "/c", "cd", project_folder, "&&", 'java', '-jar', app.app]
        else : app_cmd = [app.app]
        if not app.options is None : app_cmd.append(app.options)
        cmd = "job = Popen(%s)" % app_cmd
        return cmd

    def _build_service_cmd(self, service, state):
        mode = [1, 4][state] #[STOP, START]
        _, service_state, _, _, _, _, _ = QueryServiceStatus(service)
        if service_state == mode: return None
        if state : cmd = "job = StartService('%s')" % service
        else : cmd = "job = StopService('%s')" % service
        return cmd

    def _waiting(self, app):
        if app.wait :
            app.job.wait()
            app.set_job(None)


#############################
### --- ELEMENT CLASS --- ###
#############################
            
class Element:
    def __init__ (self, name, type, locator=None, text=None):
        self.name    = name
        self.id      = locator
        self.txt     = text
        self.type    = type

    
##########################
### --- PAGE CLASS --- ###
##########################
            
class Page:
    def __init__ (self, name):
        self.name   = name
        self.isopen = None
        self.isself = None

    def add(self, name, type, locator, text=None, isopen=False, isself=False):
        if type.lower()=='page':
            element = locator
        else:
            element = Element(name=name, type=type.lower(), locator=locator, text=text)
            if isopen :  self.isopen = element
            if isself :  self.isself = element
        cmd = "self.%s = element" % name
        exec(cmd)
            

##########################
### --- USER CLASS --- ###
##########################

class User:
    def __init__ (self, name, password, role, defimp=None, sdp=None, sip=None, vsd=None, stp=None):
        self.name = name
        self.password = password
        self.role = role
        self.defimp = defimp
        self.sdp = sdp
        self.sip = sip
        self.vsd = vsd
        self.stp = stp


#############################
### --- PROJECT CLASS --- ###
#############################
class Item:
    def __init__ (self, name, service, assign=None, cpu=None, ram=None):
        self.name = name
        self.service = service
        self.assign = assign
        self.cpu = cpu
        self.ram = ram
        
class Service:
    def __init__ (self, name, implementation, tab=None, h2=None):
        self.name = name
        self.impl = implementation
        self.tab = tab
        self.h2 = h2

class Project:
    def __init__ (self, name, description, users, platform):
        self.name = name
        self.desc = description
        self.os = platform
        self.users = users 
        self.serv = list()
        self.defs = list()
        self.ids = list()
            
    def add_serv (self, name, implementation, tab=None, h2=None):
        self.serv.append(Service(name=name, implementation=implementation, tab=tab, h2=h2))
       
    def add_def (self, name, service, cpu=None, ram=None):
        service = [serv for serv in self.serv if serv.name == service][0]
        self.defs.append(Item(name=name, service=service, cpu=cpu, ram=ram))

    def add_id (self, name, service):
        service = [serv for serv in self.serv if serv.name == service][0]
        self.ids.append(Item(name=name, service=service))

    def get_itemserv_data(self, item_name):
        item = [item for item in self.defs if item.name == item_name][0]
        service = [serv for serv in self.serv if serv.name == item.service.name][0]
        return (service.name, service.impl, service.tab, service.h2)

    def get_idserv_data(self, item_name):
        item = [item for item in self.ids if item.name == item_name][0]
        service = [serv for serv in self.serv if serv.name == item.service.name][0]
        return (service.name, service.impl, service.tab, service.h2)
       
#########################
### --- AUT CLASS --- ###
#########################

class AUT:
    def __init__ (self, host, port, browser='Chrome'):
        self.server =  "http://%s:%s" % (host, port)
        self.browser = browser
        self.host = host
        self.port = port
