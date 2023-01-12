import json  # json is a function to allow dictionaries to be written in files


def teacher():
    group1 = [111]
    group2 = [112]
    english = [156]
    ethics = [150]
    finish = 'y'
    while finish == 'y':
                while True:
                    try:
                        id = int(input('Enter course ID:'))
                        break
                        while id not in ethics and id not in english:
                                id = int(input('Error! enter correct course id:'))
                    except:
                        print('Eror!only numbers are allowed ')



                if id in english:
                    while True:
                        try:
                            group = int(input('Group number:'))
                            break

                            while group not in group1 and group not in group2:
                                while True:
                                    try:
                                        group = int(input('Error! Enter correct group:'))
                                        break
                                    except:
                                        print('Error only numbers are allowed')
                            if group in group1:
                                id_grade_156_1()

                            elif group in group2:
                                id_grade_156_2()
                        except:
                            print('Error only numbers are allowed')

                elif id in ethics:
                    while True:
                        try:
                            group = int(input('Group number:'))
                            break
                            while group not in group1 and group not in group2:
                                group = int(input('Error! Enter correct group:'))

                            if group in group1:
                                id_grade_150_1()

                            elif group in group2:
                                id_grade_150_2()
                        except:
                            print('Error only numbers are allowed')
                while True:
                    try:
                        finish = input("Do you want to add other grades ? '(y) for yes (n) for no':")
                        break
                    except:
                        print('Error only enter letters')

    return



def id_grade_156_1():
    group1_id = [202201, 202202, 202203, 202204, 202205]
    i = 5
    id_student1 = {}
    abs_student1={}
    while i > 0:
        while True :
            try:
                stu_id1 = (int(input('Enter student Id:')))
                break
            except:
                print('Error only numbers are allowed')

        while stu_id1 not in group1_id:
            while True:
                try:
                    stu_id1 = int(input('Error! please enter correct ID:'))
                    break
                except:
                    print('Error only enter numbers')
        while True:
            try:
                stu_grade1 = (int(input('Enter grade of student:')))
                break
            except:
                print('Error enter numbers only')
        while stu_grade1 > 100 or stu_grade1 < 0:
            while True:
                try:
                    stu_grade1 = (int(input('Error!please enter correct grades:')))
                    break
                except:
                    print('Error enter numbers only')
        id_student1[stu_id1] = stu_grade1
        i -= 1
        abs_student1[stu_id1] = absence()
        if i >= 1:
            while True:
                try:
                    cont = input("if you finished this group please press (y) or (n) if not finished:")
                    break
                except:
                    print('Error enter letters only')
        if cont == 'y':
            break

    file = open('file156(g).txt', 'w')
    # ('Group (1) English grades: ')
    file.write(json.dumps(id_student1))
    # json.dumps is a function to allow dictionaries to be written in files
    file.write('\n')
    file.close()
    # file.write('group (1) absence days in English:')
    file1=open('file156(a).txt','w')
    file1.write(json.dumps(abs_student1))
    file1.write('\n')
    file1.close()
    return file,file1






def id_grade_156_2():
    group2_id=[202206,202207,202208,202209,202210]
    i=5
    id_student2 = {}
    abs_student2 = {}
    while i > 0:
        while True:
            try:
                stu_id2 = (int(input('Enter student Id:')))
                break
            except:
                print('Error enter numbers only')
        while stu_id2 not in group2_id:
            while True:
                try:
                    stu_id2 = int(input('Error! please enter correct ID:'))
                    break
                except:
                    print('Error enter numbers only')
        while True:
            try:
                stu_grade2 = (int(input('Enter grade of student:')))
                break
            except:
                print('Error enter numbers only')
        while stu_grade2 > 100 or stu_grade2 < 0:
            while True:
                try:
                    stu_grade2 = (int(input('Error!please enter correct grades:')))
                    break
                except:
                    print('Error enter numbers only')
        id_student2[stu_id2] = stu_grade2
        abs_student2[stu_id2] = absence()
        i -= 1

        if i >= 1:
            while True:
                try:
                    cont = input("if you finished this group please press (y) or (n) if not finished:")
                    break
                except:
                    print('Error enter letters only')

        if cont == 'y':
            break

    file2 = open('file156(g2).txt', 'w')
   # ('Group (2) English grades: ')
    file2.write(json.dumps(id_student2))
    # json.dumps is a function to allow dictionaries to be written in files
    file2.write('\n')
    file2.close()
   # ('group (2) absence days in English:')
    file3=open('file156(a2).txt',"w")
    file3.write(json.dumps(abs_student2))
    file3.write('\n')
    file3.close()
    return file2,file3



def id_grade_150_1():
    group1_id = [202201, 202202, 202203, 202204, 202205]
    i = 5
    id_student1 = {}
    abs_student1 = {}
    while i > 0:
        while True:
            try:
                stu_id1 = (int(input('Enter student Id:')))
                break
            except:
                print('Error enter numbers only')
        while stu_id1 not in group1_id:
            while True:
                try:
                    stu_id1 = int(input('Error! please enter correct ID:'))
                    break
                except:
                    print('Error enter numbers only')
        while True:
            try:
                stu_grade1 = (int(input('Enter grade of student:')))
                break
            except:
                print('Error enter numbers only')
        while stu_grade1 > 100 or stu_grade1 < 0:
            while True:
                try:
                    stu_grade1 = (int(input('Error!please enter correct grades:')))
                    break
                except:
                    print('Error enter numbers only')
        id_student1[stu_id1] = stu_grade1
        abs_student1[stu_id1] = absence()
        i -= 1

        if i >= 1:
            while True:
                try:
                    cont = input("if you finished this group please press (y) or (n) if not finished:")
                    break
                except:
                    print('Error enter letter only')

        if cont == 'y':
            break

    file4 = open('file150(g).txt', 'w')
    #                   if written in here file will reset grades
    #('Group (1) Ethics grades: ')
    file4.write(json.dumps(id_student1))
    # json.dumps is a function to allow dictionaries to be written in files
    file4.write('\n')
    file4.close()
    #file.write('group (1) absence days in Ethics:')
    file5=open('file150(a).txt','w')
    file5.write(json.dumps(abs_student1))
    file5.write('\n')
    file5.close()
    return file5,file4



def id_grade_150_2():
    group2_id = [202206, 202207, 202208, 202209, 202210]
    i = 5
    id_student2 = {}
    abs_student2 = {}
    while i > 0:
        while True:
            try:
                stu_id2 = (int(input('Enter student Id:')))
                break
            except:
                print('Error enter numbers only')

        while stu_id2 not in group2_id:
            while True:
                try:
                    stu_id2 = int(input('Error! please enter correct ID:'))
                    break
                except:
                    print('Error enter numbers only')
        while True:
            try:
                stu_grade2 = (int(input('Enter grade of student:')))
                break
            except:
                print('Error enter numbers only')

        while stu_grade2 > 100 or stu_grade2 < 0:
            while True:
                try:
                    stu_grade2 = (int(input('Error!please enter correct grades:')))
                    break
                except:
                    print('Error enter numbers only')
        id_student2[stu_id2] = stu_grade2
        i -= 1
        abs_student2[stu_id2] = absence()

        if i >= 1:
            while True:
                try:
                    cont = input("if you finished this group please press (y) or (n) if not finished:")
                    break
                except:
                    print('Error enter numbers only')

        if cont == 'y':
            break

    file6 = open('file150(g2).txt', 'w')
    #('Group (2) Ethics grades: ')
    file6.write(json.dumps(id_student2))
    # json.dumps is a function to allow dictionaries to be written in files
    file6.write('\n')
    file6.close()
    #('group (2) absence days in Ethics:')
    file7 = open('file150(a2).txt','w')
    file7.write(json.dumps(abs_student2))
    file7.write('\n')
    file7.close()
    return file7,file6




def absence():
    abs=(int(input('Enter absence days:')))
    while abs < 0 or abs < 15:
        while True:
            try:
                abs = int(input('Erorr! PLease enter correct absence days:'))
                break
            except:
                print('Error enter numbers only')
    return abs






if __name__ == "__main__":
    teacher()
    file = open("file156.txt", 'r')
    for line in file:
        print(line)
    file.close()
    file2 = open('file150.txt', 'r')
    for line2 in file2:
        print(line2)
    file2.close()