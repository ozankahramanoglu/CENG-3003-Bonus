# This python programme creates a random example data for assignment.

# Data file format will appear like this

# 1.1.1.1 10/10/2017 111
# ip+(whitespace)+day/month/year+(whitespace)+login time in second

# Output file name will be "log.txt"

import random as r  # importing random module


def random_log_generator():
    line_count = 2048

    log_txt = open("log.txt", 'w')  # opening a text file in write mode. This means old file will be deleted

    for i in range(0, line_count):
        line = ""  # a line variable
        for j in range(0, 4):
            line = line + str(r.randrange(1, 255)) + '.'  # creating a random ip
            if (j == 3):
                line = line[:-1]  # deleting the last dot

        line += ' ' + str(r.randrange(1, 31)) + '/' + str(r.randrange(1, 13)) + '/' + str(r.randrange(2010, 2018))
        # creating a random date
        line += ' ' + str(r.randrange(20, 2000))  # creating a random
        if (i != line_count - 1):
            line += '\n'  # adding a EOF end of lines
        log_txt.write(line)  # writing line to text file

    log_txt.close()


random_log_generator()
