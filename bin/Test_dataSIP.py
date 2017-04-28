# -*- coding: cp1252 -*-

### =============================================
###  MODULE: (Test_data) 
###  DESCRIPTION: TCs data file
###  VERSION: 1.0
###  DEVELOPER: Bruno Calado
###  TEAM: AVV
###  DATE: 13-04-2017
###  Copyright 2017 Altran
### =============================================

############################
### --- IMPORTATIONS --- ###
############################
from classes import User, Project


#####################
### --- USERS --- ###
#####################

Admin  = User(name="Admin" , password="admin" , role="administrator")
Leader = User(name="Leader", password=""      , role="leader"       )
Worker = User(name="Worker", password=""      , role="worker"       )
Trolha = User(name="Trolha", password="obras" , role="worker"       , defimp=False, sdp=False, sip=False, vsd=False, stp=False)
Mestre = User(name="Mestre", password="obras" , role="leader"       , defimp=True, sdp=True, sip=True, vsd=True, stp=True)
Asdrubal = User(name="Carpiteiro", password="obras" , role="leader"       , defimp=True, sdp=False, sip=True, vsd=False, stp=False)

########################
### --- PROJECTS --- ###
########################
Obras = Project("Obras", "Santa Engracia", ["Trolha"], "imx6-sabrelite:integrity")

Obras.add_serv(name="Services definitions"       , implementation="Service implementation"        , tab="#tabServices"     , h2="SERVICES")
Obras.add_serv(name="Watchdogs definitions"      , implementation="Watchdog implementation"       , tab="#tabWatchdogs"    , h2="WATCHDOGS")
Obras.add_serv(name="Policies action definitions", implementation="Policies action implementation", tab="#tabPolicyActions", h2="POLICIES_ACTIONS")
Obras.add_serv(name="Watchdogs IDs"              , implementation="Watchdogs IDs")
Obras.add_serv(name="Policies IDs"               , implementation="Policies IDs")
Obras.add_serv(name="Interlocks IDs"             , implementation="Interlocks IDs")

Obras.add_def(name="DataPublisherSvc"        , service="Services definitions"       , cpu="50", ram="256")
Obras.add_def(name="IgnitionSvc"             , service="Services definitions"       , cpu="51", ram="257")
Obras.add_def(name="CodeGenTCM_AppWatchdog"  , service="Watchdogs definitions"      , cpu="52", ram="258")
Obras.add_def(name="Itl_Pol_Action_DoNothing", service="Policies action definitions", cpu="53", ram="259")
Obras.add_def(name="DoorSvc"                 , service="Services definitions"       , cpu="54", ram="260")

Obras.add_id(name="CodeGenTCM_AppWatchdog", service="Watchdogs IDs")
Obras.add_id(name="ITL1_POLICY"           , service="Policies IDs")
Obras.add_id(name="Itl3"                  , service="Interlocks IDs")


