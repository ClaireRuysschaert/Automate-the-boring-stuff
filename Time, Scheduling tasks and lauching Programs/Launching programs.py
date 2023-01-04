import subprocess

#Popen returns poll() and wait()
    # poll = "are the program still open" 
        # return None if the programm still runs
        # returns an exit code : 0 if it's close
    # wait = block until the process has terminated

paintProc = subprocess.Popen('c:\\Windows\\System32\\mspaint.exe')
print(paintProc.poll() == None)
paintProc.wait() # Doesn't return until MS Paint closes.
print(paintProc.poll())

#directly open a file
#subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\Users\netcl\\hello.txt'])

#Task scheluder, launchd and cron
import datetime
print(datetime.datetime(2019, 1, 7))
