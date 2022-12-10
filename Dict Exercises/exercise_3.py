# Show the list of students for each subject
# e.g. `python exercise_3.py` should print
# Math: Yuki, Mozart, Kumo, Globule
# English: Yuki, Mozart, Kumo, Globule
# Science: Yuki, Mozart, Kumo, Globule
# Music: Mozart
# Greek: Mozart, Globule

from students import grades

def which_one():
    dict_students_subjects = {}
    for student, subject_grades in grades.items():
        for subject in subject_grades.keys():
            if subject in dict_students_subjects:
                dict_students_subjects[subject].append(student) 
            else:
                dict_students_subjects[subject] = [student]
    
    for keys, values_list in dict_students_subjects.items():
        print(f'{keys} : ' + ', '.join(values_list))

which_one()

# default dict from collection import DD