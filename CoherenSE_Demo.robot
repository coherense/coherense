*** Settings ***
Suite Setup       Start
Suite Teardown    Finish
Test Teardown
Resource          bin/CoherenSE_resource.txt

*** Variables ***

*** Test Cases ***
SIP00
    [Documentation]    *Title :* Open
    Open Application
    Comment    Login as "Trolha"

SIP01
    [Documentation]    *Title :* Create User
    Login as "Admin"
    Add New User as "Trolha"
    Verify "Trolha" User Creation
    Add New User as "Mestre"
    Verify "Mestre" User Creation
    Log Out

SIP02
    [Documentation]    *Title :* Import Definitions
    Login as "Mestre"
    Import Definitions from "ValidJSONSForTest.zip" File
    Publish Definitions With Tag "Etiqueta"

SIP03
    [Documentation]    *Title :* Create Project
    Create a New Project with Name "Obras"

SIP04
    [Documentation]    *Title :* Add Items to Project
    Select Project with Name "Obras"
    Add to Project "Obras" an "ID" "CodeGenTCM_AppWatchdog"
    Add to Project "Obras" an "ID" "ITL1_POLICY"
    Add to Project "Obras" an "ID" "Itl3"
    Add to Project "Obras" an "Item" "DataPublisherSvc"
    Add to Project "Obras" an "Item" "IgnitionSvc"
    Add to Project "Obras" an "Item" "CodeGenTCM_AppWatchdog"
    Add to Project "Obras" an "Item" "Itl_Pol_Action_DoNothing"
    Submit

SIP05
    [Documentation]    *Title :* Assign Items to Users
    Navigate to    ${leader_home.sip_tab.leader_proj.assign}
    Assign Project "Obras" Item "DataPublisherSvc" to User "Trolha"
    Assign Project "Obras" Item "IgnitionSvc" to User "Trolha"
    Assign Project "Obras" Item "CodeGenTCM_AppWatchdog" to User "Trolha"
    Assign Project "Obras" Item "Itl_Pol_Action_DoNothing" to User "Trolha"
    Submit
    Log Out
    Login as "Trolha"
    Verify Project "Obras" Assignment

SIP06
    [Documentation]    *Title :* Synchronize Project
    Syncronize "Obras" With "Obras r6.0"

SIP07
    [Documentation]    *Title :* Add Metadata
    Select Project with Name "Obras"
    Comment    Select Project Properties with Name "Project1"
    Comment    Set Metadata to Item "DataPublisherSvc"
    Comment    Set Metadata to Item "IgnitionSvc"
    Comment    Set Metadata to Item "CodeGenTCM_AppWatchdog"
    Comment    Set Metadata to Item "Itl_Pol_Action_DoNothing"
    Comment    Navivate to Status Tab
    Comment    Set to Submission the Item "DataPublisherSvc"
    Comment    Set to Submission the Item "IgnitionSvc"
    Comment    Set to Submission the Item "CodeGenTCM_AppWatchdog"
    Comment    Set to Submission the Item "Itl_Pol_Action_DoNothing"
    Comment    Submit Metadata
    Comment    Log Out
    Comment    Login as "Leader"
    Comment    Navigate to SIP Tab
    Comment    Syncronize "Project1" With "Project1 r7.0" as "Leader"

SIP08
    [Documentation]    *Title :* Discard Project
    Select SIP Project with name "Project1"
    Add Item "DoorSvc" of "Services definitions" to Project
    Navigate Back
    Discard Project "Project1"
    Log Out

SIP99
    [Documentation]    *Title :* Create User
    Login as "Admin"
    Add New User as "Asdrubal"
    Verify "Asdrubal" User Creation
    Log Out

*** Keywords ***
