# -*- coding: cp1252 -*-

### =============================================
###  MODULE: (GUI_data) 
###  DESCRIPTION: AUT data file
###  VERSION: 1.0
###  DEVELOPER: Bruno Calado
###  TEAM: AVV
###  DATE: 13-04-2017
###  Copyright 2017 Altran
### =============================================

############################
### --- IMPORTATIONS --- ###
############################
from classes import Page, AUT

########################
### --- AUT DATA --- ###
########################

### GUI Server
App = AUT(host="localhost", port="8080", browser="Firefox")


##########################
### --- LOGIN PAGE --- ###
##########################

login = Page("Login")
#login.add(name="logo"    , type="img"   , locator="id=login-logo", isopen=True)
login.add(name="username", type="input" , locator="id=username", isopen=True)
login.add(name="password", type="input" , locator="id=password")
login.add(name="submit"  , type="button", locator="xpath=//button[text()='Log in']")


############################
### --- COMMUN PAGES --- ###
############################

### --- HEADER --- ###
header = Page("Header")
header.add(name="username"  , type="text"   , locator="xpath=//span[@class='ng-binding'][text()='${username}']", isopen=True)
header.add(name="logout"    , type="element", locator="xpath=//span[@uib-tooltip='Logout']")
header.add(name="defimp_tab", type="tab"    , locator="xpath=//a[@uib-tooltip='Import Definition']")
header.add(name="sdp_tab"   , type="tab"    , locator="xpath=//a[@uib-tooltip='Service Definition Project']")
header.add(name="sip_tab"   , type="tab"    , locator="xpath=//a[@uib-tooltip='Service Implementation Project']")
header.add(name="vsd_tab"   , type="tab"    , locator="xpath=//a[@uib-tooltip='Virtual System Definition']")
header.add(name="stp_tab"   , type="tab"    , locator="xpath=//a[@uib-tooltip='System Topology Project']")

### --- STATUSBAR --- ###
statusbar = Page("Status Bar")
statusbar.add(name="wait"     , type="text", locator="xpath=//div[@class='cg-busy-default-text ng-binding']")
statusbar.add(name="errors"   , type="list", locator=['Error', 'Invalid'])
statusbar.add(name="error_msg", type="text", locator="xpath=//span[@class='lineText ng-binding'][contains(text(),'${msg}')]")
statusbar.add(name="ok_msg"   , type="text", locator="xpath=//span[text()='Operation has succeeded']")

### --- TOOLBAR --- ###
toolbar = Page("Toolbar")
toolbar.add(name="submit" , type="element", locator="xpath=//span[@translate='SUBMIT']")
toolbar.add(name="publish", type="element", locator="xpath=//span[@translate='PUBLISH']")


##########################
### --- ADMIN PAGE --- ###
##########################

    ### --- USER ADMIN PAGE --- ###
user_admin = Page("User administration")
user_admin.add(name="self_tab"        , type="tab"     , locator="xpath=//span[@translate='USER_ADMINISTRATION']"                    , isself=True)
user_admin.add(name="title"           , type="text"    , locator="xpath=//span[@class='ng-scope'][text()='Administration interface']", isopen=True)
user_admin.add(name="new_user"        , type="button"  , locator="xpath=//button[@class='btn btn-glyphText']")
user_admin.add(name="username"        , type="input"   , locator="id=inputName")
user_admin.add(name="password"        , type="input"   , locator="id=inputPassword")
user_admin.add(name="confirm_password", type="input"   , locator="id=inputPasswordConfirm")
user_admin.add(name="defimp_field"    , type="checkbox", locator="xpath=//input[@type='checkbox'][@ng-model='newUser.isDefImporter']")
user_admin.add(name="sdp_field"       , type="checkbox", locator="xpath=//input[@type='checkbox'][@ng-model='newUser.isSDPLeader']")
user_admin.add(name="sip_field"       , type="checkbox", locator="xpath=//input[@type='checkbox'][@ng-model='newUser.isSIPLeader']")
user_admin.add(name="vsd_field"       , type="checkbox", locator="xpath=//input[@type='checkbox'][@ng-model='newUser.isVSDLeader']")
user_admin.add(name="stp_field"       , type="checkbox", locator="xpath=//input[@type='checkbox'][@ng-model='newUser.isSTPLeader']")
user_admin.add(name="submit"          , type="button"  , locator="xpath=//button[@class='btn btn-fd-main pull-right'][@type='submit']")
user_admin.add(name="user_column"     , type="text"    , locator="xpath=(//table)[1]//tr[td[text()='${username}']]")
user_admin.add(name="defimp_column"   , type="checkbox", locator="xpath=((//table)[1]//tr[td[text()='${username}']]//input)[1]")
user_admin.add(name="sdp_column"      , type="checkbox", locator="xpath=((//table)[1]//tr[td[text()='${username}']]//input)[2]")
user_admin.add(name="sip_column"      , type="checkbox", locator="xpath=((//table)[1]//tr[td[text()='${username}']]//input)[3]")
user_admin.add(name="vsd_column"      , type="checkbox", locator="xpath=((//table)[1]//tr[td[text()='${username}']]//input)[4]")
user_admin.add(name="stp_column"      , type="checkbox", locator="xpath=((//table)[1]//tr[td[text()='${username}']]//input)[5]")

### --- ADMIN HOME PAGE --- ###
admin_home = Page("Administration interface")
admin_home.add(name="user_admin", type="page", locator=user_admin)

###########################
### --- LEADER PAGE --- ###
###########################

        ## --- IMPORT A FILE DIALOG --- ###
import_dialog = Page("Import a File")
import_dialog.add(name="title"   , type="text"   , locator="File Upload", isopen=True) # Firefox
#import_dialog.add(name="title"  , type="text"   , locator="Open"       , isopen=True) # Chrome
import_dialog.add(name="filename", type="input"  , locator="1148")
import_dialog.add(name="open"    , type="button" , locator="1")

        ## --- TAG DEFINITIONS DIALOG --- ###
tag_dialog = Page("Tag Definitions")
tag_dialog.add(name="tag"    , type="input" , locator="id=tag", isopen=True)
tag_dialog.add(name="publish", type="button", locator="xpath=//button[@class='btn btn-primary']")

    ### --- IMPORT DEFINITIONS TAB --- ###
impdef_leader = Page("Import Definition")
impdef_leader.add(name="import_dialog"  , type="page"   , locator=import_dialog)
impdef_leader.add(name="tag_dialog"     , type="page"   , locator=tag_dialog)
impdef_leader.add(name="title"          , type="txt"    , locator="xpath=//span[@class='ng-scope'][text()='Import Definition']", isopen=True)
impdef_leader.add(name="browse"         , type="element", locator="xpath=//span[text()='Choose file']")
impdef_leader.add(name="import_"        , type="button" , locator="xpath=//button[@class='btn btn-fd-main pull-right']")

            ### --- LEADER NEW PROJECT SUBTAB --- ###
leader_newproj = Page("Leader New Project")
leader_newproj.add(name="title"    , type="element", locator="xpath=//span[@translate='NEW_PROJECT'][text()='New project']", isopen=True)
leader_newproj.add(name="proj_name", type="input"  , locator="xpath=//input[@name='sipName']")
leader_newproj.add(name="proj_desc", type="input"  , locator="id=Commenttextarea")
leader_newproj.add(name="users"    , type="select" , locator="xpath=//select[@class='form-control ng-pristine ng-untouched ng-valid ng-empty']")
leader_newproj.add(name="user_add" , type="button" , locator="xpath=//button[@class='btn btn-fd-main']")
leader_newproj.add(name="platform" , type="select" , locator="xpath=//select[@class='form-control ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']")
leader_newproj.add(name="create"   , type="button" , locator="xpath=//button[@class='btn btn-save']")

            ### --- SIP ITEMS SUBPAGE --- ###
leader_sip_item = Page("SIP Items")
leader_sip_item.add(name="self_tab" , type="tab"   , locator="xpath=//a[@uib-tooltip='Items']", isself=True)
leader_sip_item.add(name="title"    , type="text"  , locator="xpath=//span[@translate='ELEMENTS'][text()='Items']", isopen=True)
leader_sip_item.add(name="set_servs", type="button", locator="xpath=//button[@class='btn btn-default dropdown-toggle sip-search-opt']")
leader_sip_item.add(name="set_item" , type="text"  , locator="xpath=//span[@class='ng-scope'][text()='${service}']")
leader_sip_item.add(name="search"   , type="button", locator="xpath=//button[@class='btn btn-fd-main']")
leader_sip_item.add(name="add_item" , type="button", locator="xpath=//table//span[@class='ng-binding'][contains(text(),'${item}')]/../../../..//button")
leader_sip_item.add(name="implement", type="text"  , locator="xpath=//table//span[text()='${implementation}']/../../../..//span[contains(text(),'${item}')]")

            ### --- SIP ASSGNMENT SUBPAGE --- ###
leader_assign = Page("SIP Items")
leader_assign.add(name="self_tab", type="tab"   , locator="xpath=//a[@uib-tooltip='Assignment']", isself=True)
leader_assign.add(name="title"   , type="text"  , locator="xpath=//span[@translate='ASSIGNMENT'][text()='Assignment']", isopen=True)
leader_assign.add(name="tab"     , type="tab"   , locator="xpath=//li[@data-target='${tab}']")
leader_assign.add(name="set_user", type="select", locator="xpath=(//table//tr/td//span[contains(text(),'${item}')]/following::td/select)[1]")

        ### --- LEADER PROJECTS SUBTAB --- ###
leader_projs = Page("Leader Projects")
leader_projs.add(name="newproj" , type="page"   , locator=leader_newproj)
leader_projs.add(name="items"   , type="page"   , locator=leader_sip_item)
leader_projs.add(name="assign"  , type="page"   , locator=leader_assign)
leader_projs.add(name="self_tab", type="tab"    , locator="xpath=//span[@translate='LEADER_PROJECTS']", isself=True)
leader_projs.add(name="new_proj", type="element", locator="xpath=//span[@translate='NEW_PROJECT']"    , isopen=True)
leader_projs.add(name="projs"   , type="table"  , locator="xpath=(//table[@class='table table-dataGrid mono'])[1]")
leader_projs.add(name="proj"    , type="row"    , locator="xpath=(//table[@class='table table-dataGrid mono'])[1]/tbody//tr/td[//span[contains(text(),'${project}')]]")

    ### --- SERVICE IMPLEMENTATIONS PROJECT TAB --- ###
sip_leader = Page("Service Implementation Project")
sip_leader.add(name="title"      , type="text", locator="xpath=//span[@translate='DASHBOARD']", isopen=True)
sip_leader.add(name="leader_proj", type="page", locator=leader_projs)

### --- LEADER HOME PAGE --- ###
leader_home = Page("Leader interface")
leader_home.add(name="impdef_tab", type="page", locator=impdef_leader)
leader_home.add(name="sip_tab"   , type="page", locator=sip_leader)

###########################
### --- WORKER PAGE --- ###
###########################

        ### --- SYNCHRONIZE PAGE --- ###
sip_sync_worker = Page("SIP Synchronize")
sip_sync_worker.add(name="title"  , type="text"  , locator="xpath=//span[@translate='SYNCHRONIZE']", isopen=True)
sip_sync_worker.add(name="compare", type="select", locator="xpath=//select[@class='form-control ng-pristine ng-untouched ng-valid ng-empty']")
sip_sync_worker.add(name="sync"   , type="button", locator="//button[@class='btn btn-save pull-right']")

    ### --- SERVICE IMPLEMENTATIONS PROJECT TAB --- ###
sip_worker = Page("Service Implementation Project")
sip_worker.add(name="sync_page", type="page"  , locator=sip_sync_worker)
sip_worker.add(name="title"    , type="text"  , locator="xpath=//span[@translate='DASHBOARD']", isopen=True)
sip_worker.add(name="row_proj" , type="text"  , locator="xpath=//table//tr//td//span[contains(text(),'${project}')]")
sip_worker.add(name="sync"     , type="button", locator="xpath=(//table//tr/td//span[contains(text(),'${project}')]/following::td/button)[1]")
sip_worker.add(name="discard"  , type="button", locator="xpath=(//table//tr/td//span[contains(text(),'${project}')]/following::td/button)[2]")


#sip_worker.add(name="", type="txt", locator="xpath=")

### --- WORKER HOME PAGE --- ###
worker_home = Page("Worker interface")
worker_home.add(name="sip_tab", type="page", locator=sip_worker)




### PAGES ###

'''
worker_home = {
              'sync_title'              : "xpath=//span[@translate='SYNCHRONIZE']",
              'status_title'            : "xpath=//span[@translate='STATUS']",
              'properties_tab'          : "xpath=//a[text()='Properties']",
              'status_tab'              : "xpath=//a[text()='Status']",
              'properties_title'        : "xpath=//span[@translate='PROPERTIES']",
              'properties_services_tab' : "xpath=//span[@translate='${tab}']",
              'properties_meta_tab'     : "xpath=//table//span[contains(text(),'${item}')]/../../../../..//span[@translate='METADATA_FROM_USERS']",
              'properties_items'        : "xpath=//table//span[contains(text(),'${item}')]",
              'properties_cpu'          : "xpath=//table//span[contains(text(),'${item}')]/../../../../..//span[@translate='CPU_MIPS']/../../..//input",
              'properties_mem'          : "xpath=//table//span[contains(text(),'${item}')]/../../../../..//span[@translate='MEMORY_KB']/../../..//input",
              'properties_cpu_set'      : "xpath=//table//span[contains(text(),'${item}')]/../../../../..//span[@translate='CPU_MIPS']/../../..//button",
              'properties_mem_set'      : "xpath=//table//span[contains(text(),'${item}')]/../../../../..//span[@translate='MEMORY_KB']/../../..//button",
              'set_ok_msg'              : "xpath=//span[text()='Operation has succeeded']",
              'submit_button'           : "xpath=(//button[@class='btn btn-cancel'])[2]",
              'status_services_tab'     : "xpath=//span[@translate='${tab}']",
              'status_items_to_submit'  : "xpath=(//table//span[contains(text(),'${item}')]/../../..//input)[2]",
              'project_sync_button'     : "xpath=(//table//span[contains(text(),'${project}')]/../../..//button)[1]",
              'project_discard_button'  : "xpath=(//table//span[contains(text(),'${project}')]/../../..//button)[2]",
              }

sip_tab = {
          'project_assignment_tab'       : "xpath=//a[@class='headerViews'][text()='Assignment']",
          'project_assignment_tab_title' : "xpath=//span[@translate='ASSIGNMENT']",
          'project_assign_tabs'          : "",
          'project_assign_table'         : "(//table[@class='table table-dataGrid mono'])[${table_id}]",
          'project_assign_button'        : "",
          }

admine_home = {
       'profile_columns'        : ["name", "defimp", "sdp", "sip", "vsd", "stp"],
       'table_rows'             : "//tbody[@class='ng-scope']",
       'table_column'           : "xpath=((//tbody[@class='ng-scope'])[${row}]/tr/td)",
       'table_profile_checkbox' : "xpath=((//tbody[@class='ng-scope'])[${user_row}]/tr/td)[${column}]/input",
       }
leader_home = {
              'sip_tab'                  : "xpath=//a[@class='projectHeaderViews'][text()='SIP']",
              'project_sync_button'      : "xpath=(//table//span[contains(text(),'${project}')]/../../..//button)[1]",
              'project_publish_button'   : "xpath=(//table//span[contains(text(),'${project}')]/../../..//button)[2]",
              'project_discard_button'   : "xpath=(//table//span[contains(text(),'${project}')]/../../..//button)[3]",
              'sync_title'               : "xpath=//span[@translate='SYNCHRONIZE']",
              'sync_compare_with'        : "xpath=//select[@class='form-control ng-pristine ng-untouched ng-valid ng-empty']",
              'sync_button'              : "xpath=//button[@class='btn btn-save pull-right']",
              'back_to_dashboard_button' : "id=headerBurger",
              'dashboard_title'          : "xpath=//span[@translate='DASHBOARD']"
              }
'''



#"//tr[td[text()='Leader']]//input[@ng-model='u.isSDPLeader']")



