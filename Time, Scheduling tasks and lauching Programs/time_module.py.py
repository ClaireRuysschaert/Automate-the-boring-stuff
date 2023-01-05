import time


def calc_prod():
    product = 1
    for i in range(1, 10000):
        product = product * i
    return product


# time.time() = epoch timestamp
start_time = time.time()
prod = calc_prod()
end_time = time.time()
print(f"The result is {len(str(prod))} digits long.")
print(f"Took {end_time - start_time} to calculate.")

# more readable with time.ctime()
final_time = time.ctime(end_time - start_time)
print(final_time)

# make a pause : time.sleep()
for i in range(2):
    print("Tick")
    time.sleep(1)
    print("Tock")
    time.sleep(1)

# rounding numbers with round()
print(round(start_time, 2))
print(round(start_time))
