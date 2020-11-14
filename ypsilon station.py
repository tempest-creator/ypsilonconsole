import time #This  gives the pause in one-second increments.  Keep this!

#Coded by Kyle Ross
#Content by DG Chapman, Sean McCoy, and Quadra
#Layout by Quadra
#Instructions - to use the keycard, have your players type "INSERT SONYA KEYCARD".
#If they want to remove the keycard, have them type "REMOVE SONYA KEYCARD".
#Card can only be inserted and removed from the control screen.
#Feel free to edit anything you want here.  Credit is appreciated but not necessary.

#All syntax options for the choices
Diagnostics = ["DIAGNOSTICS", "Diagnostics", "diagnostics"]
Schedule = ["SCHEDULE", "Schedule", "schedule"]
Controls = ["CONTROLS", "Controls", "controls"]
Roster = ["ROSTER", "Roster", "roster"]
Comms = ["COMMS", "Comms", "comms"]
Layout = ["LAYOUT", "Layout", "layout"]
Status = ["STATUS", "Status", "status"]
Back = ["BACK", "Back", "B", "back"]
More = ["MORE", "More", "more"]
On = ["on", "ON", "On", "ENABLE", "Enable", "enable", "TURN ON", "Turn on", "Turn On", "turn on"]
Off = ["off", "OFF", "Off", "DISABLE", "Disable", "disable"]
System = ["System", "SYSTEM", "system"]
Airlocks = ["Airlocks", "airlocks", "AIRLOCKS"]
Showers = ["Showers", "SHOWERS", "showers"]
Keycard = ["INSERT SONYA KEYCARD", "Insert Sonya Keycard", "insert sonya keycard"]
Deycard = ["REMOVE SONYA KEYCARD", "REMOVE KEYCARD", "TAKE OUT KEYCARD", "take out keycard", "remove sonya keycard", "remove keycard", "Remove Keycard", "Remove Sonya Keycard"]
Lock1 = ["Unlock 1", "UNLOCK 1", "1"]
Scuttle = ["SCUTTLE", "Scuttle", "scuttle"]
Life = ["Life Support", "LIFE SUPPORT", "life support", "Life support"]
Comms = ["Comms", "COMMS", "comms"]
Heracles = ["Heracles", "HERACLES", "heracles", "HAIL RSV THE HERACLES", "Hail RSV The Heracles", "hail rsv the heracles", "HAIL HERACLES", "hail heracles"]
Grasshopper = ["GRASSHOPPER", "Grasshopper", "grasshopper", "HAIL IMV GRASSHOPPER", "Hail IMV Grasshopper", "hail imv grasshopper", "HAIL GRASSHOPPER", "hail grasshopper"]
End = ["END", "END CALL", "End", "End Call", "end", "end call", "End call"]
Download = ["DOWNLOAD", "Download", "download"]
UnlockDock1 = ["UNLOCK DOCK 1", "unlock dock 1", "UNLOCK DOCKING BAY 1", "Unlock docking bay 1", "unlock 1", "UNLOCK 1", "UNLOCK ONE", "unlock docking bay 1"]
UnlockDock2 = ["UNLOCK DOCK 1", "unlock dock 2", "UNLOCK DOCKING BAY 2", "Unlock docking bay 2", "unlock 2", "UNLOCK 2", "UNLOCK TWO", "unlock docking bay 2"]
LockDock1 = ["LOCK DOCK 1", "lock dock 1", "LOCK DOCKING BAY 1", "lock docking bay 1", "LOCK 1", "lock 1", "LOCK ONE", "lock docking bay 1"]
LockDock2 = ["LOCK DOCK 2", "lock dock 2", "LOCK DOCKING BAY 2", "lock docking bay 2", "LOCK 2", "lock 2", "LOCK TWO", "lock docking bay 2"]
LockMine = ["LOCK MINESHAFT", "lock mineshaft", "Lock Mineshaft", "Lock mineshaft", "LOCK MINE", "lock mine", "Lock Mine", "Lock mine", "MINE LOCK"]
UnlockMine = ["UNLOCK MINESHAFT", "unlock mineshaft", "Unlock Mineshaft", "Unlock mineshaft", "UNLOCK MINE", "unlock mine", "Unlock Mine", "Unlock mine", "MINE UNLOCK"]
Shower1 = ["SHOWER 1 ON", "1 ON", "1 on", "ONE ON", "Shower 1 on", "shower 1 on", "one on", "One on", "ON ONE"]
Shower2 = ["SHOWER 2 ON", "2 ON", "2 on", "TWO ON", "Shower 2 on", "shower 2 on", "two on", "Two on", "ON TWO"]
Shower3 = ["SHOWER 3 ON", "3 ON", "3 on", "THREE ON", "Shower 3 on", "shower 3 on", "three on", "Three on", "ON THREE"]
Shower4 = ["SHOWER 4 ON", "4 ON", "4 on", "FOUR ON", "Shower 4 on", "shower 4 on", "four on", "Four on", "ON FOUR"]
Shower5 = ["SHOWER 5 ON", "5 ON", "5 on", "FIVE ON", "Shower 5 on", "shower 5 on", "five on", "Five on", "ON FIVE"]
Dry1 = ["SHOWER 1 OFF", "1 OFF", "1 off", "ONE OFF", "Shower 1 off", "shower 1 off", "one off", "One off", "OFF ONE"]
Dry2 = ["SHOWER 2 OFF", "2 OFF", "2 off", "TWO OFF", "Shower 2 off", "shower 2 off", "two off", "Two off", "OFF TWO"]
Dry3 = ["SHOWER 3 OFF", "3 OFF", "3 off", "THREE OFF", "Shower 3 off", "shower 3 off", "three off", "Three off", "OFF THREE"]
Dry4 = ["SHOWER 4 OFF", "4 OFF", "4 off", "FOUR OFF", "Shower 4 off", "shower 4 off", "four off", "Four off", "OFF FOUR"]
Dry5 = ["SHOWER 5 OFF", "5 OFF", "5 off", "FIVE OFF", "Shower 5 off", "shower 5 off", "five off", "Five off", "OFF FIVE"]
EnableAll = ["LOCK ALL", "lock all", "Lock All", "Lock all", "ALL ON", "ON ALL", "all on", "All on", "on all", "TURN ALL ON", "TURN ALL", "turn all on", "turn all", "ENABLE ALL", "enable all", "Enable All", "Enable all"]
DisableAll = ["UNLOCK ALL", "unlock all", "Unlock All", "Unlock all", "ALL OFF", "OFF ALL", "all off", "All off", "off all", "TURN ALL OFF", "turn all off", "DISABLE ALL", "disable all", "Disable All", "Disable all"]


#Variable Section

GlobalVariables = {
  "life_support_on": True,
  "keycard_supplied": False,
  "shower_1_on": False,
  "shower_2_on": False,
  "shower_3_on": False,
  "shower_4_on": False,
  "shower_5_on": False,
  "dock_1_locked": True,
  "dock_2_locked": False,
  "mineshaft_locked": False
}



required = ("\nUse only A, B, or C\n") #Cutting down on duplication
print ("""__   __        _ _               _____ _        _   _             
\ \ / /       (_) |             /  ___| |      | | (_)            
 \ V / __  ___ _| | ___  _ __   \ `--.| |_ __ _| |_ _  ___  _ __  
  \ / '_ \/ __| | |/ _ \| '_ \   `--. \ __/ _` | __| |/ _ \| '_ \ 
  | | |_) \__ \ | | (_) | | | | /\__/ / || (_| | |_| | (_) | | | |
  \_/ .__/|___/_|_|\___/|_| |_| \____/ \__\__,_|\__|_|\___/|_| |_|
    | |                                                           
    |_|              
FLEET COMMODORE SYSTEMS © 2246 - GUILD LICENSE
PROGRAM OPERATION GROUP SOFTWARE (P.O.G.S.)
----------
WARNING - LICENSE EXPIRED
CONTACT SYSTEMS ADMINISTRATOR
----------
""")
#Console starts with intro"
def intro():
  print ("YPSILON 14 CONTROL TERMINAL")
  time.sleep(1)
  print ("""  >DIAGNOSTICS
  >SCHEDULE
  >CONTROLS
  >ROSTER
  >COMMS
  """)
  choice = input(">>> ") #Here is your first choice.
  if choice in Diagnostics:
    option_diagnostics()
  elif choice in Schedule:
    option_schedule()
  elif choice in Controls:
    option_controls()  
  elif choice in Roster:
    option_roster()
  elif choice in Comms:
    option_comms()
  else:
    print ("SYNTAX ERROR")
    time.sleep(1)
    intro()


def option_comms():
  print ("COMMS")
  time.sleep(1)
  print ("""SCANNING FOR NEARBY SHIPS...
> HAIL RSV THE HERACLES
> HAIL IMV GRASSHOPPER
< BACK""")
  choice = input(">>> ")
  if choice in Heracles:
    option_heracles()
  elif choice in Grasshopper:
    option_grasshopper()
  elif choice in Back:
    intro()
  else:
    print ("SYNTAX ERROR")
    time.sleep(1)
    option_comms()

def option_heracles():
  print ("HAILING RSV THE HERACLES")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print ("""NO ANSWER.
  >BACK""")
  choice = input(">>> ")
  if choice in Heracles:
    option_heracles()
  elif choice in Back:
    option_comms()
  else:
    print ("SYNTAX ERROR")
    time.sleep(1)
    option_comms()

def option_grasshopper():
  print ("HAILING IMV GRASSHOPPER")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print (".")
  print ("""ALEXA: HELLO.  HOW CAN I HELP?
  >END CALL""")
  choice = input(">>> ")
  if choice in Heracles:
    option_heracles()
  elif choice in End:
    option_comms()
  else:
    print ("SYNTAX ERROR")
    time.sleep(1)
    option_comms()

def option_diagnostics(): 
  print ("\nDIAGNOSTICS")
  time.sleep(1)
  print ("""> LAYOUT
> STATUS
< BACK""")
  choice = input(">>> ")
  if choice in Layout:
    option_layout()
  elif choice in Status:
   option_status()
  elif choice in Back:
    intro()
  else:
    print ("SYNTAX ERROR")
    time.sleep(1)
    option_diagnostics()

def option_controls(): 
  print ("\nCONTROLS")
  time.sleep(1)
  print ("""> AIRLOCKS
> SHOWERS
> SYSTEM [A]
< BACK""")
  choice = input(">>> ")
  if choice in Airlocks:
    option_airlocks()
  elif choice in Showers:
   option_showers()
  elif choice in System:
   option_system()
  elif choice in Back:
    intro()
  else:
    print ("SYNTAX ERROR")
    time.sleep(1)
    option_controls()

def option_showers():
  global GlobalVariables
  print ("\nSHOWERS")
  if GlobalVariables["shower_1_on"] == True:
    print ("SHOWER 1 [> ON]")
  else:
    print ("SHOWER 1 [> OFF]")
  if GlobalVariables["shower_2_on"] == True:
    print ("SHOWER 2 [> ON]")
  else:
    print ("SHOWER 2 [> OFF]")
  if GlobalVariables["shower_3_on"] == True:
    print ("SHOWER 3 [> ON]")
  else:
    print ("SHOWER 3 [> OFF]")
  if GlobalVariables["shower_4_on"] == True:
    print ("SHOWER 4 [> ON]")
  else:
    print ("SHOWER 4 [> OFF]")
  if GlobalVariables["shower_5_on"] == True:
    print ("SHOWER 5 [> ON]")
  else:
    print ("SHOWER 5 [> OFF]")
  print (">BACK")
  choice = input(">>> ")
  if choice in Shower1:
   time.sleep(1)
   GlobalVariables["shower_1_on"] = True
   option_showers()
  elif choice in Dry1:
   time.sleep(1)
   GlobalVariables["shower_1_on"] = False
   option_showers()
  elif choice in Shower2:
   time.sleep(1)
   GlobalVariables["shower_2_on"] = True
   option_showers()
  elif choice in Dry2:
   time.sleep(1)
   GlobalVariables["shower_2_on"] = False
   option_showers()
  elif choice in Shower3:
   time.sleep(1)
   GlobalVariables["shower_3_on"] = True
   option_showers()
  elif choice in Dry3:
   time.sleep(1)
   GlobalVariables["shower_3_on"] = False
   option_showers()
  elif choice in Shower4:
   time.sleep(1)
   GlobalVariables["shower_4_on"] = True
   option_showers()
  elif choice in Dry4:
   time.sleep(1)
   GlobalVariables["shower_4_on"] = False
   option_showers()
  elif choice in Shower5:
   time.sleep(1)
   GlobalVariables["shower_5_on"] = True
   option_showers()
  elif choice in Dry5:
   time.sleep(1)
   GlobalVariables["shower_5_on"] = False
   option_showers()
  elif choice in EnableAll:
   time.sleep(1)
   GlobalVariables["shower_1_on"] = True
   GlobalVariables["shower_2_on"] = True
   GlobalVariables["shower_3_on"] = True
   GlobalVariables["shower_4_on"] = True
   GlobalVariables["shower_5_on"] = True
   option_showers()
  elif choice in DisableAll:
   time.sleep(1)
   GlobalVariables["shower_1_on"] = False
   GlobalVariables["shower_2_on"] = False
   GlobalVariables["shower_3_on"] = False
   GlobalVariables["shower_4_on"] = False
   GlobalVariables["shower_5_on"] = False
   option_showers()
  elif choice in Back:
   option_controls()
   
  else:
    print ("SYNTAX ERROR")
    option_showers()

def option_airlocks():
  global GlobalVariables
  print ("\nAIRLOCKS")
  time.sleep(1)
  if GlobalVariables["dock_1_locked"] == True:
    print ("DOCKING BAY 1 [> LOCKED]")
  else:
    print ("DOCKING BAY 1 [> UNLOCKED]")
  if GlobalVariables["dock_2_locked"] == True:
    print ("DOCKING BAY 2 [> LOCKED]")
  else:
    print ("DOCKING BAY 2 [> UNLOCKED]")
  if GlobalVariables["mineshaft_locked"] == True:
    print ("MINESHAFT [> LOCKED]")
  else:
    print ("MINESHAFT [> UNLOCKED]")
  print (">BACK")
  choice = input(">>> ")
  if choice in LockDock1:
   print ("INITIALIZING LOCK.  NOTE - DOOR MUST BE MANUALLY CLOSED FIRST.")
   time.sleep(3)
   GlobalVariables["dock_1_locked"] = True
   option_airlocks()
  elif choice in UnlockDock1:
   print ("UNLOCKING.  NOTE - DOOR MUST BE MANUALLY OPENED AFTER PROCEDURE.")
   time.sleep(3)
   GlobalVariables["dock_1_locked"] = False
   option_airlocks()
  elif choice in LockDock2:
   print ("INITIALIZING LOCK.  NOTE - DOOR MUST BE MANUALLY CLOSED FIRST.")
   time.sleep(3)
   GlobalVariables["dock_2_locked"] = True
   option_airlocks()
  elif choice in UnlockDock2:
   print ("UNLOCKING.  NOTE - DOOR MUST BE MANUALLY OPENED AFTER PROCEDURE.")
   time.sleep(3)
   GlobalVariables["dock_2_locked"] = False
   option_airlocks()
  elif choice in LockMine:
   print ("INITIALIZING LOCK.  NOTE - DOOR MUST BE MANUALLY CLOSED FIRST.")
   time.sleep(3)
   GlobalVariables["mineshaft_locked"] = True
   option_airlocks()
  elif choice in UnlockMine:
   print ("UNLOCKING.  NOTE - DOOR MUST BE MANUALLY OPENED AFTER PROCEDURE.")
   time.sleep(3)
   GlobalVariables["mineshaft_locked"] = False
   option_airlocks()
  elif choice in EnableAll:
   print ("INITIALIZING LOCKS.  NOTE - DOORS MUST BE MANUALLY CLOSED FIRST.")
   time.sleep(3)
   GlobalVariables["dock_1_locked"] = True
   GlobalVariables["dock_2_locked"] = True
   GlobalVariables["mineshaft_locked"] = True
   option_airlocks()
  elif choice in DisableAll:
   print ("UNLOCKING ALL.  NOTE - DOORS MUST BE MANUALLY OPENED AFTER PROCEDURE.")
   time.sleep(3)
   GlobalVariables["dock_1_locked"] = False
   GlobalVariables["dock_2_locked"] = False
   GlobalVariables["mineshaft_locked"] = False
   option_airlocks()   
  elif choice in Back:
   option_controls()
  else:
    print ("SYNTAX ERROR")
    option_airlocks()


def option_system():
  global GlobalVariables
  if GlobalVariables["keycard_supplied"] == True:
   option_system_a()
  else:
   print ("SYSTEM")
  time.sleep(1)
  print ("""[ACCESS DENIED. ADMIN KEYCARD REQUIRED.]
< BACK
  """)
  choice = input(">>> ")
  if choice in Keycard:
    GlobalVariables["keycard_supplied"] = True
    option_system_a()
  elif choice in Back:
    option_controls()
  else:
    print ("SYNTAX ERROR")
    time.sleep(1)
    option_system()


def option_system_a():
  print ("SYSTEM")
  time.sleep(1)
  print ("""[ACCESS GRANTED. WELCOME, SONYA.]
> LIFE SUPPORT
> SCUTTLE
< BACK""")
  choice = input(">>> ")
  if choice in Life:
    option_lifesupport()
  elif choice in Scuttle:
    option_scuttle()
  elif choice in Deycard:
    GlobalVariables["keycard_supplied"] = False
    option_system()  
  elif choice in Back:
    option_controls()
  else:
    print ("SYNTAX ERROR")
    time.sleep(1)
    option_system_a()

def option_scuttle():
  print ("SCUTTLE")
  time.sleep(1)
  print ("""[WARNING: THIS WILL INITIATE A 10-MINUTE STATION SELF-DESTRUCT SEQUENCE.
TYPE 'SCUTTLE' TO INITIATE. SEQUENCE IS IRREVERSIBLE AFTER 5 MINUTES.]
< BACK""")
  choice = input(">>> ")
  if choice in Scuttle:
    time.sleep(2)
    print ("STATION WILL SELF-DESTRUCT IN 15 MINUTES.")
    time.sleep(2)
    print ("IMMEDIATE EVACUATION SUGGESTED.")
    time.sleep(2)
    intro()
  elif choice in Back:
    option_controls()
  else:
    print ("SYNTAX ERROR")
    time.sleep(1)
    option_scuttle()
    


def option_status():
  print ("\nSTATUS")
  time.sleep(1)
  print ("SYSTEMS CHECK ...")
  time.sleep(3)
  print (""" WARNING: AIR FILTERS LAST REPLACED 455 DAYS AGO
(255 DAYS PAST RECOMMENDATION)
WARNING: SHOWER 5 OUT OF ORDER AS OF 1 DAY AGO
WARNING: MINESHAFT ELEVATOR LAST MAINTAINED 455 DAYS AGO
(255 DAYS PAST RECOMMENDATION)
WARNING: AIRFLOW 82%
(SUBOPTIMAL: REPLACE FILTERS AND CHECK VENTS FOR BLOCKAGES)
ALL SYSTEMS WITHIN ACCEPTABLE OPERATING CONDITIONS
< BACK""")
  choice = input(">>> ")
  if choice in Back:
    option_diagnostics()
  elif choice in Status:
    print ("\nYou decided to throw another rock, as if the first " 
    "rock thrown did much damage. The rock flew well over the "
    "orcs head. You missed. \n\nYou died!")
  elif choice in Back:
    intro()
  else:
    print ("SYNTAX ERROR")
    time.sleep(1)
    option_status()
    
def option_roster():
  print ("\nROSTER")
  time.sleep(1)
  print ("""01. VERHOEVEN, SONYA     - OVERSEER
02. SINGH, ASHRAF        - BREAKER
03. DE BEERS, DANA       - HEAD DRILLER
04. HUIZINGA, JEROME     - ASST. DRILLER
05. TOBIN, ROSA          - MINING ENGINEER
06. MIKKELSEN, MICHAEL   - MINING ENGINEER
07. KANTARO, KENJI       - LOADER
08. OBOWE, MORGAN        - LOADER
09. KENBISHI, RIE        - PUTTER
10. VACANT
< BACK """)
  choice = input(">>> ")
  if choice in Back:
    intro()
  elif choice in Back:
    intro()
  else:
    print ("SYNTAX ERROR")
    time.sleep(1)
    option_roster()

def option_schedule():
  print (""" SCHEDULE
2255-07-02 06:33 - IMV GRASSHOPPER    - RESUPPLY - DOCKING BAY 2 - DOCK
2255-06-04 08:34 - RSV THE HERACLES   - RESEARCH - DOCKING BAY 1 - DOCK
2255-06-02 12:23 - CTV HORN OV PLENTY - RESUPPLY - DOCKING BAY 2 - DEPART
2255-06-01 16:04 - CTV HORN OV PLENTY - RESUPPLY - DOCKING BAY 2 - DOCK
2255-05-02 08:32 - MV VASQUEZ XV      - PICKUP   - DOCKING BAY 1 - DEPART
2255-05-01 06:02 - MV VASQUEZ XV      - PICKUP   - DOCKING BAY 1 - DOCK
2255-04-02 13:02 - CTV HORN OV PLENTY - RESUPPLY - DOCKING BAY 2 - DEPART
2255-04-01 15:54 - CTV HORN OV PLENTY - RESUPPLY - DOCKING BAY 2 - DOCK
2255-03-02 08:33 - MV VAZQUEZ XV      - PICKUP   - DOCKING BAY 1 - DEPART
2255-03-01 06:04 - MV VAZQUEZ XV      - PICKUP   - DOCKING BAY 1 - DOCK
< BACK""")
  choice = input(">>> ")
  if choice in Layout:
    option_run()
  elif choice in Back:
    intro()
  else:
    print ("SYNTAX ERROR")
    time.sleep(1)
    option_schedule()



def option_layout():
  print ("\nGENERATING LAYOUT")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print ("""▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓__   _____  ___ ___ _    ___  _  _   _ _ _  ▓
▓\ \ / / _ \/ __|_ _| |  / _ \| \| | / | | | ▓
▓ \ V /|  _/\__ \| || |_| (_) | .` | | |_  _|▓
▓  |_| |_|  |___/___|____\___/|_|\_| |_| |_| ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓ | DOCK 1| DOCK 2|         ▓▓GUILD LICENSE▓▓▓
▓    ] [     ] [            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓  ___X_______X___     ______    _________   ▓
▓ |      =C=      |   |8 |9|0|  | ooo /\  |  ▓
▓ |   WORKSPACE   |___|7     |__| MESS    |  ▓
▓ |               ____     _____  ooo  0  |  ▓
▓ |    \----/     |   |_    1|  |_________|  ▓
▓ |    /MINE\     |   |6   |_|__|  WASH ~~|  ▓
▓ |    \----/     |   |5    ____   ROOM ~~|  ▓
▓ |_______________|   |4|3|2 |  |_|_|_|_|_|  ▓
▓        o↑           QUARTERS               ▓
▓       _o↓_          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓      X___|MINESHAFT ▓        ROSTER        ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 1 SONYA    6 MORGAN  ▓
▓-------LEGEND--------▓ 2 ASHRAF   7 RIE     ▓
▓  X    AIRLOCK       ▓ 3 DANA     8 ROSA    ▓
▓ =C=  COMPUTER       ▓ 4 JEROME   9 MIKE    ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 5 KANTARO  0 N/A     ▓
▓  DOCK 1  ▓  DOCK 2  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓ HERACLES ▓ RESUPPLY ▓VERSION SOFTWARE 2.25B▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  >DOWNLOAD     >BACK""")
  choice = input(">>> ")
  if choice in Download:
   print ("DOWNLOADING...")
   time.sleep(3)
   print ("\nDOWNLOAD COMPLETE.")
   time.sleep(2)
   option_diagnostics()
  elif choice in Back:
   option_diagnostics()
  else:
    print ("SYNTAX ERROR")
    option_diagnostics()
    
def option_lifesupport():
  global GlobalVariables
  print ("\nLIFE SUPPORT")
  time.sleep(1)
  if GlobalVariables["life_support_on"] == True:
    print ("LIFE SUPPORT [> ON]")
  else:
    print ("LIFE SUPPORT [> OFF]")
    print("< BACK")
  choice = input(">>> ")
  if choice in On:
   print ("ENABLING LIFE SUPPORT.  ENSURE WORKERS WAIT FIVE MINUTES BEFORE REMOVING THEIR VACCSUITS.")
   time.sleep(3)
   GlobalVariables["life_support_on"] = True
   print ("\nLIFE SUPPORT ENABLED.")
   time.sleep(2)
   option_lifesupport()
  elif choice in Off:
   print ("DISABLING LIFE SUPPORT.  ENSURE ALL WORKERS ARE WEARING THEIR VACCSUITS.")
   time.sleep(3)
   GlobalVariables["life_support_on"] = False
   print ("\nLIFE SUPPORT DISABLED.")
   time.sleep(2)
   option_lifesupport()
  elif choice in Back:
    option_system_a()
  else:
    print ("SYNTAX ERROR")
    option_lifesupport()


intro()