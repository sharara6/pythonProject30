
    finish = 'y'

    while finish == 'y':


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
