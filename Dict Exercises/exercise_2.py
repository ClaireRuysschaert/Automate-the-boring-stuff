# Compute and rank the grades of the students (average of all subjects)
# e.g. `python exercise_2.py` should print something like:
# Yuki: 18.0
# Mozart: 11.2
# Kumo: 9.0
# Globule: 7.75

# Tip : https://www.programiz.com/python-programming/methods/built-in/sorted

from students import grades

unorder_moy_list = {}
for student in grades:
    moy = sum(grades[student].values())/len(grades[student])
    unorder_moy_list[student] = moy
    
tuple_items = unorder_moy_list.items()
sorted_list = sorted(tuple_items, reverse=True)

for student, moyenne in sorted_list:
    print(f'{student} : {moyenne}')
