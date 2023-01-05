# Prettified stopwatch and copy the result to the pyperclip

import time
import pyperclip 

#Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1
lap_resut = []
# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)

        #format to string
        f_total_time = str(totalTime).rjust(5)
        f_lap_time = str(lapTime).rjust(5)
        
        formatted_lap = (f'Lap # {lapNum}: {f_total_time} ({f_lap_time})')
        print(formatted_lap)
        lap_resut.append(formatted_lap)

        lapNum += 1
        lastTime = time.time() # reset the last lap time    

except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')

pyperclip.copy('\n'.join(lap_resut))
print('Your lap have been copied! Just paste it in a mail or message!')
