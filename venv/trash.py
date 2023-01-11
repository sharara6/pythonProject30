
def course_id_section():
    group1 = [111]
    group1_id = [202201, 202202, 202203, 202204, 202205]
    group2 = [112]
    group2_id = [202206, 202207, 202208, 202209, 202210]
    english = [156]
    ethics = [150]
    finish = 'y'
    i = 5

    while finish == 'y':
        id = int(input('Enter course ID:'))

        while id not in ethics and id not in english:
            id = int(input('Error! enter correct course id:'))

        if id in english:
            group = int(input('Group number:'))

            while group not in group1 and group not in group2:
                group = int(input('Error! Enter correct group:'))

            if group in group1:
                id_student1 = {}

                while i > 0:
                    stu_id1 = (int(input('Enter student Id:')))

                    while stu_id1 not in group1_id:
                        stu_id1 = int(input('Error! please enter correct ID:'))
                    stu_grade1 = (int(input('Enter grade of student:')))

                    while stu_grade1 > 100 or stu_grade1 < 0:
                        stu_grade1 = (int(input('Error!please enter correct grades:')))
                    id_student1[stu_id1] = stu_grade1
                    i -= 1

                    if i >= 1:
                        cont = input("if you finished this group please press (y) or (n) if not finished:")

                    if cont == 'y':
                        break

                file = open('file156.txt', 'w')
                #                   if written in here file will reset grades
                file.write('Group (1) English grades: ')
                file.write(json.dumps(id_student1))
                # json.dumps is a function to allow dictionaries to be written in files
                file.write('\n')
                file.close()

            elif group in group2:
                id_student2 = {}

                while i > 0:
                    stu_id2 = (int(input('Enter student Id:')))

                    while stu_id2 not in group2_id:
                        stu_id2 = int(input('Error! please enter correct ID:'))
                    stu_grade2 = (int(input('Enter grade of student:')))

                    while stu_grade2 > 100 or stu_grade2 < 0:
                        stu_grade2 = (int(input('Error!please enter correct grades:')))
                    id_student2[stu_id2] = stu_grade2
                    i -= 1

                    if i >= 1:
                        cont = input("if you finished this group please press (y) or (n) if not finished:")

                    if cont == 'y':
                        break

                file = open('file156.txt', 'a')
                file.write('Group (2) English grades: ')
                file.write(json.dumps(id_student2))
                # json.dumps is a function to allow dictionaries to be written in files
                file.write('\n')
                file.close()

        elif id in ethics:
            group = int(input('Group number:'))

            while group not in group1 and group not in group2:
                group = int(input('Error! Enter correct group:'))

            if group in group1:
                id_student1 = {}

                while i > 0:
                    stu_id1 = (int(input('Enter student Id:')))

                    while stu_id1 not in group1_id:
                        stu_id1 = int(input('Error! please enter correct ID:'))

                    stu_grade1 = (int(input('Enter grade of student:')))
                    while stu_grade1 > 100 or stu_grade1 < 0:
                        stu_grade1 = (int(input('Error!please enter correct grades:')))

                    id_student1[stu_id1] = stu_grade1
                    i -= 1

                    if i >= 1:
                        cont = input("if you finished this group please press (y) or (n) if not finished:")

                    if cont == 'y':
                        break

                file2 = open('file150.txt', 'w')
                #                   if written in here file will reset grades
                file2.write('Group (1) Ethics grades: ')
                file2.write(json.dumps(id_student1))
                # json.dumps is a function to allow dictionaries to be written in files
                file2.write('\n')
                file2.close()

            elif group in group2:
                id_student2 = {}

                while i > 0:
                    stu_id2 = (int(input('Enter student Id:')))

                    while stu_id2 not in group2_id:
                        stu_id2 = int(input('Error! please enter correct ID:'))
                    stu_grade2 = (int(input('Enter grade of student:')))

                    while stu_grade2 > 100 or stu_grade2 < 0:
                        stu_grade2 = (int(input('Error!please enter correct grades:')))
                    id_student2[stu_id2] = stu_grade2
                    i -= 1

                    if i >= 1:
                        cont = input("if you finished this group please press (y) or (n) if not finished:")

                    if cont == 'y':
                        break

                file2 = open('file150.txt', 'a')
                file2.write('Group (2) Ethics grades: ')
                file2.write(json.dumps(id_student2))
                # json.dumps is a function to allow dictionaries to be written in files
                file2.write('\n')
                file2.close()

        finish = input("Do you want to add other grades ? '(y) for yes (n) for no':")

    return


if __name__ == "__main__":
    teacher_check()
    file = open("file156.txt", 'r')
    for line in file:
        print(line)
    file.close()
    file2 = open('file150.txt', 'r')
    for line2 in file2:
        print(line2)
    file2.close()
