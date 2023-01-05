import threading
import time

print("Start of program.")


def take_a_nap():
    time.sleep(5)
    print("Wake up!")


thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()

print("End of program.")

# Passing arguments in args with a list and keyword arg in a dict
thread_obj_2 = threading.Thread(
    target=print, args=["Yuki", "TDB"], kwargs={"sep": " & "}
)
thread_obj_2.start()

# avoid concurrency issues : never let multiple threads read/write the same
# variables
