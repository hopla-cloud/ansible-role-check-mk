#!/usr/bin/python
# _ _ _
#(_|_) |
# _ _| |_   _  ___
#| | | | | | |/ _ \
#| | | | |_| | |_| |
#|_|_|_|\__  |\___/
#      (____/
#
# - Writer : Joffrey Skandera
# - Version : 1.2
#
#
#

#import subprocess
#from subprocess import Popen

#p = Popen(["acrocmd","list","plans","--output=raw","--filter_status=ok"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#plan_ok, errors = p.communicate()
#p = Popen(["acrocmd","list","plans","--output=raw","--filter_status=warning"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#plan_warning, errors = p.communicate()
#p = Popen(["acrocmd","list","plans","--output=raw","--filter_status=error"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#plan_error, errors = p.communicate()

#if len(plan_ok)> len(plan_warning) and len(plan_ok)> len(plan_error):
#	print("0 Acronis_Backup - No error in last backup")

#if len(plan_warning)> len(plan_ok) and len(plan_warning)> len(plan_error):
#	print("1 Acronis_Backup - Warning in last backup")

#if len(plan_error)> len(plan_warning) and len(plan_error)> len(planok):
#	print("2 Acronis_Backup - Error in last backup")
print("0 Acronis_Backup - No Check")
