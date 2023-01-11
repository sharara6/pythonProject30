import trial

def teacher_check():
    pw = [999]
    #  passwords for teachers
    p = int(input('Please enter your password:'))
    if p in pw:
        trial.teacher()
    while p not in pw:
        p = int(input('Error!Please enter a valid password:'))

