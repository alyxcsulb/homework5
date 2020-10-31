# task 1 
# should have output "The class average is 79 for 3 students."

import os
READ_FILE_NAME = 'scores.txt'
READ_MODE = 'r'
WRITE_FILE_NAME = 'log.txt'
WRITE_MODE = 'w'
STUDENT_COUNT = 0
TOTAL_SCORE = 0

with open (READ_FILE_NAME, WRITE_MODE) as names_file:
    names_file.write ('Alice 69\n')
    names_file.write ('Bob 89\n')
    names_file.write ('Cindy 79\n')
    names_file.write ('Bob eighty-seven\n')
    names_file.write ('Eric abc\n')

try:
    with open (WRITE_FILE_NAME, WRITE_MODE) as logged_file:
        with open(READ_FILE_NAME, READ_MODE) as names_file:
            for line in names_file:
                student_name, student_score = line.split()
                try:
                    TOTAL_SCORE += int(student_score)
                except ValueError as error:
                    logged_file.write(f'Bad score value for {student_name}, is ignored.\n')
                else: STUDENT_COUNT += 1
        logged_file.write(f'The class average is {TOTAL_SCORE / STUDENT_COUNT} for {STUDENT_COUNT} students.')
        print(f'The class average is {TOTAL_SCORE / STUDENT_COUNT} for {STUDENT_COUNT} students.')
except IOError as error:
    print(f'File {READ_FILE_NAME} is unable to open. Error message: {error}.')



