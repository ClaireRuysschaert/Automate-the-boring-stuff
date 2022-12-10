# Import the grades from the students.py here

# Write a function that takes a student name and a subject as arguments
# e.g. `python exercise_1.py Yuki Math` should print 16

import sys
from students import grades


def grades_giver(student_name, subject_to_find):
    grades_dict = grades[student_name]
    for subject, notes in grades_dict.items():
        if subject == subject_to_find:
            return notes

if __name__ == '__main__': 
    print(grades_giver(sys.argv[1], sys.argv[2]))
