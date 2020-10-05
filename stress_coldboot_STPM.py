import os
import time
import pyautogui as p
import sys
import time

def event_log_clean():
	os.chdir(locate)
	os.system("clear_log.cmd")
	print("event log has been deleted.")
	

def Full_HD():
	os.chdir(STPM_ini)
	driver_update_bool = os.path.exists("exist.txt")
	if driver_update_bool == False:
		filebool = open("exist.txt","w")
		filebool.write("1")
		filebool.close()
		os.system("disableUAC.BAT")
		os.startfile("ITPM_DriverUpdate.exe")
		time.sleep(3)
		os.chdir(locate)
		ITPM_update = p.locateCenterOnScreen("pic/ITPM_update.PNG",confidence = 0.8)
		p.click(ITPM_update)
		time.sleep(1)
		ITPM_OK = p.locateCenterOnScreen("pic/ITPM_OK.PNG",confidence = 0.8)
		p.click(ITPM_OK)
		time.sleep(1)
		ITPM_exit = p.locateCenterOnScreen("pic/ITPM_exit.PNG",confidence = 0.8)
		p.click(ITPM_exit)

	os.chdir(plan)
	plan_bool = os.path.exists("STPM_TESTPLAN.PLN")

	if plan_bool == True:
		os.remove("STPM_TESTPLAN.PLN")
		flag = "1"
		print("file delted")
	else:
		flag ="0"

	os.chdir(STPM)
	os.startfile("STPM.exe")
	time.sleep(5)
	os.chdir(locate)
#===============================================#
#====stpm_running?==============================#
	stpm_cancel = p.locateCenterOnScreen("pic/stpm_cancel.PNG",confidence = 0.8)
	p.click(stpm_cancel,clicks = 3)
	time.sleep(2)
	stpm_terminate = p.locateCenterOnScreen("pic/stpm_terminate.PNG",confidence = 0.8)
	p.click(stpm_terminate)
	time.sleep(2)
	stpm_reset = p.locateCenterOnScreen("pic/stpm_reset.PNG",confidence = 0.7)
	p.click(stpm_reset)
	time.sleep(2)

#====stpm_stid press=======
	stpm_stid = p.locateCenterOnScreen("pic/stpm_stid.PNG",confidence = 0.5)
	p.keyDown("ctrl")
	p.keyDown("alt")
	p.click(stpm_stid)
	p.keyUp("alt")
	p.keyUp("ctrl")
	time.sleep(5)
#=====stpm_setup press=======
	stpm_setup = p.locateCenterOnScreen("pic/stpm_setup.PNG",confidence = 0.5)
	p.click(stpm_setup)
	time.sleep(1)
#=====stpm_scanAll============
	if flag == "0":
		stpm_scan_all = p.locateCenterOnScreen("pic/stpm_scan_all.PNG",confidence = 0.8)
		p.click(stpm_scan_all)
		time.sleep(1)
#=====stpm_check_both
		stpm_check_both = p.locateCenterOnScreen("pic/stpm_check_both.PNG",confidence = 0.9)
		p.click(stpm_check_both)
		time.sleep(1)
#=====stpm_check_device
		stpm_check_device = p.locateCenterOnScreen("pic/stpm_check_device.PNG",confidence = 0.8)
		p.click(stpm_check_device)
		time.sleep(1)
		stpm_alert = p.locateCenterOnScreen("pic/stpm_alert.PNG",confidence = 0.8)
		time.sleep(2)
		if stpm_alert is not None:
			p.click(stpm_alert)
	
		time.sleep(1)
#=====stpm_auto_run
		stpm_autorun = p.locateCenterOnScreen("pic/stpm_autorun.PNG",confidence = 0.9)
		p.click(stpm_autorun)
		time.sleep(1)

#=====stpm_edit_plan
	stpm_edit_plan = p.locateCenterOnScreen("pic/stpm_edit_plan.PNG",confidence = 0.9)
	p.click(stpm_edit_plan)
	time.sleep(1)
#=====stpm_test_item===============================
	stpm_test_item = p.locateCenterOnScreen("pic/stpm_test_item.PNG",confidence = 0.9)
	p.click(stpm_test_item)
	time.sleep(2)
	if flag =="1":
		stpm_test_item_wb = p.locateCenterOnScreen("pic/stpm_test_item_wb.PNG",confidence = 0.9)
		p.click(stpm_test_item_wb)
		time.sleep(2)
#=====stpm_coldboot
	stpm_coldboot = p.locateCenterOnScreen("pic/stpm_coldboot.PNG",confidence = 0.8)
	p.click(stpm_coldboot)
	time.sleep(1)
#======stpm_count_down
	stpm_count_down = p.locateCenterOnScreen("pic/stpm_count_down.PNG",confidence = 0.8)
	p.click(stpm_count_down)
	p.typewrite(['backspace','backspace'],interval=0.5)
#alert
	stpm_alert = p.locateCenterOnScreen("pic/stpm_alert.PNG",confidence = 0.8)
	p.click(stpm_alert)
	time.sleep(1)
	p.typewrite(in_count_down_time,interval=0.5)
#=======stpm_sleep_time
	stpm_sleep_time = p.locateCenterOnScreen("pic/stpm_sleep_time.PNG",confidence = 0.8)
	p.click(stpm_sleep_time)
	time.sleep(1)
	p.typewrite(['backspace','backspace'],interval=0.5)
#alert
	stpm_alert = p.locateCenterOnScreen("pic/stpm_alert.PNG",confidence = 0.8)
	p.click(stpm_alert)
	time.sleep(1)
	p.typewrite(in_sleep_time,interval=0.5)
#========stpm_execute_count
	stpm_execute_count = p.locateCenterOnScreen("pic/stpm_execute_count.PNG",confidence = 0.8)
	p.click(stpm_execute_count)
	p.typewrite(['backspace','backspace'],interval=0.5)
#alert
	stpm_alert = p.locateCenterOnScreen("pic/stpm_alert.PNG",confidence = 0.8)
	p.click(stpm_alert)
	time.sleep(1)
	p.typewrite(in_cycles,interval=0.5)
#========stpm_add_new_group
	stpm_add_new_group = p.locateCenterOnScreen("pic/stpm_add_new_group.PNG",confidence = 0.8)
	p.click(stpm_add_new_group)
	time.sleep(1)
#========stpm_save_default_plan
	stpm_save_default_plan = p.locateCenterOnScreen("pic/stpm_save_default_plan.PNG",confidence = 0.8)
	p.click(stpm_save_default_plan)
	time.sleep(1)
#=========stpm_savenexit
	if flag =="1":
		stpm_setup = p.locateCenterOnScreen("pic/stpm_setup.PNG",confidence = 0.5)
		p.click(stpm_setup)
		time.sleep(1)
		stpm_autorun_checked = p.locateCenterOnScreen("pic/stpm_autorun_checked.PNG",confidence = 0.9)
		p.click(stpm_autorun_checked)
		time.sleep(1)
		stpm_autorun = p.locateCenterOnScreen("pic/stpm_autorun.PNG",confidence = 0.9)
		p.click(stpm_autorun)
		time.sleep(1)
		stpm_edit_plan = p.locateCenterOnScreen("pic/stpm_edit_plan.PNG",confidence = 0.9)
		p.click(stpm_edit_plan)
		time.sleep(1)

	stpm_savenexit = p.locateCenterOnScreen("pic/stpm_savenexit.PNG",confidence = 0.8)
	p.click(stpm_savenexit)
	time.sleep(1)

	end_time = time.time()

	print("Time eplased :",end_time- start_time)



def Four_K():
	os.chdir(STPM_ini)
	driver_update_bool = os.path.exists("exist.txt")
	if driver_update_bool == False:
		filebool = open("exist.txt","w")
		filebool.write("1")
		filebool.close()
		os.system("disableUAC.BAT")
		os.startfile("ITPM_DriverUpdate.exe")
		time.sleep(3)
		os.chdir(locate)
		ITPM_update = p.locateCenterOnScreen("pic/ITPM_update_4k.PNG",confidence = 0.8)
		p.click(ITPM_update)
		time.sleep(1)
		ITPM_OK = p.locateCenterOnScreen("pic/ITPM_OK_4k.PNG",confidence = 0.8)
		p.click(ITPM_OK)
		time.sleep(1)
		ITPM_exit = p.locateCenterOnScreen("pic/ITPM_exit_4k.PNG",confidence = 0.8)
		p.click(ITPM_exit)

	os.chdir(plan)
	plan_bool = os.path.exists("STPM_TESTPLAN.PLN")

	if plan_bool == True:
		os.remove("STPM_TESTPLAN.PLN")
		flag = "1"
		print("file delted")
	else:
		flag ="0"

	os.chdir(STPM)
	os.startfile("STPM.exe")
	time.sleep(5)
	os.chdir(locate)
#===============================================#
#====stpm_running?==============================#
	stpm_cancel = p.locateCenterOnScreen("pic/stpm_cancel_4k.PNG",confidence = 0.8)
	p.click(stpm_cancel,clicks = 3)
	time.sleep(2)
	stpm_terminate = p.locateCenterOnScreen("pic/stpm_terminate_4k.PNG",confidence = 0.8)
	p.click(stpm_terminate)
	time.sleep(2)
	stpm_reset = p.locateCenterOnScreen("pic/stpm_reset_4k.PNG",confidence = 0.7)
	p.click(stpm_reset)
	time.sleep(2)

#====stpm_stid press=======
	stpm_stid = p.locateCenterOnScreen("pic/stpm_stid_4k.PNG",confidence = 0.5)
	p.keyDown("ctrl")
	p.keyDown("alt")
	p.click(stpm_stid)
	p.keyUp("alt")
	p.keyUp("ctrl")
	time.sleep(5)
#=====stpm_setup press=======
	stpm_setup = p.locateCenterOnScreen("pic/stpm_setup_4k.PNG",confidence = 0.5)
	p.click(stpm_setup)
	time.sleep(1)
#=====stpm_scanAll============
	if flag == "0":
		stpm_scan_all = p.locateCenterOnScreen("pic/stpm_scan_all_4k.PNG",confidence = 0.8)
		p.click(stpm_scan_all)
		time.sleep(1)
#=====stpm_check_both
		stpm_check_both = p.locateCenterOnScreen("pic/stpm_check_both_4k.PNG",confidence = 0.9)
		p.click(stpm_check_both)
		time.sleep(1)
#=====stpm_check_device
		stpm_check_device = p.locateCenterOnScreen("pic/stpm_check_device_4k.PNG",confidence = 0.9)
		p.click(stpm_check_device)
		time.sleep(1)
		stpm_alert = p.locateCenterOnScreen("pic/stpm_alert_4k.PNG",confidence = 0.8)
		time.sleep(2)
		if stpm_alert is not None:
			p.click(stpm_alert)
	
		time.sleep(1)
#=====stpm_auto_run
		stpm_autorun = p.locateCenterOnScreen("pic/stpm_autorun_4k.PNG",confidence = 0.9)
		p.click(stpm_autorun)
		time.sleep(1)

#=====stpm_edit_plan
	stpm_edit_plan = p.locateCenterOnScreen("pic/stpm_edit_plan_4k.PNG",confidence = 0.9)
	p.click(stpm_edit_plan)
	time.sleep(1)
#=====stpm_test_item===============================
	stpm_test_item = p.locateCenterOnScreen("pic/stpm_test_item_4k.PNG",confidence = 0.9)
	p.click(stpm_test_item)
	time.sleep(2)
	if flag =="1":
		stpm_test_item_wb = p.locateCenterOnScreen("pic/stpm_test_item_wb_4k.PNG",confidence = 0.9)
		p.click(stpm_test_item_wb)
		time.sleep(2)
#=====stpm_coldboot
	stpm_coldboot = p.locateCenterOnScreen("pic/stpm_coldboot_4k.PNG",confidence = 0.8)
	p.click(stpm_coldboot)
	time.sleep(1)
#======stpm_count_down
	stpm_count_down = p.locateCenterOnScreen("pic/stpm_count_down_4k.PNG",confidence = 0.8)
	p.click(stpm_count_down)
	p.typewrite(['backspace','backspace'],interval=0.5)
#alert
	stpm_alert = p.locateCenterOnScreen("pic/stpm_alert_4k.PNG",confidence = 0.8)
	p.click(stpm_alert)
	time.sleep(1)
	p.typewrite(in_count_down_time,interval=0.5)
#=======stpm_sleep_time
	stpm_sleep_time = p.locateCenterOnScreen("pic/stpm_sleep_time_4k.PNG",confidence = 0.8)
	p.click(stpm_sleep_time)
	time.sleep(1)
	p.typewrite(['backspace','backspace'],interval=0.5)
#alert
	stpm_alert = p.locateCenterOnScreen("pic/stpm_alert_4k.PNG",confidence = 0.8)
	p.click(stpm_alert)
	time.sleep(1)
	p.typewrite(in_sleep_time,interval=0.5)
#========stpm_execute_count
	stpm_execute_count = p.locateCenterOnScreen("pic/stpm_execute_count_4k.PNG",confidence = 0.8)
	p.click(stpm_execute_count)
	p.typewrite(['backspace','backspace'],interval=0.5)
#alert
	stpm_alert = p.locateCenterOnScreen("pic/stpm_alert_4k.PNG",confidence = 0.8)
	p.click(stpm_alert)
	time.sleep(1)
	p.typewrite(in_cycles,interval=0.5)
#========stpm_add_new_group
	stpm_add_new_group = p.locateCenterOnScreen("pic/stpm_add_new_group_4k.PNG",confidence = 0.8)
	p.click(stpm_add_new_group)
	time.sleep(1)
#========stpm_save_default_plan
	stpm_save_default_plan = p.locateCenterOnScreen("pic/stpm_save_default_plan_4k.PNG",confidence = 0.8)
	p.click(stpm_save_default_plan)
	time.sleep(1)
#=========stpm_savenexit
	if flag =="1":
		stpm_setup = p.locateCenterOnScreen("pic/stpm_setup_4k.PNG",confidence = 0.5)
		p.click(stpm_setup)
		time.sleep(1)
		stpm_autorun_checked = p.locateCenterOnScreen("pic/stpm_autorun_checked_4k.PNG",confidence = 0.9)
		p.click(stpm_autorun_checked)
		time.sleep(1)
		stpm_autorun = p.locateCenterOnScreen("pic/stpm_autorun_4k.PNG",confidence = 0.9)
		p.click(stpm_autorun)
		time.sleep(1)
		stpm_edit_plan = p.locateCenterOnScreen("pic/stpm_edit_plan_4k.PNG",confidence = 0.9)
		p.click(stpm_edit_plan)
		time.sleep(1)

	stpm_savenexit = p.locateCenterOnScreen("pic/stpm_savenexit_4k.PNG",confidence = 0.8)
	p.click(stpm_savenexit)
	time.sleep(1)

	end_time = time.time()

	print("Time eplased :",end_time- start_time)

#========main==================================================
screen =p.size() # get the resolution
print(screen)
count_down_time=input("Count Down time before test : ")
sleep_time=input("Sleep & suspend time : ")
cycles =input("Cycles : ")

start_time = time.time()

in_count_down_time=[]
in_sleep_time=[]
in_cycles=[]
for i in count_down_time:
	in_count_down_time.append(i)
for j in sleep_time:
	in_sleep_time.append(j)
for k in cycles:
	in_cycles.append(k)
in_sleep_time.insert(1,"del")


os.system("mode con cols=80 lines=20")
#

#
locate = os.getcwd() #get current directory
STPM = locate+"/STPM_V2.5.1.0(Build_01021743)"
STPM_ini = STPM+"/ITPM_DriverUpdate_20190313"
plan = STPM+"/PLAN"

if screen == (1920,1080):
	event_log_clean()
	Full_HD()
if screen == (3840,2160):
	event_log_clean()
	Four_K()
	







        

