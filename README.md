# STPM Coldboot Auto

## Note

**Should set the scaling in advance to prevent unexpected situations.**

**Full_HD scaling should be 125%**

**4K resolution scaling should be 250%**


## How to use it
* Run stress_coldboot_STPM.exe as administrator.


## Folder hierarchy
* STPM_V2.5.1.0(Build_01021743)
  * ITPM_DriverUpdate_20190313
* pic
* clear_log.cmd
* stress_coldboot_STPM.exe

## What is the application capable of ?
* Turn off the user access control(UAC) automatically.
* Update the ITPM driver by ifself.
* Using less steps to set up STPM coldboot compared to the original one.

## Others
* The application is written by Python using Pyautogui module.