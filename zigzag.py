import time


while True:
    for number_of_spaces in range(0, 6):
        print(' '*number_of_spaces + '******')
        time.sleep(0.15)
    for number_of_spaces in range(6, 0, -1):
        print(' '*number_of_spaces + '******')
        time.sleep(0.15)
