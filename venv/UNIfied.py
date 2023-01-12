import teacher
import The_Student_portal
     # group1 = [111]
     # group2 = [112]
     # english = [156]
     # ethics = [150]
     # group1_id = [202201, 202202, 202203, 202204, 202205]
     # group2_id = [202206, 202207, 202208, 202209, 202210]
     # pw = [999]


def student_teacher():
    t= ['t','T']
    s= ['s','S']
    while True:
        try:
            s_t = input('If you are a teaher press (t) ,If you are a student press (s):')
            break
        except:
            print('only liters are allowed')
    while s_t not in t and s_t not in s:
        while True:
            try:
                s_t = input('Please enter a valid answer:')
                break
            except:
                print('only liters are allowed')
    if s_t in t:
        teacher.teacher_check()  #teacher portal
    elif s_t in s:
        The_Student_portal.Student_portal()








# if __name__ == "__main__":
#     student_teacher()
#     file = open("file156.txt", 'r')
#     for line in file:
#         print(line)
#     file.close()
#     file2 = open('file150.txt', 'r')
#     for line2 in file2:
#         print(line2)
#     file2.close()