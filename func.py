def file_sorting(filename):
    print("File is sorted and output file is created")
    file = open(filename, 'r')  # opening the input file in read mode
    file2 = open("out.txt", 'w')  # opening a output in write mode

    list_of_lines = []

    for line in file:
        if (line[-1] == '\n'):
            list_of_lines.append(
                line[:-1].split(" "))  # deleting the EOF character if there is one and splitting it by whitespaces
        else:
            list_of_lines.append(line.split(" "))

    for i in range(len(list_of_lines) - 1, -1, -1):  # sorting by year
        for k in range(i):

            if int(list_of_lines[k][1].split('/')[2]) > int(list_of_lines[k + 1][1].split('/')[2]):
                temp = list_of_lines[k]
                list_of_lines[k] = list_of_lines[k + 1]
                list_of_lines[k + 1] = temp

    for i in range(len(list_of_lines) - 1, -1, -1):  # sorting by month
        for k in range(i):
            if (int(list_of_lines[k][1].split('/')[2]) == int(list_of_lines[k + 1][1].split('/')[2])):
                if int(list_of_lines[k][1].split('/')[1]) > int(list_of_lines[k + 1][1].split('/')[1]):
                    temp = list_of_lines[k]
                    list_of_lines[k] = list_of_lines[k + 1]
                    list_of_lines[k + 1] = temp

    for i in range(len(list_of_lines) - 1, -1, -1):  # sorting by day
        for k in range(i):
            if (int(list_of_lines[k][1].split('/')[1]) == int(list_of_lines[k + 1][1].split('/')[1])):
                if int(list_of_lines[k][1].split('/')[0]) > int(list_of_lines[k + 1][1].split('/')[0]):
                    temp = list_of_lines[k]
                    list_of_lines[k] = list_of_lines[k + 1]
                    list_of_lines[k + 1] = temp

    for i in range(len(list_of_lines) - 1, -1, -1):  # sorting by login time
        for k in range(i):
            if (int(list_of_lines[k][1].split('/')[0]) == int(list_of_lines[k + 1][1].split('/')[0])):
                if int(list_of_lines[k][2]) > int(list_of_lines[k + 1][2]):
                    temp = list_of_lines[k]
                    list_of_lines[k] = list_of_lines[k + 1]
                    list_of_lines[k + 1] = temp

        if (i != 0):  # output of sorted log file
            file2.write(str(list_of_lines[i][0] + " " + list_of_lines[i][1] + " " + list_of_lines[i][2]) + '\n')
        else:
            file2.write(str(list_of_lines[i][0] + " " + list_of_lines[i][1] + " " + list_of_lines[i][2]))

    file.close()


def search_file(filename, date):
    file = open(filename, 'r')
    # date = input("Sorting of log file is completed\nIf you want to search for a specific date\nEnter a date for showing the logs in that date\nThe date format should be like this\n\t(day/month/year)\n\t")
    found = []

    for line in file:  # adding found date to a array
        splited_line = line.split(" ")
        if (str(splited_line[1]) == str(date)):
            found.append(splited_line)

    for i in range(len(found) - 1):  # sorting the dates by their login time
        if found[i][2] > found[i + 1][2]:
            temp = found[i]
            found[i] = found[i + 1]
            found[i + 1] = temp

    if (len(found) == 0):  # if there is no date in the log file
        return ("No date found\n")
    else:  # printing the result of search sorted by login date
        result = ("There are {0} entry/entries in {1} \n".format(len(found), date))
        for f in found:
            a = ("ip: {0}\tdate:{1}\tlogin time:{2} second\n".format(f[0], f[1], f[2]))
            result += a
        return result
