import trial

def teacher_check():
    pw = [999]
    #  passwords for teachers
    while True:
        try:
            p = int(input('Please enter your password:'))
            if p in pw:
                trial.teacher()
                break
            while p not in pw:
                p = int(input('Error!Please enter a valid password:'))
        except:
            print('Error! only numbers are allowed')



