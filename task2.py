# task 2:
# letters are case IN-sensitive ( a = A)
# summary should show count of letters in book

import os

READ_SENTENCE = 'book.txt'
READ_MODE = 'r'
WRITE_LETTERS = 'summary.txt'
WRITE_MODE = 'w'

try:
    with open (WRITE_LETTERS, WRITE_MODE) as summ_file:
        with open (READ_SENTENCE, READ_MODE) as book_file:
            letter_count = []
            total_letters = ''
            lines = book_file.read()
            lines = lines.lower()
            lines = sorted(lines)
            for i in range(1, 100):
                amount = 0 
                for line in lines:
                    letter_count += line
        letter_count = [letter.upper() for letter in letter_count]
        print(f'{i} {letter_count}')
        if letter_count.count(i) == 0:
            print ("It does not have all 26 letters.")
        else:
            print ("It has all 26 letters")
