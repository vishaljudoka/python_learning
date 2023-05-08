"""
# Script for NAS monitoring
#last Modified : 28/09/2020
#Changed By : VS
#parameteres : NAS location to be monitoring
#Duartion : Duration in minutes file siting in NAS
#Eg : NAS_File_Check.py D:\foldername 15
"""
import os
import time
from sys import argv


path=str(argv[1])
path_r='r"'+path +'"'
min_monitor=int(argv[2])

os.chdir(path)
print("Sno ," ,"NASPath " ,", File ," , " Minutes elapsed , " ," Last Modified date")
sno=0

def secondsToform(secs):
    days = secs//86400
    hours = (secs - days*86400)//3600
    minutes = (secs - days*86400 - hours*3600)//60
    seconds = secs - days*86400 - hours*3600 - minutes*60
    result = ("{0} day{1}: ".format(days, "s" if days!=1 else "") if days else "") + \
    ("{0} hour{1}: ".format(hours, "s" if hours!=1 else "") if hours else "") + \
    ("{0} minute{1}: ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
    ("{0} second{1} ".format(seconds, "s" if seconds!=1 else "") if seconds else "")
    return result

for file in os.listdir("."):
    if os.path.isfile(file) and not file.startswith(("Archive" )):
        ab=time.ctime(os.path.getmtime(file))
        time_mod =os.path.getmtime(file)
        time_cur =time.time()
        sno+=1
    if time_cur !=time_mod:
        min_chg=int((time_cur -time_mod)// 60)
        if min_chg >min_monitor :
            print( sno ," , ", path , " , ", file, " , minutes_elapsed:",str(secondsToform(min_chg*60)), " , Modified_date :", ab )

print( "Total Count" ," , ", sno )